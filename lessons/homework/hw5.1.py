import keyword
import string


test_data =  ["_", "__" ,"___", "x", "get_value", "get value", "get!value",
             "some_super_puper_value", "Get_value", "get_Value", "get_Value",
             "getValue", "3m", "m3", "assert", "assert_exception","import"]


for test_variable_name in test_data:
    result = "Correct naming convention for potential variable: "
    if test_variable_name in keyword.kwlist:
        print(f"Incorrect naming convention for potential variable: {test_variable_name}")
        continue

    if test_variable_name.islower() or test_variable_name == "_":
        pass
    else:
        print(f"Incorrect naming convention for potential variable: {test_variable_name}")
        continue

    if test_variable_name[0].isdigit():
        print(f"Incorrect naming convention for potential variable: {test_variable_name}")
        continue

    if test_variable_name.count("_") > 1:
        print(f"Incorrect naming convention for potential variable: {test_variable_name}")
        continue

    for symbol in test_variable_name:
        if symbol in string.punctuation and symbol != "_":
            result = "Incorrect naming convention for potential variable:"
            break

        if symbol == " ":
            result = "Incorrect naming convention for potential variable:"
            break

    print(result, test_variable_name)