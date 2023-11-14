    #                   Словари и кортежи
    #
    #
    # "Кортежи" (tuple) - это те же самые списки,но они не изменяются .
    #              Проще говоря это бетонированный список.
    #
    # Кортежи возможно изменить только в одном случае , если их перезаписать, обработать
    #         данные  и обратно вернуть в картежи,т.е еще раз перезаписать.

#data_types = ('hello',123,33.44)
#перезаписываем из кортежа в список
#data_types = list(data_types)
#добавляем эл-т
#data_types.append(222222)
# переводим обратно в кортеж
#data_types = tuple(data_types)
#print(data_types)
#                        "Словари"

#  1 хранят коллекцию ключей и значений.
#  2Ключи должны быть уникальными и не могут повторятся 2 раза. Если происходит повторение ключа
#   он перезаписывается.
#  3 ключи могут быть любого типа данных

# person = {
#     'name': 'Ivan',
#     'age': 49,
#     'education': True,
#     1997: False,
#     145: True,
#     'weight': 55.55,
#    два значения записываются только в []скобках и в кавычках ''
#     'nummer' : ['0555111222', '0777111222']
# }

# 'Добавление'
# person['cars'] = 'bmw'
# person['cars'] = 'lexus'

# Изменение
# person['age'] = 50

# Удаление
# del person[145]

# Можем вывести отдельно ключи (keys) и отдельно значения (values)
# print(person.keys())
# print(person.values())

# Если хотим вывести нужное значение(нужно указать строку и эл-т)
#print(person['nummer'][1])

# Если хотми добавить еще один номер(эл-т)
#person['nummer'].append('0999111222')

#print(person)

# Если хотим все сделать красиво в столбик

# for keys,values  in person.items():
#     print(f'{keys}-{values}')

# Пример из 2-х кортежей создать словарь

# money = (1,3,5,10,20,50,100,200,500,1000,2000,5000)
# person = (False,False,False,False,'Satylganov','Datka','Moldo','Osmonov','Karalaev','Balasagyn', False, 'Chokmorov')
#
# nominal = dict(zip(money,person))
# for i,j in nominal.items():
#     print(f'{i}-{j}')
#
# print(nominal)


#   Метод extend-расширяет список другим списком( при этом объединяемые списки могут содержать
#                 эл-ты любых типов: можно объединить строки с числами или числа с кортежами)

# KGTU = {
#     'address': 'Toktogula 175',
#     'courses': ['Android', 'Backend', 'Frontend'],
#     'bag' : {'fails','errors', 'stack'}
#
# }
# del KGTU['bag']
#
# KGTU['address'] = 'Manasa 66'
#
# KGTU['nummer'] = '0312545125'
#
# KGTU['instagram'] = 'kstu.kg'
# courses = ['Big data','English']
# KGTU['courses'].extend(courses)
#
# for keys,values in KGTU.items():
#     print(f'{keys}-{values}')
#
#
# print(KGTU)













