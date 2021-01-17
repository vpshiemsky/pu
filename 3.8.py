class Count:
    def __init__(self,*args):
        self.spisok=[]
    def check(self):
        while True:
            try:
                chislo=int(input('Введите значения : '))
                self.spisok.append(chislo)
                print(f'Текущий список : {self.spisok}')
            except:
                print(f'Недопустимое значение : число и буква')
                poisk=input('Продолжить? Y/N ')
                if poisk=='Y' or poisk=='y':
                    print(a.check())
                elif poisk=='N' or poisk=='n':
                    print('Вы вышли')
                return f'Вы вышли'
a=Count(1)
print(a.check())



