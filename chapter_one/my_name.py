# name = "Adetunji Henry"
# print(name)
import math

#
# def factorial(number):
#     factorial = 1
#     for i in range(1, number):
#         factorial *= i
#     return factorial


# print(factorial(6))


# def addition(number1, number2):
#     total = number1 + number2
#     return total
#
# print(addition(7,8))


# def square_root(number):
#     total = math.sqrt(number)
#     return total
#
#
# print(math.sqrt(120))
#
#
# def multiplication(number1, number2):
#     total = number1 * number2
#     return total
#
#
# print(multiplication(8, 9))


def reverse(number):
    reverse_number = 0
    while number != 0:
        digit = number % 10

        reverse_number = reverse_number * 10 + digit

        number = number // 10

    return reverse_number


# reverse(256)
# print(reverse(256))

#
# def free_flow(a_string='', an_int=0, a_float=None, a_list=[], a_dict={}): # everything in the bracket has been set to false
#     if a_string:
#         print(a_string)
#     else:
#         print("Nothing was entered!")
#
#
# # free_flow("John Smith")
# free_flow("goat", 1.0, "hen")


