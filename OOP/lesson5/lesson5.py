class Mersedes_C220_202:
    def __init__(self, color, fuel, kuz0v, year):
        self.color = color
        self.fuel = fuel
        self.kuzov = kuz0v
        self.year = year

    def comfort(self, yes_no):
        return f'данная машина имеет комфорffffffт {yes_no}'

    def __str__(self):
        return (f'{self.color}\n'
                f'{self.fuel}\n'
                f'{self.kuzov}\n'
                f'{self.year}')


mersedes = Mersedes_C220_202(color='серый', fuel='disel', kuz0v='universal', year=1997)
mersedes.comfort(True)


class Merse____des_C220_203(Mersedes_C220_202):
    def __init__(self, color, fuel, kuz0v, year, sdi, abs):
        super().__init__(color, fuel, kuz0v, year)
        self.sdi = sdi
        self.abs = abs

    def econom(self,yes_no):
        return f'данная машина экономичная{yes_no}'



    def __str__(self):
        return super().__str__() + (f'\n{self.sdi}\n'
                                    f'\n{self.abs}'

                                    )
mersedes = Mersedes_C220_203(color='белый',fuel='disel',kuz0v='univeresal',year=2003,sdi=True,abs=True)
mersedes.econom(True)
mersedes.comfort(True)


class Mersedes_C220_204(Mersedes_C220_203):
    def __init__(self, color, fuel, kuzov, year,esp,4_matic):
        super().__init__(color,fuel,kuzov,year)
        self.esp = esp
        self.4_matic = 4_matic

    def good_handling(self,yes_no):
        return f'данная машина хорошо управляется{yes_no}'

    def __str__(self):
        return super().__str__() + (f'\n{self.esp}\n'
                                    f'\n{self.4_matic}')

mersedes = Mersedes_C220_204(color='синий',fuel='diesel',kuzov='universal',year=2008,esp=True,4_matic=True)
mersedes.comfort(True)
mersedes.good_handling(True)