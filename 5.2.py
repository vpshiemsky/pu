my_list = [7, 5, 3, 3, 2]
print(f'Рейтинг {my_list}')
a=int(input('Введите число : '))
for el in range(len(my_list)):
    if my_list[el]==a:
        my_list.insert(0,a)
        break
    elif my_list[0]<a:
        my_list.insert(0,a)
    elif my_list[-1]<a:
        my_list.append(a)
    elif my_list[el]>a and my_list[el+1]<a  :
        my_list.insert(el+1,a)
print(f'Текущий список {my_list}')

#вроде все работает,но для 4 получается что то непонятное
#я вижу ,что ошибка в 10-11 строках ,но не знаю как исправить