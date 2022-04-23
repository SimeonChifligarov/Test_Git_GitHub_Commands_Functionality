# def heavy_calculation(*args):
#     return sum(*args)
#
#
# def calculate(*args, memo={}):
#     arguments = args
#     try:
#         value = memo[arguments]  # return already calculated value
#     except KeyError:
#         value = heavy_calculation(arguments)
#         memo[arguments] = value  # update the memo dictionary
#     return value
#
#
# print(calculate(3, 4, 5))
# print(calculate(3, 2))
# print(calculate(3, 3, 5))
# print(calculate(3, 4, 5))
# print(calculate(3, 2))
#
#
# def heavy_calculation(*args):
#     arguments = list(*args)
#     result = 0
#     for arg in arguments:
#         result += arg
#     return result
#
#
# def calculate(*args, memo={}):
#     arguments = tuple(args)
#     try:
#         value = memo[arguments]  # return already calculated value
#     except KeyError:
#         value = heavy_calculation(arguments)
#         memo[arguments] = value  # update the memo dictionary
#     return value
#
#
# print(calculate(3, 4, 5))
# print(calculate(3, 2))
# print(calculate(3, 3, 5))
# print(calculate(3, 4, 5))
# print(calculate(3, 2))
#
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# my_dict2 = my_dict.copy()
# my_dict3 = {'a': 1, 'b': 2, 'c': 3}
# my_dict4 = {'b': 1, 'a': 2, 'c': 3}
# my_dict5 = my_dict
#
# print(my_dict == my_dict3)
# print(my_dict == my_dict4)
# print(my_dict == my_dict2)
# print(my_dict == my_dict5)
#
# my_dict2['d'] = 4
# print(my_dict)
# print(my_dict2)
# print(my_dict == my_dict2)
#
# my_list = [1, 2, 3, 4, 5]
# my_list2 = [1, 2, 3, 4, 5]
# my_list3 = my_list.copy()
#
# print(my_list == my_list2 == my_list3)
# # print(my_list == my_list3)
# # print(my_list3 == my_list2)
# my_list2.append(100)
# print(my_list == my_list2)
# print(my_list == my_list3)
#
# my_list = [1, 2, 3, 4, 5]
# my_list2 = [1, 2, 3, 4, 5]
# my_list3 = my_list.copy()
# my_list4 = my_list
#
# print(my_list == my_list2)
# print(id(my_list) == id(my_list2))
# print(id(my_list) == id(my_list3))
# print(id(my_list) == id(my_list4))
#
# a = []
# # a.pop()  # IndexError: pop from empty list
# a = {'a': 1, 'b': 2, 'c': 3}
# b = a.popitem()
# print(b)
# print(a)
#
# a = (1, 250, 3, 43, 2, 11)
# print(sorted(a))
# print(a)
# # a.sort() # AttributeError: 'tuple' object has no attribute 'sort'
# print(a)
#
# a = ['ab', 'bbbbbbbb', 'Az', 'az', '11', 'Ca']
# print(sorted(a))
# print(a)
# a.sort()
# print(a)
#
#
# def sort_me_baby(el1):
#     return el1[0]
#
#
# a = {'a': 22, 'd': 14, 'b': 33}
# b = sorted(a.items(), key=lambda x: x[0])
# print(b)
# c = dict(b)
# print(c)
# d = sorted(a.items(), key=sort_me_baby)
# print(dict(d))
# print(*a.items(), sep=', ')
#
# b = ('a', 22)
# print(*b)
#
# a = 'with     5spaces baby'
# print(a.split(' ', maxsplit=1))
# print(a.split(' ', maxsplit=2))
# print(a.split(' ', maxsplit=3))
# print(a.split(' ', maxsplit=4))
# print(a.split(' ', maxsplit=5))
# print(a.split(' ', maxsplit=6))
# print(a.split(' ', maxsplit=7))
# print(a.split(' ', maxsplit=8))
# print(a.split(' '))
# print(' '.join(a.split(' ')))
#
# a = '   '
# print(a.split(' '))
#
# a = 'abcdef'
# print(''.join(list(reversed(a))))
#
# print('b1'.isalpha())
#
# a = ['baba', 'asdasdasd', 'kick', 'da', 'manastirski livadi']
# b = (len(el) for el in a)
# print(b)
#
# a = [1, 2, 3, 4, 5, 6]
# # changed = [True if num % 2 == 0 else 'baba' for num in a]
# changed = [11 if num % 2 == 0 else 'baba' for num in a]
#
# print(changed)
#
# a = [1, 2, 3, 4]
# b = [1, [2, 3, 4], [5, 6]]
# a.extend(b)
# print(a)
# print(b)
# a.insert(0, 100)
# print(a)
#
# a = {'baba': 3, 'dqdo': 11, 'kote': 33, 'kuchence': 0}
# b = sorted(a.items(), key=lambda el: el[1])
# c = [el[0] for el in b]
# print(b)
# print(c)
#
# d = list(a.keys())
# e = list(a.values())
# print(d)
# print(sorted(e))
# print(e)
#
# a = [1, 2, 3, 4, 5, 6]
# # b = list(reversed(a))
# b = reversed(a)
# c = a[::-1]
# print(a)
# # print(b)
# # print(list(b))
# print(c)
#
# a.reverse()
# print(a)
# # print(b)
# print(list(b))
# print(c)
#
# a = [1, 2, 3, 4, 5, 6]
# b = map(lambda el: str(el) + ' boza', a)
# print(b)
# print(list(b))
#
# a = ['a', 'b', 'baba', 'dqdo']
# a[0], a[1], a[3] = a[2], a[3], a[0]
# print(a)
#
# import re
#
# a = 'some fucking good text11233'
# b = list(a)
# # print(re.split(r'', a)[1:-1])
# # print(re.findall(r'.', a))
#
# c = ''.join(b)
# print(c)
# print(''.join(b))
#
# from collections import deque
#
# a = [1, 2, 3, 4, 5, 6]
# b = deque([str(el) for el in a])
# print(b)
# print(type(b))
# # print('-------------')
# # print('\n'.join(b))
# print(b[2] + b[3])
#
# a = (['a', 'b', 'c'], [1, 2, 3], [4, 5, 6],)
# b = [1, ]
# c = []
#
# # a[1].append(4)
# a[1].clear()
# print(a)
# print(b)
# print(c)
# print(len(a))
#
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6, 7, 8, 9}
# print(a.union(b) == b.union(a))
# from pprint import pprint
#
# a = []
# for i in range(5):
#     a.append([j + 1 for j in range(5)])
#
# # pprint(a)
#
# b = [1, 2, 3, 4]
# [print(row) for row in [el for el in a]]
#
# a = 'basi qkoto maina11'
# b = [ch for ch in a]
# print(b)
# c = list(a)
# print(c)
# print('----------')
# print(b == a)
# print(c == list(a))
# d = list(a)
# print(c == d)
# d.pop()
# print(d)
# print(c)
# print(c == d)
#
# a = 'bate agoshooo'
# b = set(a)
# print(b)
#
# a = range(5)
# a = (i for i in range(5))
# print(a)
#
# for i in a:
#     print(i)
# for i in a:
#     print(i)
# for i in a:
#     print(i)
#
# print(type(a))
# print(a)
#
# a = {1}
# print(type(a))
# a.add(5)
# print(a)
#
#
# def is_vowel(char):
#     return char in ['a', 'o', 'e']
#
#
# print(is_vowel('o'))
# print(is_vowel('x'))
#
# a = [1, 2, 3, 4, 5]
# b = []
# print(len(a) > 0)
# print(len(b) > 0)
#
# print(bool(a))
# print(bool(b))
#
# a = [0, 0, 1]
# print(any(a))
#
# print(True in a)
#
#
# def some_func(*args, **kwargs):
#     print(type(args))
#     print(args)
#     print(*args)
#     print('-----------')
#     print(type(kwargs))
#     print(kwargs)
#     # print(**kwargs)
#     real_dict = kwargs
#     print(real_dict)
#
#
# some_func(1, 2, 3, 4, 5, boss='mass', mad='duddddeeee')
#
#
# def my111_func(**kwargs):
#     print(kwargs)
#
#
# a = {'azd': 1, 'bab': 4, 'karl': 9, 'linch': 16}
# # print(**a)
# my111_func(**a)
#
#
# def my22_func(name, age):
#     return f'My name is {name}, and my age is {age}'
#
#
# a = {'name': 'Gosho', 'age': 15}
# b = {'name': 'Gosho', 'age': 15, 'mass': 'azzzz'}
#
# print(my22_func(**a))
#
#
# # print(my22_func(**b))
#
# def a(n):
#     if n == 0:
#         return
#     print(n)
#     a(n - 1)
#
#
# a(5)
#
# import sys
#
# print(sys.version)
#
# my_arr = ['kuche', 'baba', 'kotka', 'kotka', 'baba', 'dqdo', 'kuche', 'kotka']
# my_dict = {word: my_arr.count(word) for word in my_arr}
# print(my_dict)
#
# dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
#
# # Identify odd and even entries
# res = {k: ('Even' if v % 2 == 0 else 'Odd') for (k, v) in dict1.items()}
#
# print(res)
#
# my_arr0 = ['kuche', 'kotka']
# my_arr = ['kuche', 'baba', 'kotka', 'kotka', 'baba', 'dqdo', 'kuche', 'kotka']
# my_dict0 = {word: my_arr.count(word) for word in my_arr0}
# print(my_dict0)
#
# from math import trunc
#
#
# def trunc(x):
#     return 'hello baby'
#
#
# from math import trunc
#
# print(trunc(4.5))
# # print(trunc)
#
# # help(trunc)
# import time
#
# # msg = input('what do ??? : ')
# # time.sleep(3)
# # print(msg)
#
# a = 5
#
# # def azz():
# #     azz2()
# #     azz3()
# #     azz4()
# #
# #
# # def azz2():
# #     print('azzz2')
# #
# #
# # def azz3():
# #     print('azzz3')
# #
# #
# # azz()
# #
# # real_input = input()
#
# # a, b = [int(el) for el in real_input[1:-1].split(', ')]
# # c, d = eval(real_input)
# # print(a)
# # print(b)
# # print(c)
# # print(d)
# # print(a == c)
# # print(b == d)
#
# a = ' '
#
# print('bbbb' if a else 'ccccc')
#
# a = {1, 2, 3, 1, 1, 1, 2, 2, 3}
# print(len(a))
# print(a.__len__)
#
# a = [0, 'kote', 13]
# b = a[-1] if a else None
# print(b)
#
#
# # while True:
# #     try:
# #         number = int(input('Please, enter a number: '))
# #         break
# #     except ValueError:
# #         print('Oops... Try again, try better... ')
#
#
# # try:
# #     print 'Hello' #SyntaxError
# # except SyntaxError:
# #     print('stx err')
#
# def is_in_range(col, row, n=8):
#     return 0 <= col < n and 0 <= row < n
#
#
# print(is_in_range(3, 2))
# print(is_in_range(8, 2))
# print(is_in_range(11, 2))
# print(is_in_range(-3, 2))
# print(is_in_range(4, 3, 6))
# print(is_in_range(3, 2, 2))
# print(is_in_range(-3, 2, 12))
# print(is_in_range(10, 10, 12))
#
# a = [1, 2, 3, 4, 5]
#
# for i in range(5):
#     b = a[0]
#     print(b)
#     # print(a[1]) #IndexError
#
#     a = a[1:]
#     print(a)
#     print('---------')
#
# a = None or []
# print(a)
#
# a = {'baby': 'ines', 'b_fam': 'ivanova', 'cac': 'aca'}
# print(a['baby'])
#
#
# class AreWe:
#     text_a = 'helllooo'
#
#     def some_func_a(self):
#         return 42
#
#
# b = AreWe()
# print(b.some_func_a())
# print(b.some_func_a)
# print(b.text_a)
#
# a = []
# print(not any(a))
# print(len(a) == 0)
# a.append(3)
# a.append(33)
# print(not any(a))
# print(len(a) == 0)
#
#
# class A:
#     def __init__(self, name, age):
#         self.name = name
#         self.set_age(age)
#         self.__age = self.get_age()
#
#     def set_age(self, age):
#         self.__age = age
#
#     def get_age(self):
#         return self.__age
#
#
# a = A('tosho', 44)
# print(a.get_age())
#
#
# class A:
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return f'I am {self.name}'
#
#
# a1 = A('pesho')
# a2 = A('tosho')
# a3 = A('gosho')
# a4 = A('bosho')
#
# list_a = [a1, a2, a3, a4]
# print([str(el) for el in list_a])
#
# del a3
# print([str(el) for el in list_a])
#
# list_b = [el for el in list_a if not el.name == 'gosho']
# print([str(el) for el in list_b])
#
# print([str(el) for el in list_a])
# list_a.remove(a2)
# print([str(el) for el in list_a])
#
#
# class A:
#     pass
#
#
# class B(A):
#     pass
#
#
# class C(B):
#     pass
#
#
# class D(A):
#     pass
#
#
# a = A()
# b = B()
# c = C()
# d = D()
#
# print(isinstance(a, A))
# print(isinstance(a, B))
# print('---------')
# print(isinstance(b, A))
# print(isinstance(b, B))
# print('---------')
# print(isinstance(c, A))
# print(isinstance(c, B))
# print(isinstance(c, C))
# print('---------')
# print(c.__class__.__name__ == A.__name__)
# print(c.__class__.__name__ == B.__name__)
# print(c.__class__.__name__ == C.__name__)
# print('---------')
# print(isinstance(c, object))
#
# a = [1, 2, 3, 4, 5, 6]
# iter_a = iter(a)
# print(iter_a)
#
# while True:
#     try:
#         element = next(iter_a)
#         print(element)
#         # print(iter_a)
#     except StopIteration:
#         break
#
# print(iter_a)
#
# iter_b = iter(a)
#
# print(iter_b)
#
#
# class custom_range:
#     # def custom_range(start, end):
#     # return range(start, end + 1)
#
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#         self.current = self.start
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         # if self.current <= self.end:
#         #     real_current = self.current
#         #     self.current += 1
#         #     return real_current
#         # else:
#         #     self.current = self.start
#         #     raise StopIteration
#         if self.end < self.current:
#             self.current = self.start
#             raise StopIteration
#
#         self.current += 1
#         return self.current - 1
#
#
# one_to_ten = custom_range(1, 5)
# for num in one_to_ten:
#     print(num)
#
# for num in one_to_ten:
#     print(num)
#
#
# def next_nums(n):
#     num = 0
#     while num < n:
#         yield num
#         num += 1
#
#
# a = next_nums(5)
#
# for el in a:
#     print(el)
# print('-----')
# for el in a:
#     print(el)
#
#
# def some_func(goss, *args, **kwargs):
#     print(goss)
#     # print(kwargs['goss'])
#     print(args)
#     print(kwargs)
#     return 'done'
#
#
# a = some_func(boss='toss', goss='ross', pros='pros')
# print(a)
#
# from time import time
#
#
# def time_measure(func):
#     def wrapper(*args, **kwargs):
#         start = time()
#         result = func(*args, **kwargs)
#         end = time()
#         time_needed = end - start
#         print(time_needed)
#         return result
#
#     return wrapper
#
#
# @time_measure
# def calculate_sum_of_one_to_hundred():
#     my_list = [num for num in range(1_000_000)]
#     result = sum(my_list)
#     return result
#
#
# print(calculate_sum_of_one_to_hundred())
#
#
# def repeat(n):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(n):
#                 func(*args, **kwargs)
#
#         return wrapper
#
#     return decorator
#
#
# @repeat(5)
# def say_hi():
#     print("hello there")
#
#
# say_hi()
#
#
# class Fibonacci:
#     def __init__(self):
#         self.cache = {0: 0, 1: 1}
#
#     def __call__(self, n):
#         # if n not in self.cache:
#         #     if n == 0 or n == 1:
#         #         self.cache[n] = n
#         #     else:
#         #         self.cache[n] = self(n - 1) + self(n - 2)
#         #
#         # return self.cache[n]
#
#         if n not in self.cache:
#             for i in range(2, n + 1):
#                 if i not in self.cache:
#                     self.cache[i] = self.cache[i - 1] + self.cache[i - 2]
#
#         return self.cache[n]
#
#
# fib = Fibonacci()
#
# # for i in range(6):
# #     print(fib(i))
#
# print(fib(8))
# print(fib(6))
# print(fib.cache)
#

