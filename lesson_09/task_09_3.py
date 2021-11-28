# Реализовать базовый класс Worker (работник).
# Техническое задание:
#     1. определить атрибуты: name, surname, position (должность), income (доход)
#     2. атрибут income должен быть защищённым и ссылаться на словарь, содержащий элементы:
#     оклад и премия, например, {"wage": wage, "bonus": bonus}
#     3. При создании экземпляра параметры wage, bonus передаются как числа.
#     4. создать класс Position (должность) на базе класса Worker. Это наследование.
#     5. в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
#     и дохода с учётом премии (get_total_income)
#     6. проверить работу примера на реальных данных:
#     - создать экземпляры класса Position,
#     - передать данные,
#     - проверить значения атрибутов,
#     - вызвать методы экземпляров.

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return f'{sum(self._income.values())}'


p1 = Position('Иван', 'Иванов', 'хормейстер', 50000, 15000)

print(p1.get_full_name())
print(p1.position)
print(p1.get_total_income())

p2 = Position('Антон', 'Антонов', 'дирижёр оркестра', 21000, 87000)
print(f'\nПолное имя: {p2.get_full_name()}')
print(f'Имя: {p2.name}')
print(f'Фамилия: {p2.surname}')
try:
    print(f'Премия: {p2.bonus}')
except AttributeError:
    print('Премия: нет доступа к данным. Данные защищены!')
print(f'Доход: {p2.get_total_income()}')
