a=float(input('Введите значение выручки : '))
b=float(input('Введите значение издержки : '))
c=int(input('Введите численность сотрудников фирмы : '))
d=(a-b)/c
if a>b:
    print(f'Прибыль : {a-b}')
    print(f'Прибыль на одного сотрудника : {d:.2f}')
else :
    print(f'Убыток :{b-a}')
