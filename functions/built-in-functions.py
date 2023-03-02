#~~~~~~~~~~~~~~~~~~~~~~ВСТРОЕННЫЕ ФУНКЦИИ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
# enumerate - номерует какую то последовательность,принмает последовательность и возвращает
#генератор где элементы генератора это tuple

# str = 'hello'
# enum = enumerate(str)
# print(enum)        #<enumerate object at 0x104ee1260>
# print(list(enum))    #[(0, 'h'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o')]

#номерация начинается с нуля,но это не индекцы

# str = 'world'
# enum = enumerate(str, 1)
# print(list(enum))              #[(1, 'w'), (2, 'o'), (3, 'r'), (4, 'l'), (5, 'd')]

#номеровать можно все инерируемые обьекты

#часто используется например дан список с числами умножьте на 2 все числа под
#нечетными индексами, умножьте на 3 все числа под индексом, кратными 3


# list1 = [1,4,78,3,7,0,4,2,7]

# for ind in range(len(list1)):
#     element = list1[ind]
#     if ind % 2:   #это тоэе самое как ind % 2 != 0
#         list1[ind] = element * 2
#     if ind % 3 == 0:  #not ind % 3
#         list1[ind] = element * 3
# print(list1)
# [3, 8, 78, 9, 7, 0, 12, 4, 7]
# теперь с помощью enum/enumerate


# list1 = [1,4,78,3,7,0,4,2,7]
# for ind , element in enumerate(list1):
#     if ind % 2:   
#         list1[ind] = element * 2
#     if ind % 3 == 0:  
#         list1[ind] = element * 3
# print(list1)
#[3, 8, 78, 9, 7, 0, 12, 4, 7]



# string  = 'defg'
# dict_ = {}
# for k,v in enumerate(string,4):
#     dict_[k] = v
# print(dict_)

# string = 'defg'
# dict_ = {}
# print(dict_(enumerate(string,4)))



# #zip
# print(dict(enumerate(string,1)))

# list1 = [1,2,3,4,5]
# list2 = 'abcdefg'
# list3 = [0.5,0.3,0.6]

# print(list(zip(list1,list2,list3)))
# [(1, 'a', 0.5), (2, 'b', 0.3), (3, 'c', 0.6)]




#zip- сылается только на короткий элемент, можем передовать 
#столько сколько хотим




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ФУНКЦИЯ ВЫСШЕГО ПОРЯДКА~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#это функция которая:
#принимает в аргументы другую функцию
#возвращать функцию
#создает внутри себя функцию
#вызывает внутри себя функцию


#map - это функция которая принимает в аргументы функцию и итерируемый обьект
#возвращает генератор в котором все элементы - результат принимаемой функции в которую передали
#элементы последовательности

#например 
# mapped = map(int,['1','2','3'])
# print(mapped)     #<map object at 0x104352830>

# print(list(mapped))      #[1, 2, 3]


# дан список с числами, создайте новый список, где элементы - число из списка+1
# list1 = [1,2,3,4]
# # res = [2,3,4,5]

# def res1(i):
#     return i+1
# print(list(map(res1, list1)))

# #теперь с помощью lambda
# print(list(map(lambda i: i+1, list1)))


#черновик для меня
# # const sweetArray = [2, 3, 4, 5, 35]
# # const sweeterArray = sweetArray.map(sweetItem => {
# #     return sweetItem * 2
# # })

# # console.log(sweeterArray)
# #задача
# # list1 = [1,2,3,4]
# # list2 = list1.map 
# # list1item ={return list1 + 1}
# # print(list1)


# list1 = [1,2,3,4]
# mapped_numbers = (list1(map(lambda x : 1 + 2)))



#filter - принимает в аргументы функцию и итерируемый обьект возврашает генератор
#в котором элементы из последовательности прошедшие фильтр (функция вернула True)

#пример 
# list2 = [-3,4,6,43,75,10]
# def is_positive(i):
#         return i > 0  #(True,False)
# print(list(filter(is_positive, list2)))   #[4, 6, 43, 75, 10]

# #с lambda функцией

# print(list(filter(lambda i: i>0, list2)))      #[4, 6, 43, 75, 10]

#задачка


# list1 = ['Hello', 'woRLD', 'MAKERS']
# res = ['Hello', 'MAKERS']







# reduce - функция которая импортируется из модуля functools
#которая принимает в себя функцию и итерируемый обьект
#возвращает один результат

#пример
# from functools import reduce

# list1 = [2,3,4,65,87,1]
# def mul(x,y):
#     return x*y
# res = reduce(mul, list1)
# print(res)   #135720 


# в x идет число последовательный и в y число которое мы хотим умножить и так до конца


# string = 'hello'
# print(reduce(lambda x,y: x+'$'+y, string))
# h$e$l$l$o
# x='h', y='e' -> 'h$e'
# x='h$e', y='l' -> 'h$e$l'
# x='h$e$l', y='l' -> 'h$e$l$l'
# x='h$e$l$l', y='o' -> 'h$e$l$l$o'

#вам дан список с какими то слова и вывведите самое длиное слова в списке

# res = reduce(mul, list1)
# print(res)
# # 74880 = 2*4*6*3*65*8


# string = 'hello'
# print(reduce(lambda x,y: x+'$'+y, string))
# # h$e$l$l$o
# # x='h', y='e' -> 'h$e'
# # x='h$e', y='l' -> 'h$e$l'
# # x='h$e$l', y='l' -> 'h$e$l$l'
# # x='h$e$l$l', y='o' -> 'h$e$l$l$o'


# list1 = ['hello','world','makers','bootcamp','aaa']
# # bootcamp
# print(reduce(
#     lambda x, y: x if len(x) > len(y) else y,
#     list1))


