class Textil:
    def __init__(self,v,h):
        self.v=v
        self.h=h
    def c(self):
        return {self.v}/6.5+0,5
    def k(self):
        return {self.h}*2+0,3
    @property
    def full(self):
        return str(f'Общая площадь \t:{self.v+self.h}')
class Coat(Textil):
    def __init__(self,v,h):
        super().__init__(v,h)
        self.c=round(self.v/6.5+0,5)
    def __str__(self):
        return f'Площадь на пальто : {self.c}'
class Jacket(Textil):
    def __init__(self,v,h):
        super().__init__(v,h)
        self.k=round(self.h*2+0,3)
    def __str__(self):
        return f'Площадь на костюм : {self.k}'
coat=Coat(2,4)
jacket=Jacket(1,2)
print(coat)
print(jacket)
print(coat.full)
print(jacket.full)
print(coat.c)
print(jacket.k)