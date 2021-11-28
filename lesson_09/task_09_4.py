# Реализуйте базовый класс Car (машина).
# Техническое задание:
#     1. атрибуты: speed, color, name, is_police(булево). speed - текущая скорость машины.
#     2. методы: go, stop, turn(direction), которые должны сообщать(выводить на экран),
#     что машина поехала, остановилась, повернула (куда). turn(direction) - метод,
#     принимающий параметр: направление поворота.
#     3. опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar
#         1. добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля
#         2. для классов TownCar и WorkCar переопределите метод show_speed.
#         При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#     4. Создайте экземпляры классов, передайте значения атрибутов.
#     Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.


class Car:
    # Атрибуты класса
    def __init__(self, speed, color, name, is_police):
        self.speed = speed  # Текущая скорость
        self.color = color
        self.name = name
        self.is_police = is_police

    # Методы класса
    def go(self):
        return f'Машина {self.name} поехала'

    def stop(self):
        return f'Машина {self.name} оставилась'

    def turn(self, direction):
        if direction == 'L':
            direction = 'налево'
        elif direction == 'R':
            direction = 'направо'
        return f'Машина {self.name} повернула {direction}'

    def show_speed(self):
        return f'Текущая машины {self.name}: {self.speed} км/ч'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f'Машина {self.name} превышает скорость! {self.speed} км/ч'
        else:
            return f'Текущая скорость {self.name}: {self.speed} км/ч'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f'Машина {self.name} превышает скорость! {self.speed} км/ч'
        else:
            return f'Текущая скорость {self.name}: {self.speed} км/ч'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} - машина полиции'
        else:
            return f'{self.name} - не является машиной полиции'


# Задаём атрибуты: speed, color, name, is_police
porsche = SportCar(110, 'чёрный', 'Porsche', False)
miniсooper = TownCar(70, 'синий', 'Mini Cooper', False)
mercedes = WorkCar(50, 'белый', 'Mercedes-Benz', False)
ford = PoliceCar(120, 'белый',  'Ford', True)
bmw = TownCar(90, 'белый',  'BMW', True)

print(f'\nВыполняем доступ к атрибутам:')
print(f'\t{porsche.speed}')
print(f'\t{miniсooper.color}')
print(f'\t{mercedes.name}')
print(f'\t{ford.is_police}')
print(f'\tЦвет машины {ford.name}: {ford.color}')

print(f'\nВызываем методы:')
print(f'\t{porsche.turn("L")}.')
print(f'\t{miniсooper.turn("R")}.')
print(f'\t{mercedes.go()}.\n\t{mercedes.show_speed()}.')
print(f'\t{porsche.show_speed()}.')
print(f'\t{bmw.show_speed()}.')
print(f'\t{ford.show_speed()}.')
