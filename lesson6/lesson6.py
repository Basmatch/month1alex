#   Lymbda function и исключения try except

# Пример
# def my_family(role, name,age=18):
#     return (f'{role}-{name}-{age}')
# print(my_family(role='Отец',name='Иван',age=50))
# print(my_family(role='Мать',name='Мария',age=45))
# print(my_family(role='Сын',name='Борис',age=25))
# print(my_family(role='Дочь',name='Алина',age=20))

# Пример :
# def average(*args):
#     return  sum(args)/len(args)
# count =7
# while count!=0:
#     count-=1
#     temp = float(input('Какая температура\n'
#                        '01\n'
#                        '02\n'
#                        '03\n'
#                        '04\n'
#                        '05\n'
#                        '06\n'
#                        '07\n'
#                        '09'))
#     print(average(temp))
#
#
#
#  lymbda function-это та же функция, только ее используют 1 раз.(разовая ф-ия)
#  Пример:

# summa = lambda a,b: a+b
# print(summa(1,4))

#Пример:
# words = ['apple','banana','strawberry','orange']
# len_w = list(filter(lambda x: len(x)>=5, words))
# print(len_w)

#Пример:
# list_=['word','python','java']
# big = list(map(lambda x: x.upper(),list_))
# print(big)

# try except
# Пример:

# try:
#     number = '1'
#     number2 = 2
#     print(number+number2)
# except:
#     print('Складывать число со строкой нельзя')
#
# Пример:

# while 1:
#     try:
#         number = int(input('Введите первое число'))
#         operation = str(input('+ - / *'))
#         number2 = int(input('Введите второе число'))
#     except:
#         print('Пожалуйста пишите толбко цифры')
#         continue
#     if operation == '+':
#         print(number+number2)
#     elif operation == '-':
#         print(number-number2)
#     elif operation == '*':
#         print(number*number2)
#
#     elif operation == '/':
#         try:
#            print(number / number2)
#         except:
#               print('На ноль делить нельзя!')
#               continue







































































