"=======================================ДЕКОРАТОР==================================================="
# декоратор - это функция высшего порядка которая нужна чтобы расширять функционал другой функции
#не меняя ее
# 
# ДОПИСАТЬ КОД ИЗ ГИТА
# def decorator(func):
#     def wrapper():  #создали вложенную функцию
#         print('Функции началась')
#         func()
#         print('Функции завершилась')
#     return wrapper

# def func():
#     print('hello')

# res = decorator(func)   #чтобы сохдать функцию необязательно оборачивать её в def, можно и просто еее приравнять к функции какой то
# print(res)
# #<function decorator.<locals>.wrapper at 0x7fd325e123b0>

# "=======================Синтаксический сахар======================="
# def decorator(func):
#     def wrapper():  #создали вложенную функцию
#         print('Функции началась')
#         func()
#         print('Функции завершилась')
#     return wrapper
# @decorator  # func = decorator(func)  -
# # @ - возвращает функцию, которая была написана до этого, и переносит эту функцию в функцию, которая будет после @
# #в @ пишем название функции, которую хотим обернуть в новую функцию, это может быть любая функция
# def func():
#     print('hello')

# def decorator(func):
#     def wrapper(*args, **kwargs):  #здесь мы создаем параметры  #*args - tuple
#         func(*args, **kwargs)   #распаковывыем *args, **kwargs, благодаря звездочкам
#     return wrapper 

# import datetime import datetime
# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = datetime.now()
#         func(*args, **kwargs)
#         end = datetime.now()
#         print(f"Функция отработала за {end - start}")
#     return wrapper
# from functools import cache
# @timer
# @cache    #cache - кеш - позволяет за более быстрое время вывести значение, кторое было до этого уже запринтено
# def func(count):
#     for i in range(count):
#         print(i)
# print(func())


# def bold(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return f'<b>{res}</b>'
#     return wrapper

# def italic(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return f'<i>{res}</i>'
#     return wrapper

# @bold     #это будет итогом
# @italic
# def func(string):
#     return f'Hello {string}'
# # func = bold(italic(func))

# print(func('Makers'))

# "================Синтаксический сахар================"
# def decorator(func):
#     def wrapper():
#         print("Функция вызывается")
#         func()
#         print("Функция завершила работу")
#     return wrapper

# @decorator    # func = decorator(func)
# def func():
#     print('hello')

# func()
# # Функция вызывается
# # hello
# # Функция завершила работу

# print(func)
# # <function decorator.<locals>.wrapper at 0x7f1e36656440>

# # @decorator
# def func(string):
#     print(string)

# func("Hello")
# # TypeError: decorator.<locals>.wrapper() takes 0 positional arguments but 1 was given


# def decorator(func):
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs)
#     return wrapper


# def func(a,b):
#     print(a, b)

# func(4,6)
# func(a=5,b=3)
# func(b=5,a=3)

# dict_ = {'a':10, 'b':15}
# func(**dict_)

# tuple_ = (34, 54)
# func(*tuple_)

# from datetime import datetime

# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = datetime.now()
#         res = func(*args, **kwargs)
#         end = datetime.now()
#         print(f"Функция отработала за {end-start}")
#         return res
#     return wrapper

# from functools import cache
# @timer
# @cache
# def func(count):
#     return sum(range(count))

# print(func(count=100000000))
# print(func(count=100000000))

# @timer
# def func(a,b):
#     print(a,b)

# func(1,4)


# # <b>text</b> - жирный
# # <i>text</i> - курсив

# def bold(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return f'<b>{res}</b>'
#     return wrapper

# def italic(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return f'<i>{res}</i>'
#     return wrapper

# @bold
# @italic
# def func(string):
#     return f'Hello {string}'
# # func = bold(italic(func))

# print(func('Makers'))


# def func(count):
#     return sum(range(count))

# start = datetime.now()
# func(100)
# end = datetime.now()
# print(end-start)

# start = datetime.now()
# func(500)
# end = datetime.now()
# print(end-start)






    
















        