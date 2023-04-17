list1 = [12, -7, 5, 64, -14]
for num in list1:
    if num >= 0:
        print(num, end=", ")
list2 = [12, 14, -95, 3]
positive_nums = [num for num in list2 if num >= 0]
print(positive_nums)


Output: 12, 5, 64 for list 1
Output: [12, 14, 3] for list 2

