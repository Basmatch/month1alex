class Sport:
    def __init__(self, name, rules, techniques, tactics, uniform):
        self.name = name
        self.rules = rules
        self.techniques = techniques
        self.tactics = tactics
        self.uniform = uniform
    def go_to_champion_ship(self,medal):
        return (f'эта медаль для {self.name}-{medal}')

    def __str__(self):
        return (f'{self.name}\n'
                f'{self.rules}\n'
                f'{self.techniques}\n'
                f'{self.tactics}\n'
                f'{self.uniform}')

sport_1 = Sport(name='judo',rules='wrestling',techniques='trows',tactics='atack',uniform='kimono' )
sport_2 = Sport(name='box',rules='strike',techniques='blows',tactics='protection',uniform='rashguard')
print(f'{sport_1}\n--------\n{sport_2}')
print(sport_1.go_to_champion_ship(1))





