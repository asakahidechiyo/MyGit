#include <iostream>

#include "exectime.h"

void TraditionalPrime(long long n) {
    for (long long nFactor = 2; nFactor * nFactor <= n; nFactor++) {
        if (n % nFactor == 0) {
            std::cout << n << " is not prime" << std::endl;
        }
    }
    std::cout << n << " is prime" << std::endl;
}

void ErastosthenesPrime(long long nSize, long long n) {
    std::vector<bool> isPrime;
    isPrime.assign(nSize + 1, true);
    isPrime[0] = isPrime[1] = false;
    std::cout << isPrime.size() << std::endl;
    for (int i = 2; i * i <= n; i++) {
        if (isPrime[i]) {
            for (int j = i * i; j <= n; j += i) {
                if (isPrime[j])
                    isPrime[j] = false;
            }
        }
    }
    if (isPrime[n])
        std::cout << n << " is prime" << std::endl;
    else
        std::cout << n << " is not prime" << std::endl;
}

int main() {
    auto msTrad = exet::measureExecutionTime(TraditionalPrime, 10000101);
    auto msEras = exet::measureExecutionTime(ErastosthenesPrime, 10000500, 10000101);
    std::cout << msTrad << " and " << msEras;
    system("pause");
}