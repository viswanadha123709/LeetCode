import sys
sys.setrecursionlimit(5000)

maxi = 10**5
isprime = [True] * (maxi + 1)
isprime[0] = isprime[1] = False

for i in range(2, int(maxi ** 0.5) + 1):
    if isprime[i]:
        for j in range(i * i, maxi + 1, i):
            isprime[j] = False

primes = []

for i in range(maxi + 1):
    if isprime[i]:
        primes.append(i)


class Solution:
    def smallestValue(self, n: int) -> int:

        def generate(n):
            if isprime[n]:
                return n

            for i in primes:
                if n % i == 0:
                    return i + generate(n // i)

        while not isprime[n]:
            new_n = generate(n)

            if new_n == n:
                return n

            n = new_n

        return n