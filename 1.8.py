class Data:
    def __init__(self,day_month_year):
        self.day_month_year=str(day_month_year)
    @classmethod
    def first(cls, day_month_year):
        data=[]
        for i in day_month_year.split():
            if i!= '-':
                data.append(i)
        return int(data[0]),int(data[1]),int(data[2])
    @staticmethod
    def valid(day,month,year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2019 >= year >= 0:
                    return f'Все хорошо'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'
    def __str__(self):
        return f'Текущая дата : {Data.first(self.day_month_year)}'
today=Data('13 - 1 - 2021')
print(today)
print(today.first('13 - 1 - 2021'))
print(Data.valid(13,1,2021))
print(Data.first('26 - 5 - 2015'))
print(Data.valid(26,5,2015))







