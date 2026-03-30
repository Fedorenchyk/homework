def difference(*numbers):
    if len(numbers) == 0:
        return 0
    min_number = float(min(*numbers))
    max_number = float(max(*numbers))
    result = max_number - min_number

    if result % 1 == 0:
        return result
    else:
        result = round(result, 2)
        return round(result, 2)


assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')
