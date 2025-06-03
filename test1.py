# Sample string array
string_array = ["apple", "banana", "cherry"]

# Using lambda to reverse the string array
reversed_array = list(map(lambda x: x[::-1], string_array))

print(reversed_array)
