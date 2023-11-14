 #         ООП-Объектно-ориентированое-программирование.
 # В ООП центральными являются понятия "Класса" и "Объекта"
 #   "Класс"-абстракция реального мира(обобщенный шаблон),специальный тип данных,описывает
 #           свойства и методы у подобных объектов:
 #    "Объект" - частный случай класса
 # Пример:
 # "Класс"-машины  "Объект"- марки машин(Mercedes,Bmw,Audi) "Атрибуты"(бизнес класс,эконом)


class Car:
    def __init__(self, name, color, volume, car_body,start_year):
        self.name = name
        self.color = color
        self.volume = volume
        self.car_body = car_body
        self.start_year = start_year

    def tunning(self, cost, master):
        return (f'Цена тюнинга - {cost}\n'
                f'Мастер - {master}')

    def review(self, review_cost):
        if review_cost <=10000:
            return f'Эта - {self.name} очень дешевая в обслуживани'
        elif review_cost >=20000:
            return  f'Эта - {self.name} очень дорогая в обслуживании'

    def __str__(self):
        return (f'{self.name}\n'
                f'{self.color}\n'
                f'{self.volume}\n'
                f'{self.car_body}\n'
                f'{self.start_year}')

car_1 = Car(name='BMW', color='black', volume=3.0, car_body='sport', start_year=1997)
print(car_1.tunning(10000,'Nikita'))
car_2 = Car(name='Lexus', color='white', volume=5.0,car_body='jeep', start_year=2023)
print(car_2.tunning(90000,'Maksim'))
print(f'{car_1}\n-------\n{car_2}')
print(car_1.review(int(input(f'скольлко вы заплатили {car_1.name} за месяц обслуживания'))))
print(car_2.review(int(input(f'скольлко вы заплатили {car_2.name} за месяц обслуживания'))))