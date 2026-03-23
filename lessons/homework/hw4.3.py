import random
NUMS_SIZE = 10
list1 = []
for i in range(NUMS_SIZE):
    list1.append(random.randint(3, 10))

print(list1)
list2 = []
list2.append(list1[0])
list2.append(list1[2])
list2.append(list1[-2])
print(list2)





