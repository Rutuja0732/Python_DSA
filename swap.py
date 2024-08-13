# Method 1: Using a temporary variable
a = 5
b = 10

print("Before swap: a =", a, "b =", b)

temp = a
a = b
b = temp

print("After swap: a =", a, "b =", b)

# Method 2: Without using a temporary variable
x = 5
y = 10

print("Before swap: x =", x, "y =", y)

x, y = y, x

print("After swap: x =", x, "y =", y)