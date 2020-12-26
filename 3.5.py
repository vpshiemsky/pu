with open('okk.txt','r') as my_file:

    salary=[]
    poor=[]
    spisok=my_file.read().split('\n')
    for i in spisok:
        i=i.split()
        if int(i[1])<20000:
            poor.append(i[0])
        salary.append(i[1])
print(f'Оклад меньше 20000- {poor},средний оклад- {sum(map(int,salary))/len(salary)} ')