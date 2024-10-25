# Задача "Магические здания"

class House:
    def __init__(self, name, floors):
        self.name = name
        self.number_of_floors = floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return 'Название: ' + str(self.name) + ', кол-во этажей: ' + str(self.number_of_floors)

    def go_to(self, new_floor):
        if 1 > new_floor or new_floor > self.number_of_floors:
            print(
                f'\n Такого этажа ({new_floor}) не существует, так как в доме "{self.name}" всего {self.number_of_floors} этажей.')
        else:
            for i in range(1, new_floor + 1):
                print(f'этаж {i}')


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))