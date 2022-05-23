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
