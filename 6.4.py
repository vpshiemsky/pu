# from itertools import count
# for el in count(int(input('Введите стартовое число : '))):
#     if el>=1000:
#         exit(0)
#     else:
#         print(el)
# специально сделал ограничение тк там бесконечный цикл
from itertools import cycle

list = ['ABC','GBF',123,'No']
for el in cycle(list):
    print(el)