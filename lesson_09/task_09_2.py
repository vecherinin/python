# Реализовать класс Road (дорога).
# Техническое задание:
# 1. определить атрибуты: length (длина), width (ширина)
# 2. значения атрибутов должны передаваться при создании экземпляра класса
# 3. атрибуты сделать защищёнными
# 4. определить метод расчёта массы асфальта, необходимого для покрытия всей дороги
#     1. метод возвращает массу асфальта
#     2. формула длина * ширина * масса асфальта для покрытия одного кв. метра дороги асфальтом,
#     толщиной в 1 см * число см толщины полотна;
# 5. проверить работу метода и вывести массу асфальта для 2-3 наборов параметров.
#
# Примеры/Тесты:
# 20 м*5000 м*25 кг*5 см = 12500 т

class Road:
    def __init__(self, _width, _length):
        self._width = _width
        self._length = _length

class Count_Mass(Road):
    __kg_per_square = 25  # масса 1 кв. м. асфальта толщиной 1 см
    def __init__(self, _width, _length, _thickness):
        super().__init__(_width, _length)
        self.thickness = _thickness
        # Масса 1 кв. м. заданной толщины
        self.square_mass = self.thickness * self.__kg_per_square

    def mass(self):
        text = f"{self._width} м * {self._length} м * {self.__kg_per_square} кг * {self.thickness} cм"
        result = self._width * self._length * self.square_mass // 1000
        return f"{text} = {result} т"


road_1 = Count_Mass(20, 5000, 5)
road_2 = Count_Mass(24, 4500, 6)
road_3 = Count_Mass(18, 6327, 4)
print(road_1.mass())
print(road_2.mass())
print(road_3.mass())
