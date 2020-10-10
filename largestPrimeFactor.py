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

    print(prime)

    return prime

def findPrimeFactor(n):
    primeList = primeGenerator(n)
    filtered = []

    for p in primeList:
        print(p)


test_num = 10
findPrimeFactor(test_num)
