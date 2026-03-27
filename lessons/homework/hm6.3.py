user_input = int(input("Enter a number: "))

multiplication_result=10

while multiplication_result > 9:
    user_input = str(user_input)
    multiplication_result = 1
    for char in user_input:
        if char.isdigit():
            multiplication_result *= int(char)
    print(multiplication_result)
    user_input = multiplication_result