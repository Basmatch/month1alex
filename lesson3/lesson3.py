#         Структура данных -включает в себя 4 структуры :
# 1 Списки(list)
# 2 Картежи(tuple)
# 3 Словари(dictionary)
# 4 Набор или множество (set)
import nt

#   Списки- это объекты,находящиеся в одной переменной разного типа данных.
#            Есть 2 варанта создания списков :
#
# 1 mylist = []
#
# 2 mylist = list()
#
# Вариант номер 1 в основном служит для создания
#
# Вариант номер 2 служит для разбивки

# name = 'Alexander'
# name = list(name)
# print(name)

# data_list = ['hello', 123,True,False,'world',12.44]
# print(data_list)

# Списки можно:
# 1 добавлять
# 2 удалять
# 3 изменять
# 4 редактировать и т.д

#         1 Добавлять можно разными методами(способами)
#  1-ый append-позволяет добавлять новый элемент в конец списка

#data_list = ['hello', 123,True,False,'world',12.44]
#data_list.append('Aleksandr')
# print(data_list)
#data_list.append('Far Cry')
# print(data_list)

#    2-ой insert -позволяет вставить новое значение между эл-ми,где нужно указать
#                  номер эл-та,т.е. его индекс, перед которым ставится значение.
#
#                0       1     2     3       4       5     - номер индекса
# data_list = ['hello', 123, True, False, 'world', 12.44]  - название элемента
#
# Первый эл-т всегда начинается с цифры 0

#data_list.insert(2, "Radomir")
# print(data_list)

#data_list.insert(1, 'Android')
#print(data_list)

# name = 'Alexander'
# name = list(name)
# name.insert(4,4)
# print(name)

#        Удаление - происходит при помощи 2-х методов:

#  1-ый "remove" удаление по эл-ту (необхимо указать наименование эл-та,
#              который хотим удалить)

# data_list = ['hello', 123,True,False,'world',12.44]
# data_list.remove(False)
# print(data_list)

#  2-ой "del"- удаление по индексу (необходимо указать номер индекса
#                      эл-та,который хотим удалить)

# data_list = ['hello', 123,True,False,'world',12.44]
# del data_list[2]
# # print(data_list)

#       Изменения- совершаем [в квадратных скобках и указываем номер эл-та(индекс),который
#                 хотим заменить и после знака = прописываем название нового эл-та]

# data_list[1]=1997
# print(data_list)

#        Сортировка "sort" -(сортирует эл-ты) работает только с числовыми типами данных

# number = [1,3,2,4,6,5,7,0]
# number.sort()
# print(number)

#    Реверсация "reverse" - помогает отобразить эл-ты в зеркальном отражении

# name = ['A', 'l', 'e', 'x', 'a', 'n', 'd', 'e', 'r']
# name.reverse()
# print(name)

#          Перемещение эл-та с одного списка в другой
#   При перемещении эл-та следует указывать в квадратных скобках []:
# 1 в какой список вставляем эл-т (название строки)
# 2 из какого списка переносится эл-т (название строки)
# 3 указывается номер(индекс) того эл-та из той строки откуда он переносится

# pop- указывает на перемещение эл-та из одного списка в другой

# men=['Ivan','Dima','Anton']
# women=['Masha','Vera','Lubov']
# women.append(men.pop(1))
# print(men)
# print(women)


# men=['Ivan','Dima','Anton']
# women=['Masha','Vera','Lubov']
# women.insert(1,men.pop(1))
# print(men)
# print(women)

#     Цикл for
#Пример: Разместить эл-ты по нужным строкам

# data_list = [12,True,'R','A','D','o',11,12.33]
# numbers = list()
# strings = list()
# boolean = list()
# for i in data_list:
#     if type(i) == str:
#         strings.append(i)
#     elif type(i) == int:
#         numbers.append(i)
#     else:
#         boolean.append(i)
# print(numbers)
# print(strings)
# print(boolean)

# Пример:  из строки boolean удалить 12.33

# data_list = [12,True,'R','A','D','o',11,12.33]
# numbers = list()
# strings = list()
# boolean = list()
# for i in data_list:
#     if type(i) == str:
#         strings.append(i)
#     elif type(i) == int:
#         numbers.append(i)
#     else:
#         boolean.append(i)
#
# boolean.remove(12.33)
# print(numbers)
# print(strings)
# print(boolean)

# Пример:Сделать сортировку чисел в строке numbers

# data_list = [12,True,'R','A','D','o',11,12.33]
# numbers = list()
# strings = list()
# boolean = list()
# for i in data_list:
#     if type(i) == str:
#         strings.append(i)
#     elif type(i) == int:
#         numbers.append(i)
#     else:
#         boolean.append(i)
#
# boolean.remove(12.33)
# numbers.sort()
# print(numbers)
# print(strings)
# print(boolean)

# Пример: В строке strings букву R оставляем , а остальные большие буквы меняем
#           на маленькие.

# data_list = [12,True,'R','A','D','o',11,12.33]
# numbers = list()
# strings = list()
# boolean = list()
# for i in data_list:
#     if type(i) == str:
#         strings.append(i)
#     elif type(i) == int:
#         numbers.append(i)
#     else:
#         boolean.append(i)
#
# boolean.remove(12.33)
# numbers.sort()
# strings[1]='a'
# strings[2]='d'
# print(numbers)
# print(strings)
# print(boolean)











