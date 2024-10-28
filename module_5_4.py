# Задача "История строительства"

class House:
    houses_history = []
    total_floors = 0

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        cls.total_floors += args[1]
        return object.__new__(cls)

    def __init__(self, name, floors):
        self.name = name
        self.number_of_floors = floors

    def __del__(self):
        print(f'    {self.name} снесён, но он останется в истории')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return 'Название: ' + str(self.name) + ', кол-во этажей: ' + str(self.number_of_floors)

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        else:
            print(f'Действие невыполнимо, так как классы не одинаковые: {type(self)} и {type(other)}')

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        else:
            print(f'Действие невыполнимо, так как классы не одинаковые: {type(self)} и {type(other)}')

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        else:
            print(f'Действие невыполнимо, так как классы не одинаковые: {type(self)} и {type(other)}')

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        else:
            print(f'Действие невыполнимо, так как классы не одинаковые: {type(self)} и {type(other)}')

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        else:
            print(f'Действие невыполнимо, так как классы не одинаковые: {type(self)} и {type(other)}')

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        else:
            print(f'Действие невыполнимо, так как классы не одинаковые: {type(self)} и {type(other)}')

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        else:
            print(f'Действие невыполнимо, так как классы не одинаковые: {type(self.number_of_floors)} и {type(value)}')
            return self

    def __radd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        else:
            print(f'Действие невыполнимо, так как классы не одинаковые: {type(self.number_of_floors)} и {type(value)}')
            return self

    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        else:
            print(f'Действие невыполнимо, так как классы не одинаковые: {type(self.number_of_floors)} и {type(value)}')
            return self

    def go_to(self, new_floor):
        if 1 > new_floor or new_floor > self.number_of_floors:
            print(
                f'\n Такого этажа ({new_floor}) не существует, так как в доме "{self.name}" всего {self.number_of_floors} этажей.')
        else:
            for i in range(1, new_floor + 1):
                print(f'этаж {i}')


if __name__ == '__main__':
    h1 = House('ЖК Эльбрус', 10)
    print(f'История построенных объектов: {House.houses_history}')
    h2 = House('ЖК Акация', 20)
    print(f'История построенных объектов: {House.houses_history}')
    h3 = House('ЖК Матрёшки', 20)
    print(f'История построенных объектов: {House.houses_history}')

    # Удаление объектов
    print(f'Получен приказ: снести {h2.name} ')
    del h2
    print(f'Получен приказ: снести {h3.name} ')
    del h3

    print(f'История построенных объектов: {House.houses_history}')
    print(f'Всего возведено {House.total_floors} этажей')
    print(f'При закрытии проекта снести оставшиеся объекты')
