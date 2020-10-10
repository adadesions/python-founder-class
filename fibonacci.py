a1 = 1
a2 = 2
an = a1 + a2
sum_ = a2 

print(a1, ',', a2, end=", ")
for n in range(100):
    an = a1 + a2
    if an > 4000000:
        print('\n=== DONE ===')
        break

    if an % 2 == 0:
        sum_ += an
        print(an, end=", ")

    a1 = a2
    a2 = an

print("Even term sum =", sum_)