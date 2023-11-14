#import datetime  #    Модули-отдельные файлы с кодом ,которые можно повторно использовать
#           в других программах .
# random(случайность) имеет 4 значения :
#    import-Применяется для того,что бы ,сделать код в одном модуле, доступным для
#           работы в другом
#
#    randint-принимает два аргумента:начало и конец диапазона и возвращает случайное целое
#            число в этом диапазоне
#
#    sample-позволяет вам брать случайную выборку эл-ов из набора данных или вектора с заменой
#           или без нее
#
#    randrange-возвращает случайно выбранное число из последовательности
#
import random
from random import randint, sample
import datetime
# Пример:(Игра казино)
print('Добро пожаловать в казино')
start = datetime.datetime.now()

try:
    cash = int(input('Внесите вашу ставку'))
    print(f'Вы внесли - {cash}')
    if cash <= 0:
        print('Не пытайтесь меня обмануть вводите нормальные деньги!')

except:
    print('Произошла ошибка системы!')

while cash != 0:
        try:
            bet = int(input(f'Какую сумму из {cash} желаете поставить!'))
            if bet>cash:
                print('У вас не хватает денег!')
                continue
            person = [randint ( 1, 6), randint( 1, 6)]
            computer = [randint( 1, 6), randint( 1, 6)]
        except:
            print('Вводите только число')
            continue

        if  sum(person) > sum(computer):
                cash += bet
                print(f'Вы выиграли у вас денег {cash}')
        elif sum(person) < sum(computer):
                cash -= bet
                print(f'Вы проиграли у вас денег {cash}')
        else:
                print('Ничья!!!')




endgame = datetime.datetime.now() - start
print(f'Вы провели в игре - {endgame}')










# # Пример(1): кофейный аппарат
#
# print('Здравствуйте возьмите стаканчик')
# cash = int(input('Внесите наличку!'))
# print(f'Баланс - {cash}')
# while cash != 0:
#     print('-'*20)
#     coffe = str(input('Выберите кофе\n'
#                        '1-Латте\n'
#                        '2-Американо\n'
#                        '3-Капучино\n'
#                        '4-Айскофе\n'))
#     print('-'*20)
#     if coffe == '1':
#         print('-'*20)
#         print('Латте стоит 20 р')
#         print('-'*20)
#         answer =str(input('Вы уверены в своем заказе?да/нет'))
#         if answer == "да":
#             cash -= 20
#             print(f'У вас осталось денег на карте : {cash}\n'
#                   f'Вы купили Кофе №{coffe}\n'
#                   f'1-Латте\n'
#                       '2-Американо\n'
#                       '3-Капучино\n'
#                       '4-Айскофе\n')
#             break
#         elif answer == 'нет':
#             button_exit = int(input('Нажмите кнопку 1 для выхода'))
#             if button_exit == 1:
#                 print('Всего хорошего')
#                 break
#             else:
#                 print('Пожалуйста нажмите 1')
#                 continue
#
#
#     elif coffe == '2':
#          print('-' * 20)
#          print('Американо стоит 50 р')
#          print('-' * 20)
#          answer = str(input('Вы уверены в своем заказе?да/нет'))
#          if answer == "да":
#              cash -= 50
#              print(f'У вас осталось денег на карте : {cash}\n'
#                    f'Вы купили Кофе №{coffe}\n'
#                    f'1-Латте\n'
#                       '2-Американо\n'
#                       '3-Капучино\n'
#                       '4-Айскофе\n')
#              break
#          elif answer == 'нет':
#                 button_exit = int(input('Нажмите кнопку 1 для выхода'))
#                 if button_exit == 1:
#                     print('Всего хорошего')
#                     break
#                 else:
#                     print('Пожалуйста нажмите 1')
#                     continue
#     elif coffe == '3':
#          print('-' * 20)
#          print('Капучино стоит 60 р')
#          print('-' * 20)
#          answer = str(input('Вы уверены в своем заказе?да/нет'))
#          if answer == "да":
#             cash -= 60
#             print(f'У вас осталось денег на карте : {cash}\n'
#                   f'Вы купили Кофе №{coffe}\n'
#                   f'1-Латте\n'
#                   '2-Американо\n'
#                   '3-Капучино\n'
#                   '4-Айскофе\n')
#             break
#          elif answer == 'нет':
#             button_exit = int(input('Нажмите кнопку 1 для выхода'))
#             if button_exit == 1:
#                 print('Всего хорошего')
#                 break
#             else:
#                 print('Пожалуйста нажмите 1')
#                 continue
#
#     elif coffe == '4':
#          print('-' * 20)
#          print('АйсКофе стоит 90 р')
#          print('-' * 20)
#          answer = str(input('Вы уверены в своем заказе?да/нет'))
#          if answer == "да":
#             cash -= 90
#             print(f'У вас осталось денег на карте : {cash}\n'
#                   f'Вы купили Кофе №{coffe}\n'
#                     f'1-Латте\n'
#                     '2-Американо\n'
#                     '3-Капучино\n'
#                     '4-Айскофе\n')
#             break
#          elif answer == 'нет':
#             button_exit = int(input('Нажмите кнопку 1 для выхода'))
#             if button_exit == 1:
#                 print('Всего хорошего')
#                 break
#             else:
#                 print('Пожалуйста нажмите 1')
#                 continue



#Пример:









































