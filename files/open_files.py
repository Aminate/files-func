#===========================   ПАКЕТЫ И МОДУЛИ  ============================================
# модуль это любой файл с расщирением .py
# можно с любого файла импортировать переменную с помощью импорт 
# import (например test)
#from test import 'a'
# пакет услуг - типа несколько
# package - набор модулей (в папке обьезательно должен быть (__init__.py)




#когда мы открываем какой-нибудь файл передается два аргумента типа мы хотим открыть файл,
# а второй аргумент в каком режиме мы его хотим открыть (типа в режиме чтение или в режиме писменности)

# from package.test1 import hello
# from package.test2 import list1
# module - любой файл с расширением .py

# import test
# print(test.a)

# from test import a
# print(a)

# package - набор модулей (в папке обязательно должен быть __init__.py)

# from package.test1 import hello
# from package.test2 import list1

# "==================================       РАБОТА С ФАЙЛАМИ             ======================================="
# open - мы будем открывать файл в определенном режиме
# какие режиме у нас есть
# r - read (только режим чтение)
# w - write (только для перезаписи тоесть каждый раз при открытии очищает файл)
# a - append(только для до записи,значит будет записоваться в конец)
# x - (создает файл но если он уже создон то выдает ощибку)
# b - бинарный вид (тоесть мы можем записовать что-то в бинарном ввиде)



# Read -     (функция)
# позволяет только читать а не записывать

# file = open('test1.txt')
#если такого файла нет то выйдет ощибка,
# если не указать режим - откроется в режиме чтения


# print(dir(file))


# file.close()    #обьезательно нужно закрывать!

# close - для закрытие файла
# closed - для булевого значение проверки закрывает/если не закрыт то закрывает
# name - передает название файла

#readable - для  чтение содержимого
# writable - для проверки записи


# если мы запустим read еще раз то оно сылается где стоит коретка


#а чтобы вывелось два раза мы переносим каретку и указываем индекс,если с начало то с  индексом(0)
# seek(0)

# так же можем проходиться по индексу


# tell - скажет нам где находится каретка
#file = open('test.txt', 'r')
# если такого файла нет - выйдет ошибка
# если не указать режим - откроется в режиме чтения

#print(dir(file))

# print("readable", file.readable()) # True
# print("writable", file.writable()) # False

# print(file.read()) # считывает от начала до конца
# print(file.read()) # '', потому что каретка в коце файла
# file.seek(0) # перенос каретки в начало (на индекс 0)
# print(file.read()) # считывает от начала до конца

# file.seek(5)
# print(file.read()) # считываем от 5 индекса до конца

# file.seek(0)
# print(file.read(5)) # 'Hello' считываем 5 символов
# print(file.read()) # '\nWorld\nMakers\n' считваем от 5 до конца

# file.seek(0)
# print(file.readline()) # 'Hello\n' считывает до \n
# print(file.readline()) # 'World\n' считывает до \n

# file.seek(0)
# print(file.readlines())
# # ['Hello\n', 'World\n', 'Makers\n']

# file.seek(10)
# print(file.tell()) # 10

# file.read() # считал до конца (на 19 индекс)
# print(file.tell()) # 19

# # file.write("hello")
# # io.UnsupportedOperation: not writable
# # !запись в режиме чтения запрещена

# print(file.name) # 'test.txt'
# print(file.closed) # False
# file.close() # !важно закрывать файлы
# print(file.closed) # True



# пример работы с читением:
# file1 = open('test1.txt', 'r')  
# data = file1.read()
# print(data)
# file1.close()
# Hello
# World
# Makers
#так же можно с функцией with где можно не закрывать в конце файл и тот и тот дает нам одинаковый результат:
# with open('test1.txt', 'r') as file:
#     data = file.read()
#     print(data)
# Hello
# World
# Makers

#(СКОЛЬКО БЫ НЕ БЫЛО ДАННЫХ МЫ ПОЛУЧАЕМ ЕГО ВЕЗДЕ С ЛЮБЫМ РАСШИРЕНИЕМ)




# Write - 

# если такого файла нет а мы указали то он автоматически открывает новый файл, таким названием который мы указали
# если мы указали сушествуещий файл то он выдает нам в очищенном ввиде

# в каком режиме откроем то и будет делать если в режиме чтение то оно не будет записывать

#если мы хотим чтото записать с переносом строки то нужно указать /n
# file.write('hello)
#file.write('world')
#helloworld мы не ввили /n


#а если пробелом то ввидем его внутри скобки (пробел)


# а если мы по индексу 0 записываем что-то то он не ставит туда то что мы записали а просто перезаписывает индексы
#так сказать заменяет по индексу

# file = open("new_file.txt", 'w')
# # если файл нет - создает
# # если есть - очищает

# print("readable", file.readable()) # False
# print("writable", file.writable()) # True

# # file.read()
# # io.UnsupportedOperation: not readable
# # !в режиме записи чтение запрещено

# file.write('Hello ')
# file.write('Makers')
# # Hello Makers

# file.writelines(['Hello', 'World'])
# # Hello MakersHelloWorld

# file.writelines(['\nNew\nLine'])
# # Hello MakersHelloWorld
# # New
# # Line

# file.seek(0)
# file.write("AAA")
# # AAAlo MakersHelloWorld
# # New
# # Line

# file.close()

# Append - 


# он так же как и write создает файл если его нет а мы указали его
# так же можем читать а не писать
# append всегда записывает в конце, и всегда можем с начальной буквы пишется
# file = open("new_file2.txt", 'a')
# # если файла нет - создается новый
# а если мы хотим добавить в начало то можем использовать a+ append

