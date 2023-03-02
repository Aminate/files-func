#  ===========================    SCOPES    ==========================================
# Задание 1
# Вам дана вложенная функция:

# def foo():
#     var = 'переменная foo'
  
#     def bar():
#         var = 'переменная bar'
#         . . .
 
#     bar()
# foo()
# print('переменная в foo: ', var)
# Внесите изменения в функции bar таким образом чтобы при 
# вызове функции foo и при попытке распечатать переменную var в глобальной области видимости, 
# выводился следующий результат:

# переменная в foo:  переменная foo
# переменная в foo:  переменная bar

# var = 'переменная в foo' 
# def foo(): global var
# var = 'переменная foo' 
# print('переменная в foo: ', var) 
# def bar(): 
#     global var 
#     var = 'переменная bar'
#     bar() 
#     foo()
# print('переменная в foo: ', var)

#ПРАВЕЛЬНОЕ РЕШЕНИЕ


# def foo():
#     var = 'переменная foo'
#     print('переменная в foo: ', var)
  
#     def bar():
#         global var
#         var = 'переменная bar'
 
#     bar()
# foo()
# print('переменная в foo: ', var)



# переменная в foo:  переменная foo
# переменная в foo:  переменная bar


# Задание 2
# У вас есть глоабльная переменная x со значением Я глобальная переменная!. 
# Напишите функцию my_func()которая изменяет значение этой переменной на Я могу изменяться,
# т.е если вы после вызова функции распечатаете переменную x вне функции она должна возвращать вам значение Я могу изменяться.

# Пример:
# my_func()
# print(x)
# Output:
# Я глобальная переменная!
# Я могу изменяться
# Затем чтобы удостовериться что вы изменили именно глобальную переменную выведите в консоль словарь глобальных имен.


# x = "Я глобальная переменная!"
# def my_func(): 
#     global x
#     print(x)
#     x = "Я могу изменяться" 
#     return x
# print(my_func())


# Задание 3 (не окончкен)
# Дана глобальная переменная num со значением 3.
# Напишите функцию mul которая будет возвращать квадрат этой переменной и записывать 
# результат в глобальную переменную num. Вызовите функцию три раза, и распечатайте переменную num.
# mul()
# mul()
# mul()
# print(num)
# Output:
# 6561
# тaк кaк num перезаписали на 9(3*3 = 9) затем на 81
# (99 = 81) и после на 6561(8181 = 6561)num = 3 
# def mul(): 
#     global num num = num ** 2 
#     mul()
#     mul()
#     mul() 
# print(num)

# Задание 4
# Напишите небольшую программу для подсчета доходов и расходов.
# У вас есть глобальная переменная balance = 0 общий счет.
# Программа должна состоять из трех функций: get_salary(amount) - функция 
# для увеличения баланса, которая принимает в аргументы amount - заработная плата и
# увеличивает переменную balance на число переданное в amount.
# pay_bills(amount, log_name) - уменьшает баланс на количество amount , 
# log_name - принимает строку - на что были потрачены деньги и распечатывает результат,
# например если мы вызвали pay_bills(300, 'интернет')
# функция распечатывает строку в виде

# "Вы заплатили 300 сом за интернет"
# И функция get_balance(), которая будет распечатывать вам строку:
# У вас на счету `n` сом
# где n - это текущее значение глобальной переменной balance.
# Вызовите функции в данном порядке:

# get_salary(1000)                      
# get_balance()
# pay_bills(400, 'кабельное тв')
# get_balance()
# Результат:
# У вас на счету 1000 сом
# Вы заплатили 400 сом за кабельное тв
# У вас на счету 600 сом

# balance = 0
# get_salary = int(input())

# balance = 0 
# def get_salary(amount): 
#     global balance 
#     balance = balance + amount 
# def pay_bills(amount, long_name): 
#         global balance 
#         balance = balance - amount 
#         print(f'Вы заплатили {amount} сом за {long_name}') 
#         return balance 
# def get_balance(): 
#         global balance 
#         print(f'У вас на счету {balance} сом') 


# balance = 0 
# def get_salary(amount): 
#     global balance 
#     balance = balance + amount 
#     def pay_bills(amount, long_name): 
#         global balance 
#         balance = balance - amount 
#         print(f'Вы заплатили {amount} сом за {long_name}') 
#         return balance 
#     def get_balance(): 
#         global balance 
#         print(f'У вас на счету {balance} сом') 
#         get_salary(1000) 
#         get_balance() 
#         pay_bills(400, 'кабельное тв')
#         get_balance()



