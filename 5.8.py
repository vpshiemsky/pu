class Complex_Number:
    def __init__(self,a,b,*args):
        self.a=a
        self.b=b
        self.z = 'a + b * i'

        def __add__(self, other):
            print(f'Сумма z1 и z2 равна')
            return f'z = {self.a + other.a} + {self.b + other.b} * i'

        def __mul__(self, other):
            print(f'Произведение z1 и z2 равно')
            return f'z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

        def __str__(self):
            return f'z = {self.a} + {self.b} * i'


z_1 = Complex_Number(1, -2)
z_2 = Complex_Number(3, 4)
print(z_1)
print(f'{z_1 + z_2}')
print(f'{z_1 * z_2}')