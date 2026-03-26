import string

user_input = input("Please enter text to convert to hashtag: ")
user_input = user_input.title()
user_input = user_input.replace(" ", "")

for symbol in string.punctuation:
    user_input = user_input.replace(symbol, "")

user_input = "#" + user_input

user_input = user_input[:140]

print(user_input)
