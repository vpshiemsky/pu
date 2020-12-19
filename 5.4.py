from functools import reduce
def func(prev_el,el):
    return prev_el*el
print(f'Списко четных значений : {[el for el in range(99,1001) if el %2==0]}')
print(f'Перемноженные числа : {reduce(func, [el for el in range(99, 1001) if el % 2 == 0])}')
#мне кажется во 2 принте ошибка но не знаю как исправить