from sys import argv
try:
    time,salary,bonus=argv,argv,argv

    time=int(input())
    salary=int(input())
    bonus=int(input())
    result=time*salary+bonus
    print(f'Зарплата сотрудника : {result}')
except ValueError:
    print(f'Не числа')
