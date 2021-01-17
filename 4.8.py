class Sklad:
    def __init__(self,name,quantity,price,numb,*args):
        self.name=name
        self.quantity=quantity
        self.price=price
        self.numb=numb
        self.store_full=[]
        self.store=[]
        self.unit={'Модель устройства ': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}
    def __str__(self):
        return f'Название - {self.name}, Цена - {self.price} ,Количество - {self.quantity}'
    def reception(self):
        try:
            union=input('Введите наименование : ')
            union_p=int(input('Введите цену : '))
            union_q=int(input('Введите количество : '))
            unique=print(f'Модель устройства - {union} ,Цена за ед. - {union_p}, Количество - {union_q}')
            self.unit.update(unique)
            print(f'Текущий список - {self.store}')
        except:
            return f'Ошибка'
class Printer(Sklad):
    def t_print(self):
        return f'Распечатано {self.numb} раз'
class Scanner(Sklad):
    def t_scan(self):
        return f'Сканировано {self.numb} раз'
class Copy(Sklad):
    def t_copy(self):
        return f'Копировано {self.numb} раз'
unit_1=Printer('HP',2000,1,1)
unit_2=Scanner('Xerox',3500,3,2)
unit_3=Copy('Canon',7000,1,6)
print(unit_1.t_print())
print(unit_2.t_scan())
print(unit_1.reception())