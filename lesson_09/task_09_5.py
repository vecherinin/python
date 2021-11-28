# Реализовать класс Stationery (канцелярская принадлежность).
# Техническое задание:
#     1. атрибут title (название)
#     2. метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
#     3. создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
#         1. в каждом классе реализовать переопределение метода draw.
#         Для каждого класса метод должен выводить уникальное сообщение;
#     4. создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    # Атрибуты класса
    def __init__(self, title):
        self.title = title  # Название

    # Методы класса:
    def draw(self):
        return f'Запуск отрисовки'

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Выбрано для отрисовки: {self.title}. Запуск отрисовки.'

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Выбрано для отрисовки: {self.title}. Запуск отрисовки.'

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Выбрано для отрисовки: {self.title}. Запуск отрисовки.'

pen = Pen('ручка')
pencil = Pencil('карандаш')
handle = Handle('маркер')

print(pen.draw())
print(pencil.draw())
print(handle.draw())
