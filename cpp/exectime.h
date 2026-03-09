#pragma once
#include <chrono>
#include <iostream>
#include <thread>
#include <utility>
#include <vector>

namespace exet {
/**
 * @brief measure execution time for any function, para1 is the name of function, then give other
 * paras for your function
 * @return time in ms, which is std::chrono::milliseconds
 */
template <typename Func, typename... Args>
auto measureExecutionTime(Func&& func, Args&&... args) {
    using namespace std::chrono;
    milliseconds msBegin = duration_cast<milliseconds>(system_clock::now().time_since_epoch());
    std::forward<Func>(func)(std::forward<Args>(args)...);
    milliseconds msEnd = duration_cast<milliseconds>(system_clock::now().time_since_epoch());
    return milliseconds(msEnd).count() - milliseconds(msBegin).count();
}
}  // namespace exet