#~~~~~~~~~~~~~~~~~~~~~~~ РАЗБОР С ЛЕКЦИИ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#lambda - является анонимной,без имени
#синтаксис этой функции выглядит так:
#lambda аргументы : действие 
# В начале прописывается ключевое слово lambda, в 
# аргументы указываются переменные куда попадают переданные объекты, 
# через двоеточие указывается какое действие надо совершить с данными аргументами.
# Например:
# sum = lambda x, y :  x + y
# sum(5, 4)
# тоесть мы через sum указываем и через функцию lambda
# и через дваиточее что хотим сложить их
# x=у нас будет(5) а y= у нас будет (4) sum = lamba 5, 4 : 5 + 4

#map
# map() принимает два обязательных аргумента - функцию и итерируемый объект,
# т.е объект, который способен возвращать элементы по одному
# (к примеру списки, кортежи, множества и.т.п).
# map() будет брать по очереди каждый элемент в итерируемом объекте и применять к каждому
# элементу функцию(переданную в качестве первого аргумента).



# примеры с map
#создадим список и пер-им анонимную 

# list_ =[1, 43, -65, 23]
# list2 = list(map(lambda x: x < 0, list_))
# print(list2)      #[False, False, True, False]


# func = lambda num: num + 1
# res =[]
# list_ = [1, 2, 4, 5, 6]
# for i in list_:
#     res.append(func(i))
# print(res)      [2, 3, 5, 6, 7]














# Что это значит, например:
# old_list = ['1', '2', '3', '4', '5', '6', '7'] 
# new_list = list(map(int, old_list)) 
#print(new_list)    #[1, 2, 3, 4, 5, 6, 7]

# map() берет каждую строку из old_list и применяя к ней функцию int(), преобразует в число:
# ‘1’ ---> int(‘1’) ---> 1  
# ‘2’ ---> int(‘2’) ---> 2
#тоесть простыми слова map функция которая берет элемент и к каждому приминает что-то

# Для того чтобы преобразовать объект map в список мы можем воспользоваться другой встроенной
# функцией - list().
# В итоге мы получаем список из чисел:
# [1, 2, 3, 4, 5, 6, 7]

#теперь попробуем с строк первые буквы сделать заглавной,мы попробуем 
#с функцией title() так же после попробуем с функцией map()
#title() пример
# list_ = ['amina', 'adilet', 'ilya', 'daana'] 
# new_list = [] 
# for x in list_: 
#     new_list.append(x.title()) 
# print(new_list)  #['Amina', 'Adilet', 'Ilya', 'Daana']


#мы попробували с  title() а теперь с map()
# В начале напишем свою функцию generate, принимающая аргумент в переменную item,
# и применяющая к item метод строк title():

# def generate(item): 
#     return item.title() 

# list_ = ['amina', 'adilet', 'ilya', 'daana'] 
# new_list = list(map(generate, list_)) 
# print(new_list)   #['Amina', 'Adilet', 'Ilya', 'Daana']

#так же функ map может принимать в себя несколько списков
# l1 = [1, 2, 3] 
# l2 = [4, 5, 6] 
# new_list = list(map(lambda x, y: x + y, l1, l2)) 
# print(new_list)   #[5, 7, 9]

#ну тут все логично,а теперь допустим что наш лист1 и лист2 не 
#одинаковы по длине тоесть один меньше второго,тогда map 
#остановиться в тот момент когда один из списков закончится
#к примеру
# l1 = [1, 2, 3] 
# l2 = [5, 6] 
# new_list = list(map(lambda x, y: x + y, l1, l2)) 
# print(new_list)   #[6, 8]
#тут так как у 3 нету пары его проигнарировали к чертовой матери


#filter - прежде всего это функ которая делит и возвращает то что мы хотим
#типа true/false
# filter() имеет следующий синтаксис:
# filter(функция,  итерируемый объект)
# age =
# def is_legal(age):
#     return age > 18
# print(age)

#пример еще с filter
#получаем с списка только четные числа
# def filter_nums(number):
#     if number % 2 == 0:
#         return True

# res = list(filter(filter_nums, [1,2,4,6,8]))
# print(res)     #[2, 4, 6, 8]






#тот же пример с ламда
#is_legal = list(filter(lambda age: age > 18, my_list))

# в этом примере я покажу как отсартировать больше 75 ти числ 
# scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# def get_scores(score):
#     return score > 75
# over_75 = list(filter(get_scores, scores))
# print(over_75)     #[90, 76, 88, 81]

#а в след примере как мы отсортировали тех людей кто входит в группу пайтон
# students = [{'name': 'jane', 'group': 'python'}, 
#              {'name': 'joe', 'group': 'js'}, 
#              {'name': 'jack', 'group': 'python'}]
# pythons = list(filter(lambda student: student['group'] == 'python', students))
# print(pythons)    
#[{'name': 'jane', 'group': 'python'}, {'name': 'jack', 'group': 'python'}]

#reduce - во первых чтобы потключать эту функцию для начало нужно 
#вызвать его нужно прописать
# import functools 


#Мы знаем что reduce по завершению работы 
# возвращает нам результат в виде одного объекта


#~~~~~~~~~~~~~~~~~~~~~~~`      КРАТКОЕ ПОНЯТИЕ ОТ НУРКАМИЛЫ    `~~~~~~~~~~~~~~~~~~~`
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





















# list1 = ['THIS', 'IS', 'SOME','LIST'] 
# проверим с помощью функции all и метода строк isupper,
# действительно ли все строки в списке в верхнем регистре:

# new_list1 = all(str.isupper() for str in list1) 
# print(new_list1)   #True  