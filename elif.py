
num = int(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
else:
    if num < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")

n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):
    print("*" * i)

for i in range(n - 1, 0, -1):
    print("*" * i)




x = int(input("Enter a number: "))

if x > 0:
    if x % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")
else:
    if x == 0:
        print("The number is zero.")
    else:
        if x % 2 == 0:
            print("The number is negative and even.")
        else:
            print("The number is negative and odd.")