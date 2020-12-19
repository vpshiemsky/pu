from itertools import count
from math import factorial
def generator():
    for el in count(1):
        yield factorial(el)
fact=generator()
x=0
for el in fact:
    if x<10:
        print(el)
        x+=1
    else:
        exit(0)
# цикл бесконечный => сделал чтобы выводились факториалы до 10