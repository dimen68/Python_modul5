# Задача "Developer - не только разработчик"

class House:
    def __init__(self, name, floors):
        self.name = name
        self.number_of_floors = floors


    def go_to(self, new_floor):
        if  1 > new_floor or new_floor > self.number_of_floors:
            print(f'\n Такого этажа ({new_floor}) не существует, так как в доме "{self.name}" всего {self.number_of_floors} этажей.')
        else:
            for i in range(1, new_floor + 1):
                print(f'этаж {i}')


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)