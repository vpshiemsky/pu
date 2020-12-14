a=int(input('Введите количество элементов списка:'))
spisok=[]
i=0
el=0
while i< a:
    spisok.append(input('Введите значение списка:'))
    i+=1
for elements in range(int(len(spisok)/2)):
    spisok[el+1],spisok[el]=spisok[el],spisok[el+1]
    el+=2
print(spisok)