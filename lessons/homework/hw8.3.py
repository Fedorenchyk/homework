def find_unique_value(some_list):
    unique_numbers = []
    for number in some_list:
        if some_list.count(number) == 1:
            unique_numbers.append(number)
    unique_numbers = float("".join(map(str, unique_numbers)))
    return unique_numbers

assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")