class func_logger:
    _logfile = 'out.log'

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        log_string = self.func.__name__ + ' was called'
        with open(self._logfile, 'a') as opened_file:
            opened_file.write(log_string + '\n')
        return self.func(*args, **kwargs)


@func_logger
def say_hi(name):
    print(f'Hi, {name}!')


say_hi('Peter')


def some_func(*args, **kwargs):
    print(args)
    print(*args)
    print('----')
    print(kwargs)
    # print(**kwargs)
    print('; '.join([f'key: {key}, value: {value}' for key, value in kwargs.items()]))


# some_func(1, 3, 4, 5, b=10, d=15)
some_func(1, 3, 4, 5, **{'b': 10, 'd': 15})

a = [1, 2, 3, 3, 4, 5, 3, 2, 100, 1000]
print(a)

del a[len(a) - 2]
print(a)

b = {'baba': 'lada', 'kaka': 'lambo', 'lele': 'male'}
print(b)

del b['kaka']
print(b)

a = [1, 2, 'baba']
if a == [1, 2, 'baba']:
    print('yeah')
else:
    print('naah')


class A:
    def __init__(self):
        self.__d = None
        self.a = 1
        self.b = 2
        self.c = 'baba'

    @property
    def d(self):
        return self.__d

    @d.setter
    def d(self, value):
        self.__d = value

    def some_a(self):
        return self

    def some_b(self):
        return self

    def some_c(self):
        return self

    @staticmethod
    def some_d():
        return

    @classmethod
    def some_e(cls):
        return cls


