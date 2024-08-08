
my_string = "Hello,World,This,Is,Python"


words = my_string.split(",")


print("Split string:")
print(words)


joined_string = "-".join(words)


print("\nJoined string:")
print(joined_string)


numbers = ["1", "2", "3", "4", "5"]
comma_separated = ",".join(numbers)
print(comma_separated)  # Output: "1,2,3,4,5"

names = ["John", "Mary", "Jane", "Bob"]
dash_separated = "-".join(names)
print(dash_separated)  # Output: "John-Mary-Jane-Bob"s