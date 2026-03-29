def common_elements():
    list1 = list(range(0, 100, 3))
    list2 = list(range(0, 100, 5))
    set1 = set(list1)
    set2 = set(list2)
    return set1&set2

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print('ok')