# result = 0 
# def pow_first(x,y): 
#     global result 
#     result = x ** y 
#     def pow_second(z): 
#         global result 
#     result = result % z 
#     pow_first(2, 3) 
#     pow_second(3) 
#     print(result)

# my_list = ['a','m','i','n','a']
# from functools import reduce 
# new_word = reduce(lambda x, y: x + y, my_list) 
# print(new_word)







# list_ = [5, 8, 4, 6, 7]
# result = all(x > 0 for x in list_) 
# print(not result)  #False














#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                 Built-in. Таск 1
# Задание 1
# Дан список:list_ = [1, 2, 3, 4]  
# Выведите сумму всех этих чисел, результат сохраните в новой 
# переменной result и выведите в консоль.

# Вывод:10


# from functools import reduce

# list_ = [1, 2, 3, 4]

# def mul(x,y):
#     return x+y

# result = reduce(mul, list_)
# print(result)
  
# Задание 2
# Создайте переменную list_ и сохраните в нем список из чисел.
# Проверьте, что все числа больше трёх, результат сохраните в новой переменной 
# result и выведите в консоль. Используйте встроенную функцию.

# list_ = [1, 5, -9, 6, -4] 
# result = all(int > 3 for int in list_) 
# print(bool(result)) #False


# Задание 4
# Создайте переменную list_ и сохраните в нем список из чисел.
#  Создайте новый список, состоящий из квадратов этих чисел,
#   результат сохраните в новой переменной result и выведите в консоль.

# Пример:
# list_ = [1, 2, 3, 4]  
# Вывод:
# [1, 4, 9, 16]  
# Используйте встроенную функцию.

# list_ = [1, 2, 3, 4] 
# result = list(map(lambda x: x ** 2, list_)) 
# print(result)

# Задание 5
# Создайте переменную list_ и сохраните в нем список из чисел.
#  Отфильтруйте этот список, оставив только чётные числа,
#   результат сохраните в новой переменной result и выведите в консоль.
# Пример:
# list_ = [1, 2, 3, 4] 
# Вывод:
# [2, 4] 
# Используйте встроенную функцию.

# list_ = [1, 2, 3, 4]
# result = list(filter(lambda x: x % 2 == 0, list_)) 
# print(result)

# Задание 6
# Создайте переменную list_ и сохраните в нем список со строками. Отфильтруйте этот список,
#  оставив только те строки, длина которых больше 7 символов. Результат сохраните в новой переменной 
#  result и выведите в консоль.
# Пример:
# list_ = ['inheritance', 'solid', 'polymorphism', 'dry', 'yagni',] 
# Вывод:
# ['inheritance', 'polymorphism'] 
# filter(функция,  итерируемый объект)
# is_legal = list(filter(lambda age: age > 18, my_list))
# list_ = ['inheritance', 'solid', 'polymorphism', 'dry', 'yagni',] 
# result = list( filter(lambda x: len(x) > 7, list_) ) 
# print(result)

# Встроенные функции.
# Задание 7
# Создайте переменную list_ и сохраните в нем список из чисел. Выведите произведение всех этих чисел. 
# Результат сохраните в новой переменной result и выведите в консоль. Используйте библиотеку reduce.
# Пример:
# list_ = [5, 6, 7, 8] 
# Вывод:1680 

# from functools import reduce 
# list_ = [5, 6, 7, 8] 
# result = reduce(lambda a, b : a * b, list_) 
# print(result)


# Задание 8
# Создайте переменную list_ и сохраните в нем список из чисел.
#  Посчитате количество чётных и нечётных чисел в этом списке в переменных list2 и 
#  list3. Результат сохраните в новой переменной result и выведите в консоль в виде строки:
# even: количество_четных, odd: количество_нечетных
# Пример:
# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ] 
# Вывод:
# even: 5, odd: 5 
# Используйте встроенную функцию.


# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ] 
# even = len(list(map(lambda x: x%2==0, list_))) 
# odd = len(list(map(lambda x: x%2!=0, list_))) 
# result = f'even: {even}, odd: {odd}' 
# print(result)


# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
# list2 = len(list(filter(lambda x: x % 2 == 0, list_))) 
# list3 = len(list(filter(lambda x: not x % 2 == 0, list_))) 
# result = f'even: {list2}, odd: {list3}' 
# print(result) (правельный результат)



