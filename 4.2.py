strk=(input('Введите несколько слов : '))
word=[]
num=1
for el in range(strk.count('')):
    word=strk.split()
    if len(str(strk))<=10:
        print(f'{num} {word[el]}')
        num+=1
    else:
        print(f'{num} {word[el] [0:10]}')
        num+=1

# все ок,но после 1 строчки выдает ошибку








