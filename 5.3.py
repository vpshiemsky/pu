def func():
    sum=0
    f=True
    while f==1:
        a=input('Введите число (G-выход) ').split()
        result=0
        for el in range(len(a)):
            if a[el]=='G' or a[el]=='g':
                print('Вы вышли из программы ')
                exit(0)


            else:
                result=result+int(a[el])
        sum=sum+result
        print(f'Сумма сейчас {result}')
        print(f'Общая сумма {sum}')






func()
