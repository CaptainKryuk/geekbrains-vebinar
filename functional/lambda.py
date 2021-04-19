
# * function
# def testfunc(num):
#     return lambda x : x * num

# result1 = testfunc(10)
# result2 = testfunc(1000)

# print(result1(9))
# print(result2(9))

# * map filter
# numbers_list = [2, 6, 8, 10, 11, 4, 12, 7, 13, 17, 0, 3, 21]

# filtered_list = list(filter(lambda num: (num > 7), numbers_list))

# print(filtered_list)

# numbers_list = [2, 6, 8, 10, 11, 4, 12, 7, 13, 17, 0, 3, 21]

# mapped_list = list(map(lambda num: num % 2, numbers_list))

# print(mapped_list)


# * custom
# def function_builder(func, num_list):
#   new_list = []
#   for num in num_list:
#     new_list.append(func(num))
#   return new_list


# print(function_builder(lambda n: n / 10, [1,2,3,4,5,6,7,8,9]))