# Задание 9
# Создайте переменную list_ и сохраните в нем список из чисел. Если число в списке меньше 0, 
# замените его на False, если больше, то на True. Результат сохраните в новой переменной result и выведите в консоль.
# Пример:
# list_ = [-1, 2, 3, 5, -3, 7] 
# Вывод:
# [False, True, True, True, False, True] 
# Используйте встроенную функцию.
# list_ = [-1, 2, 3, 5, -3, 7] 
# result = (list(map(lambda x: x > 0,list_)))
# print(result)



# Встроенные функции.
# Задание 10
# Создайте переменную list_ и сохраните в нем список со строками. Найдите самое длинное имя из списка функцией reduce.
#  Результат сохраните в новой переменной result и выведите в консоль.
# Пример:
# list_ = ['Paul', 'George', 'Ringo', 'John'] 
# Вывод   George 
# from functools import reduce
# list_ = ['Paul', 'George', 'Ringo', 'John'] 
# result = reduce(lambda x,y: x if len(x) > len(y) else y, list_)
# print(result)



# Задание 11
# Напишите функцию, которая будет проходить по диапазону чисел от 1 до 50. 
# Если число кратно 3 выведите Fizz, в остальных случаях Buzz.
# Результат запишите в переменную result
 
# result = list(map(lambda x: "Fizz" if x%3==0 else "Buzz", range(1,50))) 
# print(result)


# Задание 12
# Создайте переменную list_ и сохраните в ней список с числами. Найдите максимальное 
# число из списка встроенной функцией.
# Результат распечатайте в терминал

# from functools import reduce 
# list_ = [1,2,3,4,5,6,7,8,9,0] 
# result = reduce(lambda x,y: x if x>y else y, list_) 
# print(result)

# Задание 13
# Создайте переменную list_ и сохраните в ней список с числами. Найдите минимальное число из списка встроенной функцией.
# Используйте встроенную функцию reduce. Результат распечатайте в терминал
# from functools import reduce
# list_ = [1,2,3,4,5,6,7,8,9,0] 
# result = reduce(lambda x,y: x if x==y else y, list_) 
# print(result)
# from functools import reduce
# list_ = [23, 45, 11, 34, 23423, 33]
# result = reduce(lambda x,y: x if x==y else y, list_) 
# print(result)


# from functools import reduce 
# list_=[23, 45, 11, 34, 23423, 33]
# res=reduce(lambda x,y:x if not x>y else y,list_) 
# print(res) (правельное решение)


# Задание 14
# Создайте переменную string и сохраните в ней строку. 
# Пройдитесь по ней и выведите индексы символов. Используйте встроенную функцию enumerate.
# Результат распечатайте в терминал
# Пример  string = 'hello'
# Вывод:((0, 'h'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o'))

# string = 'hello'
# for i in enumerate(string):
#    print(i)   
# (0, 'h')
# (1, 'e')
# (2, 'l')
# (3, 'l')
# (4, 'o')

# string='hello' 
# result=tuple(enumerate(string)) 
# print(result)
# ((0, 'h'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o'))

# Задание 15
# Есть последовательность из чисел list_. 
# Верните абсолютное значение каждого числа в виде списка
# Пример
# list_ = [-7, -2, 12, 32, 432, 23, 37, 11, 76, 0, -23, 45, -32, -56]
# Вывод [7, 2, 12, 32, 432, 23, 37, 11, 76, 0, 23, 45, 32, 56]

# list_ = [-7, -2, 12, 32, 432, 23, 37, 11, 76, 0, -23, 45, -32, -56]
# result = list(map(lambda x: abs(x), list_)) 
# print(result)


# Задание 16
# В переменной list_ хранится список с разными типами данных, выведите тип 
# данных элементов последовательности в виде списка.
# Используйте встроенную функцию
# Пример:list_ = ['hello', 123]
# Вывод:[<class 'str'>, <class 'int'>]

# list_ = ['hello', 123] 
# result = list(map(lambda x: type(x), list_)) 
# print(result) #[<class 'str'>, <class 'int'>]

