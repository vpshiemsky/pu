class Stationery:
    def __init__(self,title):
        self.title=title
    def draw(self):
        return f'Запуск отрисовки{self.title}'

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return f'Вы выбрали {self.title}. Отрисовка Ручкой'
class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return f'Вы выбрали {self.title}. Отрисовка Карандашом'
class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return f'Вы выбрали {self.title}. Отрисовка Маркером'
pen=Pen('Ручка')
pencil=Pencil('Карандаш')
handle=Handle('Маркер')
print(pen.draw())
print(pencil.draw())
print(handle.draw())
