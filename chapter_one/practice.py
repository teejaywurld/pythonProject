def square(number):
    return number ** 2


print(square(7))
print(square(3.5))


# def square(number):
#     return number ** 2
#
#
# square(100)
# print("The square of 100 is", square(100))

#
# def maximum(value1, value2, value3):
#     max_value = value1
#     if value2 > max_value:
#         max_value = value2
#     if value3 > max_value:
#         max_value = value3
#         return max_value
#
#
# maximum(36, 56, 45)
# print(maximum)


import random

for i in range(20):
    print('H' if random.randrange(2) == 0 else 'T', end=' ')