# Задание 17
# Напишите переменную names, которая хранит имена студентов. Если длина имени студента больше 5, 
# добавьте к нему Python, иначе добавьте JavaScript.
# Используйте встроенную функцию
# Пример:names = ['rauchel','john','peter','jessica','steven123','dandy34','kamest','potter']
# Вывод:['rauchel Python', 'john JavaScript', 'peter Python', 'jessica Python', 'steven123 Python', 
# 'dandy34 Python', 'kamest Python', 'potter Python']

# names = ['rauchel','john','peter','jessica','steven123','dandy34','kamest','potter']
# filtered_names = [ x +'Python' if len(x) >= 5  else x + 'JavaScript' for x in names if x.isalpha()]
# print(filtered_names)  (первое решение)


# names = ['rauchel','john','peter','jessica','steven123','dandy34','kamest','potter']
# result=list(map(lambda x:f'{x} Python' if len(x)>5 else f'{x} JavaScript',names)) 
# print(result)   (второе решение с табуляцией)


# Задание 18
# Напишите программу, которая будет проверять валидность почты. Проверьте, чтобы почта заканчивалась на '@gmail.com'.
# Если почта заканчивается на что-то другое, то выведите 'Not valid email'
# Используйте встроенные функции
# Пример:list_ = ['123hello@gmail.com', '123', 'hello']
# Вывод:['123hello@gmail.com', 'Not valid email', 'Not valid email']

# list_ = ['123hello@gmail.com', '123', 'hello']
# (японятие не имею как это делается)


# Задание 19
# Создайте переменную string и сохраните в ней строку. Пройдитесь по ней и выведите индексы символов, начиная с 1.
# Используйте встроенную функцию enumerate
# Пример:string = 'hello'
# Вывод:((1, 'h'), (2, 'e'), (3, 'l'), (4, 'l'), (5, 'o'))
# string = 'hello'
# res=tuple(enumerate(string,1))
# print(res)

# Задание 20
# Создайте 2 списка, список list1, который содержит в себе строки и list2, который содержит в себе числа.
# list1 = ['M', 'A', 'K', 'E', 'R', 'S'] 
# list2 = [236, 54, 33, 21, 89, 1]
# Соедините их в данный вид:[('M', 236), ('A', 54), ('K', 33), ('E', 21), ('R', 89), ('S', 1)]
# Используйте встроенную функцию zip

# list1 = ['M', 'A', 'K', 'E', 'R', 'S'] 
# list2 = [236, 54, 33, 21, 89, 1]
# print(list(zip(list1,list2)))


# Задание 21 (я тут короче вообще пас, и я не стыжусь этого)
# Напишите переменную list_, в которой будут храниться произвольные числа.
# Отфильтруйте в разные списки отрицательные и положительные числа. И соедините эти два списка.
# Используйте встроенные функции
# Пример:list_ = [-7, -2, 12, 32, 432, 23, 37, 11, 76, 0, -23, 45, -32, -56]
# Вывод:[(12, -7), (32, -23)]


# list_ = [-7, -2, 12, 32, 432, 23, 37, 11, 76, 0, -23, 45, -32, -56]
# list1 = ()



# Задание 22
# Дан список:
# list_ = [0.334, 23.3443, 43.4, -13.44, 22.03, -11.033, 267.993, -3.24]
# Используя встроенную функцию внесите квадрат каждого числа округленный до 3х знаков в новый список.


# list_ = [0.334, 23.3443, 43.4, -13.44, 22.03, -11.033, 267.993, -3.24]
# res=list(map(lambda x:round(x**2,3),list_)) 
# print(res)

# Задание 23
# Дана последовательность list_, состоящая из строк. Проверьте, является ли последовательность палиндромом.
#  Используйте встроенную функцию и выведите в консоль.
# Пример:list_ = ['a', 'n', 'n', 'a']
# Вывод:YES

# word = input()
# if str(word) == str(word)[::-1] :
#     print("Palindrome")
# else:
#     print("Not Palindrome") (ЭТО ДЛЯ ТЕБЯ АМИНА ЧЕРНОВИК ЧТОБЫ ТЫ ЗНАЛА КАК РАБОТАЕТ ПАЛИНДРОМ)

# from functools import reduce 
# list_ = ['a', 'n', 'n', 'a'] 
# res = reduce( lambda x, y: x + y, list_) 
# if res == res[::-1]: print('YES') 
# else: print('NO')   (это правельное решение,но я не знаю почему мы использовали reduc


# (my_list = ['a','m','i','n','a']
# from functools import reduce 
# new_word = functools.reduce(lambda x, y: x + y, my_list) 
# print(new_word)        
#короче тут я хотела чтобы оно склеилась как amina )



