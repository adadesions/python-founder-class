sum_ = 0
for n in range(1, 1000):
    if n % 3 == 0 or n % 5 == 0:
        print(n, end=", ")
        sum_ += n
print("sum =", sum_)