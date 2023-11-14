class Animal:
    def __init__(self,color,predator,weight,hight,name_pet):
        self.color=color
        self.predator=predator
        self.weight=weight
        self.hight=hight
        self.name_pet=name_pet

    def eating(self,meal):
        return f'Это животное употребляет{meal}'

    def __str__(self):
        return (f'{self.color}\n'
                f'{self.predator}\n'
                f'{self.weight}\n'
                f'{self.name_pet}')

class Mammal(Animal):
    def __init__(self, color, predator, weight, hight, name_pet,home_pet):
        super().__init__(color, predator, weight, hight, name_pet)
        self.home_pet=home_pet
    def __str__(self):
        return super().__str__()+f'\n {self.home_pet}'

class Reptilie(Animal):
    def __init__(self, color, predator, weight, hight, name_pet,toxic):
        super().__init__(color, predator, weight, hight, name_pet)
        self.toxic=toxic
    def __str__(self):
        return super().__str__()+f'\n {self.toxic}'

bear=Mammal(color='коричневый',predator=True,weight=300,hight=2.20,name_pet='Миша',home_pet=False)
goat=Mammal(color='желтый',predator=False,weight=50,hight=1.30,name_pet='Нюся',home_pet=True)
crocodile=Reptilie(color='зеленый',predator=True,weight=200,hight=0.30,name_pet='Гена',toxic=False)


