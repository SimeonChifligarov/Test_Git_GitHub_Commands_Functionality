# import this
# # from main branch
# 
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
# a.pop() # IndexError: pop from empty list
# a = {'a': 1, 'b': 2, 'c': 3}
# b = a.popitem()
# print(b)
# print(a)
#
# a = (1, 250, 3, 43, 2, 11)
# print(sorted(a))
# print(a)
# a.sort()
# print(a)
#
# a = ['ab', 'bbbbbbbb', 'Az', 'az', '11', 'Ca']
# print(sorted(a))
# print(a)
# a.sort()
# print(a)

# ### received
# gimme *conflict* 

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
# # Try to find BUG
#
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
# # b = [1, 2, 3, 4]
# # [print(row) for row in [el for el in a]]
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
# some_func(1, 2, 3, 4, 5, boss='mass', mad='duddddeeee')
#
# def my111_func(**kwargs):
#     print(kwargs)
#
#
# a = {'azd': 1, 'bab': 4, 'karl': 9, 'linch': 16}
# # print(**a)
# my111_func(**a)
#
# def my22_func(name, age):
#     return f'My name is {name}, and my age is {age}'
#
#
# a = {'name': 'Gosho', 'age': 15}
# b = {'name': 'Gosho', 'age': 15, 'mass': 'azzzz'}
#
# print(my22_func(**a))
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
# # TODO something
# """
# Get this PULL
# """
#
# """
# Yes, All done
# """
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
# msg = input('what do ??? : ')
# time.sleep(3)
# print(msg)
#
# a = 5
#
#
# def azz():
#     azz2()
#     azz3()
#     # azz4()
#
#
# def azz2():
#     print('azzz2')
#
#
# def azz3():
#     print('azzz3')
#
#
# azz()
#
# real_input = input()
#
# a, b = [int(el) for el in real_input[1:-1].split(', ')]
# c, d = eval(real_input)
# print(a)
# print(b)
# print(c)
# print(d)
# print(a == c)
# print(b == d)
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
# while True:
#     try:
#         number = int(input('Please, enter a number: '))
#         break
#     except ValueError:
#         print('Oops... Try again, try better... ')
#
# # try:
# #     print 'Hello'
# # except SyntaxError:
# #     print('stx err')
# #
# # a = 5
def is_in_range(col, row, n=8):
    return 0 <= col < n and 0 <= row < n


print(is_in_range(3, 2))
print(is_in_range(8, 2))
print(is_in_range(11, 2))
print(is_in_range(-3, 2))
print(is_in_range(4, 3, 6))
print(is_in_range(3, 2, 2))
print(is_in_range(-3, 2, 12))
print(is_in_range(10, 10, 12))

a = [1, 2, 3, 4, 5]

for i in range(5):
    b = a[0]
    print(b)
    # print(a[1]) #IndexError

    a = a[1:]
    print(a)
    print('---------')

a = None or []
print(a)

a = {'baby': 'ines', 'b_fam': 'ivanova', 'cac': 'aca'}
print(a['baby'])

class AreWe:
    text_a = 'helllooo'

    def some_func_a(self):
        return 42


b = AreWe()
print(b.some_func_a())
print(b.some_func_a)
print(b.text_a)

a = []
print(not any(a))
print(len(a) == 0)
a.append(3)
a.append(33)
print(not any(a))
print(len(a) == 0)

class A:
    def __init__(self, name, age):
        self.name = name
        self.set_age(age)
        self.__age = self.get_age()

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age


a = A('tosho', 44)
print(a.get_age())

class A:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'I am {self.name}'


a1 = A('pesho')
a2 = A('tosho')
a3 = A('gosho')
a4 = A('bosho')

list_a = [a1, a2, a3, a4]
print([str(el) for el in list_a])

del a3
print([str(el) for el in list_a])

list_b = [el for el in list_a if not el.name == 'gosho']
print([str(el) for el in list_b])

print([str(el) for el in list_a])
list_a.remove(a2)
print([str(el) for el in list_a])

class A:
    pass


class B(A):
    pass


class C(B):
    pass


class D(A):
    pass


a = A()
b = B()
c = C()
d = D()

print(isinstance(a, A))
print(isinstance(a, B))
print('---------')
print(isinstance(b, A))
print(isinstance(b, B))
print('---------')
print(isinstance(c, A))
print(isinstance(c, B))
print(isinstance(c, C))
print('---------')
print(c.__class__.__name__ == A.__name__)
print(c.__class__.__name__ == B.__name__)
print(c.__class__.__name__ == C.__name__)
print('---------')
print(isinstance(c, object))
