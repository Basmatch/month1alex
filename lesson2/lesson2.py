#условные операторы if elif else
#циклы while

#условные операторы
#TODO if - работает при условии,если мы уверены на 100 % данного действия
#TODO elif - работает тогда, когда есть 2-ой вариант действия (50*50)
#TODO else - работает тогда ,когда больше нету никаких вариантов

#пример светофор
# color = str(input('Какой сейчас горит Цвет?'))
# print("Смотреть по ситуации")
# if color == 'red':
#     print(f'сейчас горит {color} STOP! ')
# elif color == 'yellow':
#     print(f'сейчас горит {color} READY or STOP! ')
# elif color == 'green' :
#     print(f'сейчас горит {color} GO! ')
# else:
#     print("Смотреть по ситуации!!!")


# Верхний регистр (uper)-  все большие буквы переводит в маленькие
# Нижний регистр (lower)- все маленькие буквы  переводит в большие


#Пример
# color = str(input('Какой сейчас горит Свет?').lower())
# if color == 'red':
#     print(f'сейчас горит {color} STOP! ')
# elif color == 'yellow':
#     print(f'сейчас горит {color} READY or STOP! ')
# elif color == 'green' :
#     print(f'сейчас горит {color} GO! ')
# else:
#     print("Смотреть по ситуации!!!")


#while- цикл бесконечности и используется в основном с 1
#while 1:
 #   print('Привет Алекс')

# while 1:
#     color = str(input('Какой сейчас горит Свет?').lower())
#     if color == 'red':
#         print(f'сейчас горит {color} STOP! ')
#     elif color == 'yellow':
#         print(f'сейчас горит {color} READY or STOP! ')
#     elif color == 'green' :
#         print(f'сейчас горит {color} GO! ')
#     else:
#         print("Смотреть по ситуации!!!")



# while 1:
#     color = str(input('Какой сейчас горит Свет?').lower())
#     if color == 'red':
#         print(f'сейчас горит {color} STOP! ')
#     elif color == 'yellow':
#         print(f'сейчас горит {color} READY or STOP! ')
#     elif color == 'green' :
#         print(f'сейчас горит {color} GO! ')
#     else:
#         print("Смотреть по ситуации!!!")
#
#     exit =str(input('Вы хотите завершить игру? да/нет'))
#     if exit == 'да':
#         print('Спасибо за игру Досвидания')
#         break
#     elif exit == 'нет':
#         print('Супер,давайте продолжим')
#         continue

#!-символ не
#Пример сортировка яблок на хорошие и плохие
apple_box = 10
good_box = 0
bad_box = 0

while apple_box !=0:
    question = str(input ('Какое яблоко? 1-хорошее 0-плохое'))
    if question == '1':
        apple_box -= 1
        good_box += 1
        print(f'общее кол-во яблок:{apple_box}\n'
              f'хороших:{good_box}\n'
              f'плохих:{bad_box}')
        apple_box -= 1
        good_box += 1
        print(f'общее кол-во яблок:{apple_box}\n'
              f'хороших:{good_box}\n'
              f'плохих:{bad_box}')
    elif question == '0':
        apple_box -=1
        bad_box +=1
        print(f'общее кол-во яблок:{apple_box}\n'
              f'хороших:{good_box}\n'
              f'плохих:{bad_box}')

print(f'Плохие{bad_box}\n'
      f'Хорошие{good_box}')
















