print('Здравствуйте Александр')
money = int(input('Внесите наличные!'))
print(f'Баланс -{money}')
while money !=0:
    print('-'*30)
    toy=str(input('Выберите игрушку\n'
                  '1-Игрушка_1\n'
                  '2-Игрушка_2\n'
                  '3-Игрушка_3\n'
                  '4-Игрушка_4\n'
                  '5-Игрушка_5\n'
                  '6-Игрушка_6\n'
                  '7-Игрушка_7\n'
                  '8-Игрушка_8\n'))
    print('-'*30)
    if toy == '1':
        print('-'*30)
        print('Игрушка №1 стоит 30 р')
        print('-'*30)
        answer = str(input('Вы уверены в своем заказе ? да/нет '))
        if answer == "да":
            money -= 30
            print(f'У вас осталось денег на карте : {money}\n'
                  f'Вы купили Игрушку № {toy}\n'
                  '1-Игрушка_1\n'
                  '2-Игрушка_2\n'
                  '3-Игрушка_3\n'
                  '4-Игрушка_4\n'
                  '5-Игрушка_5\n'
                  '7-Игрушка_7\n'
                  '8-Игрушка_8\n')
            break
        elif answer == 'нет':
            button_exit = int(input('Нажмите кнопку 1 для выхода'))
            if button_exit == 1:
                print('Всего хорошего')
                break
            else:
                print('Пожалуйста нажмите 1')
                continue





























































