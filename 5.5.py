def summ():
    try:
        with open('ok3.txt', 'w+') as file:
            line = input('Введите числа через пробел : \n')
            file.writelines(line)
            numb = line.split()

            print(sum(map(int, numb)))
    except ValueError:
        print('Это не числа')


summ()
