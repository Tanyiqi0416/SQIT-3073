message = "Hello, DuniA!"

# Print the string
print(message)

# Access individual characters in the string
first_character = message[0]
print("The first character is:", first_character)

# Find the length of the string
length = len(message)
print("The length of the string is:", length)



#
# Get user input for the name
name = input("Enter your name: ")
#
#

# Access individual characters in the string
first_character_name = name[0]
print("The first character is:", first_character_name)

# Find the length of the string
length_name = len(name)
print("The length of the string is:", length_name)


# Concatenate (combine) two strings
greeting = "Hello, " + name + "!"
print(greeting)

# Use string methods
uppercase_message = greeting.upper()
print("Uppercase message:", uppercase_message)

# Check if a substring is in the string
contains_DuniA = "DuniA" in message
print("Does the message contain 'DuniA'? ", contains_DuniA)

# Replace part of the string
new_message = message.replace("DuniA", "World")
print("Updated message:", new_message)