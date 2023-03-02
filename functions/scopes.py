"ОБЛАСТИ ВИДИМОСТИ / ПРОСТРАНСТВО ИМЕН"
#СУЩЕСТВУЮТ 4 ПРОСТРАНСТВО ИМЕН
# LEGB - (local, enclosed, global, build-in)

#build-in это встроеннная пространство (например: print, input, int, str, sum)
#
#global - глобальное пространство это наш текуший файл  (например )
#чтобы посмотреть все глобальные переменные у нас есть функция globals()
#например
# a = 5
# b = 9
# print = (globals())

#enclosed - это замкнутое пространство (находится между двумя пространствами)
#типа локальное пространство внутри которого есть еще одно пространство

#например
# var = 'глобальная'
# def func():
#     var = 'замкнутая'
#     def inner_func():
#         var = 'локальная'
#         def inner_inner_func():
#             var = 'супер локальная переменная'
#             print(var)
#         inner_inner_func()
#         print(var)
#     inner_func()
#     print(var)
# func()
# print(var)



# var = 'глобальная'
# def func():
#     var = 'замкнутая'
#     print(var)
#     def inner_func():
#         var = 'локальная'
#         print(var)
#         def inner_inner_func():
#             var = 'супер локальная переменная'
#             print(var)
#         inner_inner_func()
#     inner_func()
            


# func()
# print(var)
# print(globals())

#local - это пространство (внутри функции)


# a = 'hello'

# def func(a, b):
#     print("GLOBAL", globals()) # {'a':'hello', 'func':<function ...>}
#     print("LOCAL", locals()) # {'a':10, 'b':50}

# func(10, 50)

# num1 = 10

# def func():
#     print(num1) # 10

# func()

# counter = 0

# def increase_counter():
#     global counter
#     counter += 1
#     print(counter)

# increase_counter() # 1
# increase_counter() # 2
# increase_counter() # 3
# increase_counter() # 4


# def count(i):
#     counter = 0

#     def increase_counter():
#         nonlocal counter
#         counter += 1
#         print(counter)

#     for _ in range(i):
#         increase_counter()

# count(10)
# count(10)


# def func():
#     a = 10
#     def inner_func():
#         def inner_inner_func():
#             nonlocal a
#             a += 1
#         inner_inner_func()
#         print(a)
#     inner_func()
# func()


#`````````````````````` РАЗБОР С ЛЕКЦИИ ````````````````````````````````````````````````
  
#visible- видимый
#на примере мы создадим переменную на локальном и на глобальном пространстве
# this_var_visible = 'You can see me inside and outside the function'
# def var_visibility():
#     this_var_is_not_visible = 'You can see me only inside the function'
#     print(this_var_visible)
# var_visibility()
# my_list = ['a','m','i','n','a']
# from functools import reduce 
# new_word = reduce(lambda x, y: x + y, my_list) 
# print(new_word)    #amina