########################################      all       #################################
# list1 = ['THIS', 'IS', 'SOME','LIST'] 
# проверим с помощью функции all и метода строк isupper,
# действительно ли все строки в списке в верхнем регистре:

# new_list1 = all(str.isupper() for str in list1) 
# print(new_list1)   #True    

# filter - filters, map - как цикл, проходится по каждому элементу и с помощью lambda можем указать какие операции нужно произвести с ними
# reduce -  он выводит не итерируемый объект а один результат например: list_ = [1, 3, 2, 10, 9, 7, 8] хочу найти сумму, то результат такой -> 40

# from functools import reduce

#list_ = [1, 3, 2, 10, 9, 7, 8]

# new_list = reduce(lambda x, y: x + y, list_)
# print(new_list) -> 40

# new_list = list(map(lambda x: x ** 2, list_))
# print(new_list) -> [1, 9, 4, 100, 81, 49, 64]

# filter(lambda x: x > 5, list_) -> [10, 9, 7, 8]
# filtered_list = list(filter(lambda x: x > 5, list_))
# new_list = list(map(lambda x: x ** 2, filtered_list))
# print(new_list)


#==============       ПОНЯТИЕ ОТ НАЧАЛО С ФУНКЦИЯМИ    ========================
# Проще говоря функция это кусок кода который выполняют одну задачу 
# и возвращает результат.
# Но при этом функцию можно использовать многократно
# def greet():
#     return "Hello World!" 
# print(greet())  #Hello World!
#синтаксис выглядит таким образом и выводит нам результат
#1 - тут мы первым прописали def это значит что мы сейчас будем работать
#именно с функцией 
# 2 - потом мы даем какое-то название нашей функции в нашем 
# случае это слово greet
# 3 - () эти скобки нужны чтобы туда закинуть переменные для какой
#либо информации, которую мы можем обработать внутри нашей функции.
# 4 - дальше уже остольное обрабатывает функция
# 5 - return это ключевое слово, которое дает понять 
# Python что за этой командой будет какая-то информация которая является 
# окончательной работой нашей функции и наша функция на этом 
# моменте завершает работу.
#==================Передача аргументов функции================
# теперь создадим функцию которая будет иметь аргумент и сложит их
# def sum(a, b): 
#     return a + b
 
# sum(2, 3) 
# print(sum(2, 3)) #5
# 1 - def значит работа с функцией
# 2 - sum оно сумирует нам одно число с другой и работает с левой стороны
# 3 - потом мы в скобках назначили что оно будет иметь два 
# значениеdef sum(a, b): 
# 4 - Оператор return используется в функциях для возвращения данных 
# после выполнения работы самой функции, в нашем случае оно 
# прибавело a + b
# 5 - а дальше мы дали значения нашим параметрам (a,b)
# 6 - Наша функция сработала и если мы хотим увидеть результат в терминале то можем поместить вызов sum(2, 3) 
# внутрь встроенной функции print( ):  print(sum(2, 3)) 
#(НУЖНО ЗАПОМНИТЬ ЧТО ЕСЛИ МЫ В НАЧАЛЕ ПРИ СОЗДАНИИ
# ПЕРЕДАЛИ ДВА АРГУМЕНТА ТО И В РЕЗУЛЬТАТЕ ОНО ЖДЕТ ОТ НАС ДВА АРГУМЕНТА)



#а если мы передадим только один аргумент в результате то он выдаст ощибку что он ожидал два

# def sum(a, b): 
#     return a + b 
# sum(1)  #TypeError: sum() missing 1 required positional argument: 'b'


#===============Позиционные, ключевые аргументы и аргументы по умолчанию========================
# def welcome(name, lastname): 
#     return f"Привет {name}, по фамилии {lastname}"
# print(welcome('Amina', 'Ashimova')) # Привет Amina, по фамилии Ashimova


# def welcome (name, lastname):
#     return f"Привет {name}, по фамилии {lastname}"
#     print()

# a = lambda list_: list_[-1]
# print(a([1, 2, 3, 4, 5, 'f']))  #f
#получение последнего элемента из списка



# pow_ = lambda x: x ** 2
# print(pow_(9))  #81
#возведение в квадрат


# list1 = [1,2,3,4,5,6,7,8,9,10]

# list1 = [k for k in range(1,11)]
# print(list1)