import json
profit={}
prof_average=0
prof=0
i=0
with open('ok5.txt','r') as file:
    for line in file:
        name,company,earn,minus=line.split()
        profit[name]=int(earn)-int(minus)
        if profit[name]>=0:
            prof=prof+profit.setdefault(name)
            i+=1
        if i!=0:
            prof_average=prof/i
            print(f'Средняя прибыль : {prof_average}')
        else:
            print(f'Средняя прибыль остутствует')
        pr = {'средняя прибыль': round(prof_average)}
# дальше я не знаю что с этим делать
