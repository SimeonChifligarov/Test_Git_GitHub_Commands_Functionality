# print('hit me 1 more time')

# a = 15_000
# print(type(a))
# print(type(type(a)))
# print(type(type(type(a))))  # '<class 'type'>'
# print('-----------')
# print(a.__class__.__name__)

# print('hello')
# input()
# print('do_nothing ;)')

# print((int(input())) ** 2)

# print(15 / 0) # ZeroDivisionError: division by zero

# ## keywords (33)
# True False None
# if elif else
# and or not
# pass
# while for break continue
# in is
# def class
# lambda
# import from as
# return yield
# with
# try except finally
# raise
# assert del
# global nonlocal

# print('some text')
# import time
# from datetime import datetime

# a = datetime.now()
# # print(a)
# time.sleep(3)
# b = datetime.now()
# # print(a - b) # -1 day, 23:59:56.984776
# print(b - a)
# print(a > b)
# print(b > a)

# a = 5
# print('yess') if a > 0 else print('nooo')
# print('yess') if a > 10 else print('nooo')

# a = [1, 2, 3, 4, 5, 11, 12, 13]
# b = []

# print(max(a))
# # print(max(b)) # ValueError: max() arg is an empty sequence

# a = 'Peshkata'
# print(a[2])
# # a[2] = 'D' # TypeError: 'str' object does not support item assignment
# print(a)

# print(0.1 + 0.2)  # 0.30000000000000004
# print(int(0.001337))
# print(int(0.5))
# print(int(0.9))


# digits = 1337
# sum_of_digits = 0
# while digits > 0:
#     sum_of_digits += digits % 10
#     digits = int(digits / 10)
# print(sum_of_digits)

# a = []
# b = [1, 2, 3, 4]

# print(a)
# print(bool(a))
# print('------')
# print(b)
# print(bool(b))

# if a:  # NameError: name 'a' is not defined
#     print('bob')

# a = ()
# b = tuple([])
# c = (1)  # Remove redundant parenthesis
# d = (1,)
# print(a)
# print(b)
# print(c)
# print(d)
# print('----')
# print(type(a))
# print(type(c))

# a = [1, 2, 3, 4, 5, 6, 7]
# print(a[len(a) - 1])
# print(a[-1])
# print(a[-7])
# # print(a[-8])  # IndexError: list index out of range

# a = ['a', 'b', 'c', 'd']

# for pos, val in enumerate(a):
#     print(pos)
#     print(val)
#     print('---')

# def some_func_a():
#     a = 5


# def some_func_b():
#     return


# print(some_func_a())
# print(some_func_b())
# print('----')
# print(print('----'))

# print(type(some_func_b))
# print(some_func_b.__class__.mro())

# def a():
#     pass


# print(a())

# def increase_a_by_one(x):
#     x += 1
#     return x


# a = 10
# print(a)
# print(increase_a_by_one(a))
# print(a)

# def check_func_body():
#     print('pre')
#     raise SyntaxError
#     print('post')


# #
# #
# # # print('here 1')
# # # check_func_body()
# # # print('here 2')
# #
# # check_func_body()
# # print('here 3')

# print('no function invocation')  # exit code 0

# print(range(10))
# print(type(range(5)))

# a = '1azobi4amma4iboza2'
# print(''.join((reversed(a))))
# b = list(a)
# b.reverse()
# print(''.join(b))
# print(a[::-1])

# a = [1, 2, 3, 4, 5, 6, 11, 2, 1]
# print(sorted(a))
# print(sorted(a, key=lambda el: -el))


# def sorting_func(element):
#     return -element


# print('---------')
# print(sorted(a, key=sorting_func))

# a = [1, 2, 3, 'abc', 'def', 4, 2, 1, 'a', 'abb']
# print(sorted(a))  # TypeError: '<' not supported between instances of 'str' and 'int'
# 
# 
# a = {'1a': 1, '2ab': 2, '3abc': 3, '1a': 0}  # Dictionary contains duplicate keys '1a'
# print(a)
# print([el for el in enumerate(a)])
# a['1a'] = 11
# print(a)
# print([el for el in enumerate(a)])

