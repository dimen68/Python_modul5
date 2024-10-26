# Задача "Нужно больше этажей"
def is_int(value):
    return isinstance(value, int)


def is_class_house(other):
    return isinstance(other, House)


class House:
    def __init__(self, name, floors):
        self.name = name
        self.number_of_floors = floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return 'Название: ' + str(self.name) + ', кол-во этажей: ' + str(self.number_of_floors)

    def __eq__(self, other):
        if is_class_house(other):
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        if is_class_house(other):
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if is_class_house(other):
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if is_class_house(other):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if is_class_house(other):
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if is_class_house(other):
            return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if is_int(value):
            self.number_of_floors += value
            return self

    def __radd__(self, value):
        if is_int(value):
            self.number_of_floors += value
            return self

    def __iadd__(self, value):
        if is_int(value):
            self.number_of_floors += value
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
    h2 = House('ЖК Акация', 20)

    print(h1)
    print(h2)

    print(h1 == h2)  # __eq__

    h1 = h1 + 10  # __add__
    print(h1)
    print(h1 == h2)

    h1 += 10  # __iadd__
    print(h1)

    h2 = 10 + h2  # __radd__
    print(h2)

    print(h1 > h2)  # __gt__
    print(h1 >= h2)  # __ge__
    print(h1 < h2)  # __lt__
    print(h1 <= h2)  # __le__
    print(h1 != h2)  # __ne__

    # проверка неизменности функций для целых чисел (класс int)
    print('\n***Проверка неизменности мат.функций для целых чисел (класс int)***')
    a = 6
    b = 7
    print(a + b)
    print(a > b)
    print(a < b)
    print(a == b)
