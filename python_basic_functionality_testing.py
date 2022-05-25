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

# a = 12
# b = 'baba'

# print(type(a))
# print(type(a) == int)  # True
# print(a.__class__.__name__)
# print(a.__class__.__name__ == 'int')  # True
# print(a.__class__.__name__ == int)  # False

# a = [1, 2, 3, 4, 5]
# b = a[:]
# c = a[::-1]
# print(b)
# print(c)

# nums_to_hundred = [num for num in range(1, 101)]
# print(nums_to_hundred)

# nums = [1, 2, 3, 4, 5, 6]
# filtered1 = [True if x % 2 == 0 else False for x in nums]
# filtered2 = [1 if x % 3 == 0 else 0 for x in nums]
# print(filtered1)
# print(filtered2)

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# [print(num) for num in [j for j in matrix]]
# [print(*num) for num in [j for j in matrix]]

# flattened = [num for row in matrix for num in row]
# print(flattened)

#  ### Dictionary Comprehensions...
#       -> zip() function to zip the two lists into tuple pairs
#  ### Set Comprehension...


# a = []
# print(sum(a))  # 0

# func(fargs, *args, **kwargs)  # ORDER

# a = {'name': 'zayy', 'last_name': 'baaaayz', 'middle_name': 'haiz'}
# a_a = {'name': 'zayy', 'last_name': 'baaaayz'}
# b = {'name': 'zayy', 'last_name': 'baaaayz', 'middle_name': 'haiz', 'donk': 'donk'}
# c = {1: 'zayy', 'last_name': 'baaaayz', 'middle_name': 'haiz'}


# # print(**a)  # TypeError: 'name' is an invalid keyword argument for print()

# def some_func(last_name=None, middle_name=None, name=None):
#     print(f'{name}, mid: {middle_name}, last: {last_name}')


# some_func(**a)  # zayy, mid: haiz, last: baaaayz
# some_func(**a_a)  # zayy, mid: None, last: baaaayz
# # some_func(**b)  # TypeError: some_func() got an unexpected keyword argument 'donk'
# # some_func(**c)  # TypeError: keywords must be strings

# my_dict = {'Peter': 21, 'George': 18, 'John': 45}
# sorted_dict1 = dict(sorted(my_dict.items(), key=lambda x: x[0]))
# sorted_dict2 = sorted(my_dict.items(), key=lambda x: x[0])  # List of tuples (each with 2 elements)
# print(sorted_dict1)
# print(sorted_dict2)

# coll_3 = sorted([el[1] for el in sorted_dict2])
# print(coll_3)

# print('--------')
# print(sorted_dict1.items())  # dict_items([('George', 18), ('John', 45), ('Peter', 21)])
# print(sorted_dict1.keys())
# print(sorted_dict1.values())

# def factorial(n):
#     if n == 1:  # Base case
#         return 1
#     return n * factorial(n - 1)  # Recursive case


# def recursive_power(x, y):
#     result = 1
#     if y == 0:
#         return result
#     result = x * recursive_power(x, y - 1)
#     return result

# file = open('py.txt', 'w')
# # Creates or open the file

# file.write("This is the write command.\n")
# file.write("This is too!!!")
# file.close()
# file1 = open('py_append.txt', 'a')
# # Creates or open the file

# file1.write("This is the write command.\n")
# file1.write("This is too!!!\n")
# file1.close()

# import os

# file_path = "py.txt"
# if os.path.exists(file_path):
#     os.remove(file_path)
# file_path = "py_append.txt"
# if os.path.exists(file_path):
#     os.remove(file_path)
# file_path = "python.txt"
# if os.path.exists(file_path):
#     os.remove(file_path)
# try:
#     os.remove('ala_bala.txt')
# except FileNotFoundError:
#     print("File already deleted!")


# class MyCustomError(Exception):  # Derived from the Exception class
#     pass


# raise MyCustomError  # Raising MyCustomError


