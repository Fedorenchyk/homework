#task 3.1
print ("It's simple calculator. Please follow instructions")
first_number = int(input("Enter a number: "))
symbol = input("Enter a symbol(+, -, *, /): ")
second_number = int(input("Enter another number: "))

match symbol:
    case "+":
        print("Result:", first_number+second_number)
    case "-":
        print("Result:", first_number-second_number)
    case "*":
        print("Result:", first_number*second_number)
    case "/":
        if second_number!=0:
            print("Result:", first_number/second_number)
        else:
            print("You can't divide by 0")

    case _:
        print("Invalid symbol")