# b = dict(many='true', yes='da', **a)
# print(b)
# c = dict(no='ne', **a, be='non-be')
# print(c)
# print(c.keys())  # dict_keys
# print(c.values())  # dict_values
# print(c.items())  # dict_items
# print(list(c.keys()))

# x = {1: 'one', 2: 'two', 3: 'three'}
# y = {1: 'one', 2: 'two', 3: 'three'}
# z = {2: 'two', 3: 'three', 1: 'one'}
# print(x == y)  # True
# print(y == z)  # True
# print(x == y == z)  # True
# print(id(x) == id(y))  # False
# z1 = z.copy()
# print(z1 == z)  # True
# z1[1337] = 'more_value'
# print(z1 == z)  # False
# print(z1)

# print('---------')
# a1 = {'b', 'd', 'a', 13, 37}

# print(a1)
# print([el for el in enumerate(a1)])
# a1.add('lamqta')
# print(a1)
# print([el for el in enumerate(a1)])

# y = {1: 'one', 2: 'two', 3: 'three'}
# z = {2: 'two', 3: 'three', 1: 'one'}
# print(y == z)  # True
# print(y.popitem())
# print(z.popitem())
# print(y == z)  # False

# employees = {1: {'name': 'Pete', 'age': 22},
#              2: {'name': 'Alex', 'age': 21}}

# employees[3] = {}  # {3: {}}
# employees[3]['name'] = 'Anna'  # {3: {'name': 'Anna'}}
# employees[3]['age'] = 25  # {3: {'name': 'Anna', 'age': 25}}

# print(employees)
# employees[4] = dict(name='Monster', age=88)
# print(employees)

# a = "a   d e  1 2"
# b = a.split()
# print(b)
# c = a.split(maxsplit=2)
# print(c)  # ['a', 'd', 'e  1 2']
# print(a[::-1])

# some_string = 'My name is Zimeon'
# print(some_string[-6:])
# # print(len(some_string))

# print('12123'.isdigit())  # True
# print('121212q33'.isdigit())  # False
# print('1'.isupper())  # False
# print('1'.islower())  # False
# print('ABC2'.isupper())  # True
# print('ABCc'.isupper())  # False

# text = input()
# open_parentheses = []

# for i in range(len(text)):
#     if text[i] == "(":
#         open_parentheses.append(i)
#     elif text[i] == ")":
#         start_index = open_parentheses.pop()
#         print(text[start_index:i + 1])

# from collections import deque
# queue = deque(["Pesho", "Gosho", "Tosho"])  # append, popleft; double-ended que => appendleft, pop

# a = [1, 2]
# b = (3, 4)
# c, d = a
# e, f = b
# # k, l, m = b  # ValueError: not enough values to unpack (expected 3, got 2)

# print(c, d)
# print(e)
# print(f)

# a = []
# b = 4
# c = (a, b)
# print(c)

# a.append(4)
# a.append(41)
# a.append(24)
# a.append(444)
# print(c)
# a.append(a)
# print(c)
# print(a[-1])
# print(a)
# print(a[-1] == a)  # True

# a = 1,
# print(a)
# print(type(a))  # <class 'tuple'>
# print(a[0])
# # a[0] = 2  # TypeError: 'tuple' object does not support item assignment

# a = {1}
# print(type(a))
# a.pop()
# print(a)
# # a.pop()  # KeyError: 'pop from an empty set'

# matrix = [[0 for _ in range(2)] for _ in range(3)]
# print(matrix)

# matrix1 = [[j for j in range(1, 4)] for i in range(3)]
# matrix2 = [[j + i * 3 for j in range(1, 4)] for i in range(3)]
# print(matrix1)
# print(matrix2)

# matrix = [[1, 2, 3], [4, 5, 6]]
# flattened1 = [num for sublist in matrix for num in sublist]
# flattened2 = [num * 3 for sublist in matrix for num in sublist]

# print(flattened1)
# print(flattened2)

# from pprint import pprint

# rows_count = 10
# # matrix = [map(int, ['1', '13', '133', '1337']) for _ in range(rows_count)]
# matrix = [list(map(int, ['1', '13', '133', '1337'])) for _ in range(rows_count)]

# pprint(matrix)

# flattened = [num for row in matrix for num in row]
# print(flattened)

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         print(matrix[i][j], end=" ")
#     print()

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print([j for j in matrix] == matrix)  # True
