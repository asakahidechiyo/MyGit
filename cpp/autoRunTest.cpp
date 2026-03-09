#include <filesystem>
#include <iostream>

#include "autorun.h"

auto setAutoRun(std::wstring_view name, std::filesystem::path targetPath) {
    return sys::SetAutoRun(name, targetPath);
}

int main() {
    std::wstring_view name = L"autoRunTest";
    std::filesystem::path selfPath = std::filesystem::current_path() / "autoRunTest.exe";
    auto setRes = setAutoRun(name, selfPath);
    if (setRes.has_value()) {
        std::cout << "autoRunTest ready" << std::endl;
    } else {
        std::cout << "error code: " << setRes.error() << std::endl;
    }
    auto rmvRes = sys::RemoveAutoRun(name);
    if (rmvRes.has_value()) {
        std::cout << "autoRunTest has been removed" << std::endl;
    } else {
        std::cout << "error code: " << rmvRes.error() << std::endl;
    }
    std::cin.get();
}