# class Person:
#     def __init__(self):
#         self.first_name = 'Onzi'
#         self.last_name = 'Tamm'
# 
#     def __full_name(self):
#         return f'{self.first_name} {self.last_name}'
# 
#     def info(self):
#         return self.__full_name()
# 
# 
# person = Person()
# print(person.info())  # Onzi Tamm
# # print(person.__full_name())  # AttributeError: 'Person' object has no attribute '__full_name'
# print(person._Person__full_name())  # Onzi Tamm
# print('-------')
# print(person.__dict__)
# print(person.__class__)
# print(person.__class__.__dict__)
# print(Person.__dict__ == person.__class__.__dict__)  # True
# 
# 
# class Person:
#     def __init__(self, name):
#         self.name = name
# 
#     # def __getattr__(self, attr):
#     #     return f'sorry, no "{attr}" attribute found here ;-('
# 
# 
# person = Person('Pete')
# print(getattr(person, 'name'))  # Pete
# 
# ## before def __getattr__ is defined
# print(getattr(person, 'age'))  # AttributeError: 'Person' object has no attribute 'age'
# print(getattr(person, 'age', 'None'))  # None
# 
# ## after def __getattr__ is defined
# print(getattr(person, 'age'))  # 'sorry, no "age" attribute found here ;-('
# print(getattr(person, 'age', 'None'))  # 'sorry, no "age" attribute found here ;-('
# 
# print(hasattr(person, 'name'))  # True
# print(hasattr(person, 'age'))  # False
# ## after def __getattr__ is defined
# print(hasattr(person, 'name'))  # True
# print(hasattr(person, 'age'))  # True
# 
# person = Person('Pete')
# print(person.name)  # Pete
# 
# print(setattr(person, 'name', 'George'))  # None
# print(person.name)  # George
# print(setattr(person, 'age', 21))  # None
# print(person.age)  # 21
# 
# class Phone:
#     def __setattr__(self, attr, value):
#         self.__dict__[attr] = value.upper()
# 
# 
# phone = Phone()
# phone.color = 'black'
# print(phone.color)  # BLACK
# 
# class Person:
#     def __init__(self, name):
#         self.name = name
# 
# 
# person = Person('Pete')
# print(person.name)  # Pete
# print(delattr(person, 'name'))  # None
# # print(person.name)  # AttributeError: 'Person' object has no attribute 'name'
# 
# class Phone:
#     def __delattr__(self, attr):
#         del self.__dict__[attr]
#         print(f"'{str(attr)}' was deleted")
# 
# 
# phone = Phone()
# phone.color = 'black'
# del phone.color  # 'color' was deleted
# 
# class Purchase:
#     def __init__(self, product_name, cost):
#         self.product_name = product_name
#         self.cost = cost
# 
#     def __add__(self, other):
#         name = f'{self.product_name}, {other.product_name}'
#         cost = self.cost + other.cost
#         return Purchase(name, cost)
# 
#     def __str__(self):
#         return f'{self.product_name}, {self.cost}'
# 
# 
# first_purchase = Purchase('sofa', 650)
# second_purchase = Purchase('table', 150)
# print(first_purchase + second_purchase)  # sofa, table, 800
# 
# class Person:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
# 
#     def __gt__(self, other):
#         return self.salary > other.salary
# 
# 
# person_one = Person('John', 20)
# person_two = Person('Natasha', 36)
# print(person_one > person_two)  # False
# 

ll = [1, 2, 3, 4, 5, 6]


# print(ll.__next__())  # AttributeError: 'list' object has no attribute '__next__'
# print(next(ll))  # TypeError: 'list' object is not an iterator

my_iter = iter(ll)
my_iter2 = ll.__iter__()
print(my_iter == my_iter2)  # False
print(my_iter.__iter__())  # <list_iterator object at 0x00000254364F6140>
print('------')
print(my_iter.__next__())  # 1
print(next(my_iter2))  # 1

# list  # just checking builtins.py signature

iterable = 1, 2, 3, 4, 5, 6
print(iterable)  # (1, 2, 3, 4, 5, 6)
print(type(iterable))  # <class 'tuple'>

iter_obj = iter(iterable)
while True:
    try:
        element = next(iter_obj)  # get the next item
        # do something with element
        print(element)
    except StopIteration:
        # if StopIteration is raised, break from loop
        break


class custom_range:
    def __init__(self, start, end):
        self.i = start
        self.n = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.i <= self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()


one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)

# 1... 10

def first_n(n):
    num = 0
    while num < n:
        yield num
        num += 1


sum_first_n = sum(first_n(5))
print(sum_first_n)

# Initialize the list
my_list = [1, 3, 6, 10]

# square each term using list comprehension
print([x ** 2 for x in my_list])  # Output: [1, 9, 36, 100]

# same thing can be done using generator expression
print((x ** 2 for x in my_list))  # Output: <generator object <genexpr> at 0x0000024CF0C95C40>

print(sum([x ** 2 for x in my_list]))  # 146
print(sum((x ** 2 for x in my_list)))  # 146
print(sum([x ** 2 for x in my_list]) == sum((x ** 2 for x in my_list)))  # True

def squares(n):
    i = 1
    while i <= n:
        yield i * i
        i += 1


print(list(squares(5)))  # [1, 4, 9, 16, 25]


def genrange(start, end):
    i = start
    n = end
    while i <= n:
        yield i
        i += 1


print(list(genrange(1, 10)))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
