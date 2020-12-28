class Car:
    def __init__(self,speed,color,name,is_police):
        self.speed=speed
        self.color=color
        self.name=name
        self.is_police=is_police
    def go(self):
        return f'{self.name} поехал(-а)'
    def stop(self):
        return f'{self.name} остановился(-ась)'

    def turn_right(self):
        return f'{self.name} повернулся(-ась) вправо'

    def turn_left(self):
        return f'{self.name} повернулся(-ась) влево'

    def show_speed(self):
        return f'Скорость {self.name} сейчас : {self.speed}'

class TownCar(Car):
    def __init__(self,speed,color,name,is_police):
        super().__init__(speed,color,name,is_police)
    def show_speed(self):
        print(f'Скорость {self.name} сейчас: {self.speed}')
        if self.speed>60:
            print(f'У {self.name} превышение скорости ')

class SportCar(Car):
    def __init__(self,speed,color,name,is_police):
        super().__init__(speed,color,name,is_police)

class WorkCar(Car):
    def __init__(self,speed,color,name,is_police):
        super().__init__(speed,color,name,is_police)
    def show_speed(self):
        print(f'Скорость {self.name} сейчас - {self.speed}')
        if self.speed>40:
            print(f'У {self.name} превышение скорости')

class PoliceCar(Car):
    def __init__(self,speed,color,name,is_police):
        super().__init__(speed,color,name,is_police)
    def police(self):
        if self.is_police:
           return f'{self.name}+'#не знаю что тут писать
        else:
            return f'{self.name}-'
bmv=SportCar(190,'black','bmw',False)
audi=TownCar(50,'black','audi',False)
zhiguli=WorkCar(45,'black','zhiguli',True)
uazik=PoliceCar(100,'black','uazik',True)
print(bmv.go())
print(f'{audi.stop()},когда {bmv.go()}')
print(f'{zhiguli.turn_left()},когда {uazik.turn_right()}')
print(f'Цвет {audi.name}-{audi.color}')
print(f'{uazik.name} полиция?{uazik.is_police}')
print(zhiguli.show_speed())
print(bmv.show_speed())
print(f'Цвет {audi.name}-{audi.color}')
#Только в методе show speed после вывода скорости пишется None,мне это не нравится
