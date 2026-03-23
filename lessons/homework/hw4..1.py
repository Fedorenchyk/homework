numbers = [0, 1, 0, 12, 3]

for value in numbers:
    if value == 0:
        numbers.append(value)
        numbers.remove(value)


for value in numbers:
    print(value)