print(A.mro())

a = A()
print(a.__class__.mro())
print(a.__dict__)
print(dir(A))
print(dir(a))
a.d = 5
print(a.__dict__)
print(dir(a))
print([el for el in dir(a) if not el.startswith('__')])
print([el for el in dir(a) if not (el.startswith('__') or callable(getattr(a, el)))])
print([el for el in dir(a) if (not el.startswith('__') and callable(getattr(a, el)))])
# print([el for el in [el for el in dir(a) if (not el.startswith('__'))] if not callable(getattr(a, el))])

print(id(a), a)
print(id(A), A)


def func_a():
    return func_a


b = func_a()
print(b.__dir__)
print(b.__class__)
print(b.__class__.mro())


def func_b():
    return


print(func_b.__class__.mro())

a = [1, 2, 3, 4]
a.insert(100, 55)
print(a)
a.insert(-2, 44)
print(a)
a.insert(-200, 33)
print(a)

a = [1, 2, 3, 4]
b = [1, 2, 3]
b.append(4)
c = [2, 3, 4, 1]
d = a

print(a == b)
print(a == c)
print(a == d)

print('--------')
print(id(a) == id(b))
print(id(a) == id(d))

a = 'some text 11'
print(len(a))


class A:
    def __init__(self):
        pass


