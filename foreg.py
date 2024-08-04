# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use a for loop to iterate over the list
for num in numbers:
    # Calculate the square of the current number
    square = num ** 2
    # Print the result
    print(f"The square of {num} is {square}")

# Outer loop iterates over the rows
for i in range(1, 11):
    # Inner loop iterates over the columns
    for j in range(1, 11):
        # Print the product of the current row and column numbers
        print(f"{i} x {j} = {i*j}\t", end="")
    # Print a newline after each row
    print()