# Реализовать
# функцию, принимающую
# два
# числа(позиционные
# аргументы) и
# выполняющую
# их
# деление.Числа
# запрашивать
# у
# пользователя, предусмотреть
# обработку
# ситуации
# деления
# на
# ноль.
a=int(input())
b=int(input())
def delenie(a,b):
    if b == 0:
        try:
            a / 0
        except ZeroDivisionError:
            print('Деление на 0')
            exit(0)
    else:
        c=a/b
    return c
print(delenie(a,b))