d={}

with open('ok4.txt','r') as file:

    for line in file:
        predmet, lekcia, praktika, lab = line.split()

        d[predmet]=int(lekcia)+int(praktika)+int(lab)

    print(f'Общее клоичество часов : {d}')