# print("readable", file.readable()) # False
# print("writable", file.writable()) # True

# file.write('Hello')
# # дозапись идет в конец файла (старые данные не удаляются)

# file.seek(0)
# file.write("New")
# # все равно в конец дозапись

# file.close()

#=============================  констекстный менеджер  ===============================
# as - чтобы создать переменную, а значение указываем до этого

# действие будет работать пока файл открыт
# папки всегда закрываем с слешом /

# try:
#     file = open("aaa.txt", 'w')
#     file.read()
# finally:
#     file.close()

# бинарный пример с фотографией:


# with open('test.txt') as f:
#     f.read()
#     f.seek(0)
#     f.read()
#     print(f.closed) # False
# # файл закрывается   
# print(f.closed) # True

# with open("python.jpg", 'rb') as image:
#     print(image.read())

# with open("python.jpg", 'rb') as image:
#     binary_image = image.read()

# with open("new_image.jpg", 'wb') as file:
#     file.write(binary_image)


#===================== РАЗБОР С ЛЕКЦИИ ===========================
# b - бинарные
# t - текст
# эти две функции можно использовать с другими функциями в паре



#пример:
#мы создаем переменную файл, и открываем его прописывая название этого файла, и пишем режим в котором хотим открыть 
#этот файл
# file1 = open('test1.txt','r') 
# а после мы можем открыть переменную в котором будем считать этот файл, типо вот так:
# data = file1.read()
# print(data)    
#  I tell myself you don't mean a thing
# And what we got, got no hold on me
# But when you're not there, I just crumble
# I tell myself I don't care that much
# But I feel like I die 'til I feel your touch

#и вот оно показала все данные  нам это в режиме чтение,в виде строки



# но если мы хотим в определенном ввиде, тоесть какую то часть то мы можем выделить его по индексу, или же 
# первые три буквы
# file1 = open('test1.txt','r') 
# data = file1.read(3)
# print(data) 
#I t 
# тут он посчитал вместе с табуляцией
# а если мы пропишем принт два раза:

# file1 = open('test1.txt','r') 
# data = (file1.read(10))
# data = (file1.read(5))
# print(data) 
# I t
# I t
#то он вывел нам два раза от начало и три символа

#так же мы можем ввести с помощью индексов начало шага и конец 3 этапно,например:

# file1 = open('test1.txt','r') 
# data = (file1.read(10))
# data = (file1.seek(0))
# data = (file1.read(5))
# print(data) 
#I tel
# И вот оно вывела нам проходя 10 шага и 5 включительно
# seek - он ставит курсор в определенное место куда мы указали


#метод  readline()
# возвращает нам по строчно, например:
# file1 = open('test1.txt','r') 
# print(file1.readline())
#I tell myself you don't mean a thing
#мы получаем первую строку
# а если допустим я хочу получить следущую строку то прописываю еще раз, принт 
# file1 = open('test1.txt','r') 
# print(file1.readline())
# print(file1.readline()) # и так каждый раз

# I tell myself you don't mean a thing

# And what we got, got no hold on me

#и так каждый раз, но это не удобно, поэтому мы можем пройтись по циклам:
	
# for line in file
# позволяет читать файл построчно - так как file - это генератор уже организованный в виде множества строк.
#тоесть можно пройтись по элементам,и так как наш элемент считается строкой просто принтим line и проходимся по ним


# file1 = open('test1.txt','r')
# for line in file1:
#     print(line)

# и вот так мы прошлись по каждой строке, с помощью циклов

# метод  readlines ()
#он считывает наши строки как список, тоесть используем list
# file1 = open('test1.txt','r')
# list_ = file1.readlines()
# print(list_)
# ["I tell myself you don't mean a thing\n", 'And what we got, got no hold on me\n',
#  "But when you're not there, I just crumble\n", "I tell myself I don't care that much\n", 
#  "But I feel like I die 'til I feel your touch"]


# можно так же работать с list comprahaishen, например:
# я хочу чтобы наш список не содержал \n то как я это сделаю
# file1 = open('test1.txt','r')
# list_ = file1.readlines()
# list_ = [line.replace('\n', '') for line in list_]
# print(list_)

# ["I tell myself you don't mean a thing", 'And what we got, got no hold on me', "But when you're not there,
#  I just crumble", "I tell myself I don't care that much", "But I feel like I die 'til I feel your touch"]

#Write - записывает наши данные в файл, принимает какую-то стоку
# file1 = open('test1.txt','w')
# print(file1.write('Makers')) 
#помогает нам записывать что-то либо создает новый файл
#(НЕ ПОЛУЧАЕТСЯ СОЗДАТЬ ФАЙЛ СПРОСИТЬ У НУРКАМИЛЫ)

#как добавить содержимое файла(данные)
# file2 = open('bootcamp.txt','w')
# file2.write("It's such a beautiful day today")
# file2.write("Today is my birthday")
#тут наша вторая строка прекрипилась к первой строке, 
# чтобы такого не было мы добавим в конце строки + '\n'

# 'a' #помогает нам не терять ранее содержимое из файла 'a' от слово append
#например:
# file1 = open('test1.txt, w')
# print(file1.write('Bootcamp'))

#если я хочу чтобы каждое строка начиналась с новой то добавляю в конце \n


#'x'  # используется когда хотим создать новый файл 
#например:
#file2 = open('makers2.txt','x')



# writelines
#например
