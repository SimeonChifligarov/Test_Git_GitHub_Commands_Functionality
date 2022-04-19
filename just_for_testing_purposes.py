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

def heavy_calculation(*args):
    arguments = list(*args)
    result = 0
    for arg in arguments:
        result += arg
    return result


def calculate(*args, memo={}):
    arguments = tuple(args)
    try:
        value = memo[arguments]  # return already calculated value
    except KeyError:
        value = heavy_calculation(arguments)
        memo[arguments] = value  # update the memo dictionary
    return value


print(calculate(3, 4, 5))
print(calculate(3, 2))
print(calculate(3, 3, 5))
print(calculate(3, 4, 5))
print(calculate(3, 2))

my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict2 = my_dict.copy()
my_dict3 = {'a': 1, 'b': 2, 'c': 3}
my_dict4 = {'b': 1, 'a': 2, 'c': 3}
my_dict5 = my_dict

print(my_dict == my_dict3)
print(my_dict == my_dict4)
print(my_dict == my_dict2)
print(my_dict == my_dict5)

my_dict2['d'] = 4
print(my_dict)
print(my_dict2)
print(my_dict == my_dict2)

my_list = [1, 2, 3, 4, 5]
my_list2 = [1, 2, 3, 4, 5]
my_list3 = my_list.copy()

print(my_list == my_list2 == my_list3)
# print(my_list == my_list3)
# print(my_list3 == my_list2)
my_list2.append(100)
print(my_list == my_list2)
print(my_list == my_list3)

my_list = [1, 2, 3, 4, 5]
my_list2 = [1, 2, 3, 4, 5]
my_list3 = my_list.copy()
my_list4 = my_list

print(my_list == my_list2)
print(id(my_list) == id(my_list2))
print(id(my_list) == id(my_list3))
print(id(my_list) == id(my_list4))

a = []
a.pop() # IndexError: pop from empty list
a = {'a': 1, 'b': 2, 'c': 3}
b = a.popitem()
print(b)
print(a)

a = (1, 250, 3, 43, 2, 11)
print(sorted(a))
print(a)
a.sort()
print(a)

a = ['ab', 'bbbbbbbb', 'Az', 'az', '11', 'Ca']
print(sorted(a))
print(a)
a.sort()
print(a)

def sort_me_baby(el1):
    return el1[0]

