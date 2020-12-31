class Matrix :
    def __init__(self,spisok_1,spisok_2):
        self.spisok_1=spisok_1
        self.spisok_2=spisok_2
    def __add__(self,spisok_1,spisok_2,matr):
        super().__init__(spisok_1,spisok_2,matr)
        matr=  [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
        for i in range(len(self.spisok_1)):
            for k in range(len(self.spisok_2)):
                matr[i][k]=self.spisok_1[i][k]+self.spisok_2[i][k]
        return matr
    def __str__(self):


        return ('\t'.join(str[k] for k in i)for i in matr)
my_matrix = Matrix([[1, 18, 11],
                    [6, 17, 23],
                    [41, 50, 9]],
                   [[2, 8, 2],
                    [1, 7, 93],
                    [7, 5, 97]])
print(my_matrix)
# не знаю что тут делать.....