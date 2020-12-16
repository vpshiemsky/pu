# Реализовать
# функцию
# my_func(), которая
# принимает
# три
# позиционных
# аргумента, и
# возвращает
# сумму
# наибольших
# двух
# аргументов.
def my_func(a,b,c):
    if a>=c and b>=c:
        return a+b
    elif a>=c and b<=c:
        return a+c
    else:
        return b+c
print(my_func(int(input('Первое число ')),int(input('Второе число ')),int(input('Третье число '))))
