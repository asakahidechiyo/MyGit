#pragma once  // 现代头文件保护

#include <windows.h>

#include <expected>     // C++23: 用于优雅的错误处理
#include <filesystem>   // C++17: 路径处理专家
#include <print>        // C++23: 更安全高效的格式化输出
#include <string_view>  // C++17: 轻量级字符串视图

namespace sys {

/**
 * @brief 设置程序开机自启动
 * @return std::expected<void, LSTATUS> 成功返回空，失败返回 Windows 错误码
 */
[[nodiscard]]  // 提示调用者必须处理返回值
auto SetAutoRun(std::wstring_view valueName, std::filesystem::path targetPath)
    -> std::expected<void, LSTATUS> {
    const auto* subKey = L"Software\\Microsoft\\Windows\\CurrentVersion\\Run";
    HKEY hKey = nullptr;

    // 1. 打开/创建注册表项 (使用 Wide 版本以支持 Unicode)
    LSTATUS status = RegCreateKeyExW(HKEY_CURRENT_USER,  // 建议用 HKCU，无需管理员权限即可测试成功
                                     subKey, 0, nullptr, REG_OPTION_NON_VOLATILE, KEY_ALL_ACCESS,
                                     nullptr, &hKey, nullptr);

    if (status != ERROR_SUCCESS) {
        return std::unexpected(status);
    }

    // 使用 RAII 思路，虽然这里手动关闭，但更稳妥的做法是自定义 deleter
    struct KeyGuard {
        HKEY key;
        ~KeyGuard() {
            if (key)
                RegCloseKey(key);
        }
    } guard{hKey};

    // 2. 转换路径为字符串
    std::wstring pathStr = targetPath.wstring();

    // 3. 写入值 (注意字节数计算：包含空字符，乘以 sizeof(wchar_t))
    status = RegSetValueExW(hKey, valueName.data(), 0, REG_SZ,
                            reinterpret_cast<const BYTE*>(pathStr.c_str()),
                            static_cast<DWORD>((pathStr.length() + 1) * sizeof(wchar_t)));

    if (status != ERROR_SUCCESS) {
        return std::unexpected(status);
    }

    return {};
}

[[nodiscard]]
auto RemoveAutoRun(std::wstring_view valueName) -> std::expected<void, LSTATUS> {
    const auto* subKey = L"Software\\Microsoft\\Windows\\CurrentVersion\\Run";
    HKEY hKey = nullptr;

    // 1. 打开注册表项 (需要 KEY_SET_VALUE 权限来删除值)
    LSTATUS status = RegOpenKeyExW(HKEY_CURRENT_USER, subKey, 0,
                                   KEY_SET_VALUE,  // 仅申请删除权限
                                   &hKey);

    if (status != ERROR_SUCCESS) {
        // 如果找不到该键（可能路径被删了），直接返回错误
        return std::unexpected(status);
    }

    // 2. RAII 资源管理，确保函数退出时关闭句柄
    struct KeyGuard {
        HKEY key;
        ~KeyGuard() {
            if (key)
                RegCloseKey(key);
        }
    } guard{hKey};

    // 3. 删除指定的键值
    status = RegDeleteValueW(hKey, valueName.data());

    if (status != ERROR_SUCCESS) {
        return std::unexpected(status);
    }

    return {};
}

}  // namespace sys