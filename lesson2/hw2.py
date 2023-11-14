#Дано 30 бутылок колы
#Нужно рассортировать бутыки по боксами 0.5 1 1.5(будет 3 условия)
#В конце вывести общее колличество бутылок по ящикам
#Доп задание найти среднее значение всех отсортиованных бутылок(делается вне цикла)

cola_box = 13
cola_05 = 0
cola_1 = 0
cola_15 = 0

while cola_box !=0:
        question = str(input('Какая бутылка колы? 1-05 2-1 3-15 '))
        if question == '1':
            cola_box -=1
            cola_05 +=1
            print(f' общее кол-во бутылок колы:{cola_box}\n'
                  f'05:{cola_05}\n'
                  f'1:{cola_1}\n'
                  f'15:{cola_15}')

        elif question == '2':
            cola_box -= 1
            cola_1 += 1
            print(f' общее кол-во бутылок колы:{cola_box}\n'
                  f'05:{cola_05}\n'
                  f'1:{cola_1}\n'
                  f'15:{cola_15}')

        elif question == '3':
            cola_box -= 1
            cola_15 += 1
            print(f' общее кол-во бутылок колы:{cola_box}\n'
                      f'05:{cola_05}\n'
                      f'1:{cola_1}\n'
                      f'15:{cola_15}')

print(f'05:{cola_05}\n'
      f'1:{cola_1}\n'
      f'15:{cola_15}')


print(f'Среднее значение отсортированных бутылок кола {(cola_05+cola_1+cola_15)/3} ')






















