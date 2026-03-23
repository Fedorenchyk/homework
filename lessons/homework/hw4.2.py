numbers = [0, 1, 7, 2, 4, 8]
sum = 0
for i in range(0, len(numbers), 2):
    sum += (numbers[i])

if len(numbers) != 0 :
    print(sum * (numbers[- 1]))

else:
    print(0)

