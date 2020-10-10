# function primeGenerator
def isPrime(x):
    if x <= 1:
        return False

    if x == 2:
        return True

    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False

    return True

def primeGenerator(n):
    prime = []
    for i in range(2, n):
        if isPrime(i):
            prime.append(i)

    return prime

def findPrimeFactor(n):
    primeList = primeGenerator(n)
    filtered = []

    for p in primeList:
        if n % p == 0:
            filtered.append(p)

    print(filtered)
    return filtered


def findMaxFactor(factors):
    return max(factors)


test_num = 600851475143
factors = findPrimeFactor(test_num)
myMaxFactor = findMaxFactor(factors)
print("The largest prime of", test_num, ' =', myMaxFactor)
