class Delenie:
    def __init__(self,delitel,delimoe):
        self.delitel=delitel
        self.delimoe=delimoe
    @staticmethod
    def error(delitel,delimoe):
        try:
            return (delitel/delimoe)
        except ZeroDivisionError:
            return f'Деление на 0 '
a=Delenie
print(a.error(5,0))
print(a.error(10,6))

