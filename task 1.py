
#q1 A
# for i in range(1,5):
#     print("**********")

#q1 B

# for i in range(1, 6):
#     for j in range(1, 11):
#         if j == 1:
#             print(i, end=" ")
#         else:
#             print(i * j, end=" ")
#     print()

# #q1 C

# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()

# #Q2
# def q2(items):
#     i = 1
#     for item in items:
#         i *= item
#     return i
#
# q2list = [2, 3, 4, 5]
# result = q2(q2list)
# print(result)
#
#
# #Q3

def sn(numbers):

    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest

snlist = [10, 5, 8, 3, 15]
snum = sn(snlist)
print("smallest number: ", snum)

# #q4
#
# def dup(x):
#     return list(set(x))
#
# duplist = [1, 2, 3, 4, 3, 2, 1, 5]
# newlist = dup(duplist)
# print("new list: ", newlist)

#q5
# def clone(lst):
#     return lst[:]
#
#
# original_list = [1, 2, 3, 4, 3, 2, 1, 5]
# new_list = clone(original_list)
# print("new clone list:", new_list)
#

#q6

# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# def remove_elements(lst, indices):
#     return [lst[i] for i in range(len(lst)) if i not in indices]


