rus={'One':'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file=[]
with open('okkk.txt','r',encoding='utf-8') as file :
    for i in file:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + '' + i[1])
    print(new_file)
with open('ok2.txt','w') as file_2:
    file_2.writelines(new_file)