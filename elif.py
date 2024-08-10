
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


# This is a comment - anything after the "#" symbol is ignored by the interpreter

# Print a message to the screen
print("Hello, World!")

# Ask the user for their name
name = input("What is your name? ")

# Print out a greeting with the user's name
print("Hello, " + name + "!")

# Ask the user for their age
age = int(input("How old are you? "))

# Print out a message based on the user's age
if age < 18:
    print("You're still young!")
else:
    print("You're all grown up!")