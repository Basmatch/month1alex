#   Функции (def)  -формула как в математике,где происходит отношение между-ми эл-ми,
#                 где измение в одном эл-те влечет измение в другом.
#
#
# Пример:
# def person(hair,eyes,height,gender):
#     print(f'{hair}\n'
#           f'{eyes}\n'
#           f'{height}\n'
#           f'{gender}')
# person('black hair ','eyaes broun', 184, 'male')
# person('white hair','blue eyes',169,'female')
# square(22,55)
#
#
# Пример:
# def-указывает что мы будем создавать функцию
# square-название ф-ии(может быть каким угодно)
# a,b-параметры ф-ии( могут иметь любое значение)
# square(10,33) square(22,55)-вызов ф-ий(внутри значения параметров)
#
# def square(a,b):
#     print(a*b)
# square(10,33)
# square(22,55)
#
#
# У функции есть ключевое слово:
# return- возвращение действия ф-ии ( вместо print всегда пишется return)
#
# Пример:

#def family(father, mother, brother,sister,daughter,soon):
#    return (f'Папа-{father}\n'
#            f'Мама-{mother}\n'
#            f'Брат-{brother}\n'
#            f'Сестра-{sister}\n'
#            f'Дочь-{daughter}\n'
#            f'Сын-{soon}')
#print(family(father='Паша', mother='Ольга', brother='Витя',sister='Марина',daughter='Карина',soon='Владимир'))

#    Параметр по умолчанию.(если происходит измение параметра в print,
#         то старое значение или название перезаписывается на новое)

# def family(father, mother, brother,sister,daughter,soon='Петруха'):
#     return (f'Папа-{father}\n'
#            f'Мама-{mother}\n'
#            f'Брат-{brother}\n'
#            f'Сестра-{sister}\n'
#            f'Дочь-{daughter}\n'
#            f'Сын-{soon}')
# print(family(father='Паша', mother='Ольга', brother='Витя',sister='Марина',daughter='Карина',soon='Максим'))

# Создание кортежа с помощью ф-ий (*args),так же * args помогает создать бесконечное кол-во
# аргументов
#Пример:
# def tuple_number(*args):
#     return args
# print(type(tuple_number()))

#Пример:
# def family(*args):
#     return args
# print(family('Lena','Паша','Danil','Sharik','Barsik','Egor'))

#  Создание словаря с помомощью ф-ии(**kwargs),где:
#           первая звездочка * - это ключ
#           вторая звездочка * - это значение
#   kwargs(ключевое знач-ие аргумента)   - это ключевое слово

# Пример:
# def menu(**kwargs):
#     return kwargs
# print(menu(Завтрак='Яйца',Обед='Борщ',Ужин='Пельмени'))
















































