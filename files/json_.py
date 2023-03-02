#=====================================JSON========================================"
# JavaScript Object Notation - tдиный формат, в котором храниться только те типы 
# данных, которые есть во всех яп поддерживаемые json
# JSON.
# JSON, или JavaScript Object Notation - это формат для обмена данными.
#  числа int, float
# строки str
# словари dict
# булевые значения True, False
# списки list
# пустое значение None




# импортируем всегда json
# import json
# сериализация - перевод из python в json  #dump
# десерилазация - перевод из json в python #load

# print(dir(json))   #просмотр содержимого
#например json:методы



#dump - функция которая переводит python обьект в json строку


#loads - (множество) функция которая переводит json строку в python обьект



#например 
# python_list = [1,2,3]
# json_list = json.dumps(python_list)
# print(type(python_list))  #<class 'list'>
# print(type(json_list))    #<class 'str'>

# print(python_list) [1, 2, 3]
# print(json_list)   "[1, 2, 3]"

# json_dict = '{"a":1, "b" :2}'
# python_dict = json.loads(json_dict)


# print(type(json_dict)) #<class 'str'>
# print(type(python_dict)) #<class 'dict'>


# json есть правила что можно использовать только двойные ковычки



# list_ = [
#     1,2,34.6,
#     (1,2,3),
#     {'A':1},
#     'HELLO',
#     True,False, None
# ]
# with open("test.json", "w") as file:
#     json.dump(list_,file)

#[1, 2, 34.6, [1, 2, 3], {"A": 1}, "HELLO", true, false, null]




# with open("test.json","r") as file:
#     res = json.load(file)
#     print(res)

#[1, 2, 34.6, [1, 2, 3], {'A': 1}, 'HELLO', True, False, None]

#None - null 
#мы не можем использовать в json


#===================================== РАЗБОР С ЛЕКЦИИ ========================================
# dump() dumps()
# load() loads()

#json - он вообще для чего нам нужен?
# он нужен для того чтобы мы могли передовать коды в интерфейс (тоесть посредник для js)
# python_list = [1,2,3]
# json_list = json.dumps(python_list)
# print(type(python_list)) # list
# print(type(json_list)) # str

# print(python_list) # [1,2,3]
# print(json_list) # "[1,2,3]"



# json_dict = '{"a":1, "b":2}'
# python_dict = json.loads(json_dict)

# print(type(json_dict)) # str
# print(type(python_dict)) # dict


# list_ = [
#     1,2,3,
#     4.6,
#     (1,2,3),
#     {'A':1},
#     'hello',
#     True, False, None,
#     # {1,2}
#     # TypeError: Object of type set is not JSON serializable
# ]

# with open("test.json", "w") as file:
#     json.dump(list_, file)






# with open("test.json", "r") as file:
#     res = json.load(file)

# print(res)
# [1, 2, 3, 4.6, [1, 2, 3], {'A': 1}, 'hello', True, False, None]

