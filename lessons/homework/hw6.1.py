import string

user_input = input("Please, enter 2 letters separated by a hyphen: ")
print(user_input)
first_letter, second_letter = user_input.split("-")

all_letters = string.ascii_letters

first_found_index = string.ascii_letters.find(first_letter)
second_found_index = string.ascii_letters.find(second_letter)
print(first_found_index)
print(second_found_index)

result = all_letters[first_found_index:second_found_index+1]
print(result)



