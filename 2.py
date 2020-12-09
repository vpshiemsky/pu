a=int(input('Введите время в секуданх: '))
hours=a//3600
minutes=(a-hours*3600)//60
seconds=a-(hours*3600+minutes*60)
print(f'Время в формате чч:мм:сс {hours} : {minutes} : {seconds}')

