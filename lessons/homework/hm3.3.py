nums = [1,2,3,4,5,6]
middle_index = len(nums) // 2
if len(nums) % 2 != 0:
    middle_index += 1
list1 = nums[:middle_index]
list2 = nums[middle_index:]
print(list1)
print(list2)
result = [list1, list2]
print(result)

