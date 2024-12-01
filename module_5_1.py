# Создаем класс House
class House:
    # Определяем метод __init__ для инициализации объекта
    def __init__(self, name, number_of_floors):
        # Установка атрибута self.name с помощью переданного значения name
        self.name = name
        # Установка атрибута self.number_of_floors с помощью переданного значения number_of_floors
        self.number_of_floors = number_of_floors

    # Определяем метод go_to для перехода на определенный этаж
    def go_to(self, new_floor):
        # Проверяем, существует ли указанный этаж
        if 1 <= new_floor <= self.number_of_floors:
            # Выводим все этажи от 1 до new_floor включительно
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            # Выводим сообщение, если этаж не существует
            print("Такого этажа не существует")

# Создаем объект класса House с названием 'ЖК Эльбрус' и 30 этажами
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

# Вызываем метод go_to у созданного объекта для перехода на 5 этаж
h1.go_to(5)
h2.go_to(10)