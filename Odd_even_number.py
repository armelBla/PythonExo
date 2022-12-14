number = int(input("Which number do you want to check? "))
number %= 2

if number == 0:
    print("This an even number.")
else:
    print("This is an odd number.")