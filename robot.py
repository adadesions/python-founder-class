print("Robot: What's your name ?")
name = input("User: ")
print("Robot: Nice to meet you,", name)
print("Robot: How old are you ?")
age = input("User: ")
year = 2020 - int(age)
print("oh! your birth year is", year, "right? (y/n)")
ans = input("User: ")
if 'y' in ans:
    print("Robot: Such a genius")
else:
    print("Robot: My bad~")
print("Robot: Time up? (y/n)")
ans = input("User: ")
if 'y' in ans:
    print("Robot: Bye bye~")
else:
    print("Robot: But I have to go see ya!")