t1 = (4, 5, 6)
a1 = list(t1)
a2 = [4, 5, 6]
a3 = [*t1]
print(a1)
print(a2)
print(a3)
print(a1 == a3)

print('----------')


def some_func_a(number, batka, zadka):
    return f'my number is {number}, batka: {batka}, zadka: {zadka}'


print(some_func_a(2, batka='sasa', zadka=44))
print(some_func_a(2, zadka='sasa', batka=44))
print(some_func_a(zadka=2, batka='sasa', number=44))
print(some_func_a(**{'batka': 22, 'zadka': 33, 'number': 'kaka'}))
# print(dict(zadka=2, batka='sasa', number=44))


print(range(2, 13))
print(range(2, 13, 3).__class__.mro())
print(type(range(2, 13, 3)))
print(list(range(4, 9)))


class A:
    def __init__(self):
        self.mama = 'mama'
        self.baba = 22


c = A()
b = {'dom': {'nice': 'one', 'bad': 'two'}, 2: 2}
a = {'kol': 13, 'bol': {'some': 1, 'any': 2, 'done': 55}, 'b_obj': b, 'c_obj': c}
d = 'kol'
print(a['kol'])
print(a[d])
print(a)
print(a.__class__.mro())
print('--------')

print(a['c_obj'])
print(a['c_obj'].mama)
print(a['c_obj'].baba)


def func_a(kakvo, **kwargs):
    pass


def func_a(**kwargs):
    print(kwargs['gosho'])


func_a(instance=15, bobo=3, gosho='omg', kakvo='pazzz')

a = 5

a = 'PetarStoyanov'
print(a)
# a[2] = 'g'  # TypeError: 'str' object does not support item assignment
print(a)

x = lambda a: a + 10
print(x)

my_list = [1, 2, 3, 2, 2]
# last = my_list.index(22) # ValueError: 22 is not in list
# print(last)  # ValueError

ala_bala = {'ala': 'ala1', 'bala': 'bala2', 'cala': 'cala3'}
print(ala_bala.keys())
print(ala_bala.values())
print(ala_bala.items())

my_dict = {1: 'apple', 2: 'banana'}
copied_dict = my_dict.copy()
print(my_dict == copied_dict)
print(id(my_dict) == id(copied_dict))
