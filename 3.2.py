list=['winter','spring','summer','autumn']
d={1:'winter',2:'spring',3:'summer',4:'autumn'}
month=int(input('Введите месяц : '))
if month==1 or month==2 or month==12:
    print(list[0])
    print(d.get(1))

elif month==3 or month==4 or month==5:
    print(list[1])
    print(d.get(2))

elif month==6 or month==7 or month==8:
    print(list[2])
    print(d.get(3))

elif month==9 or month==10 or month==11:
    print(list[3])
    print(d.get(4))
else:
    print('Такого месяца не существует')