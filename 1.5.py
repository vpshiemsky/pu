file=open('text.txt','w')
tekst=input('Введите текст : \n')
while tekst:
    file.writelines(tekst)
    tekst= input('Введите текст : \n')
    if not tekst:
        break
file.close()

file=open('text.txt','r')
content=file.readlines()
print(content)
file.close()
