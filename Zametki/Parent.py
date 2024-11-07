from os import name
from Print import Print


class ParentAnimal:
    class_name = "ParentAnimal"

    def __init__(self, note_id, name, commands, birth_date):
        self.name = name
        self.commands = commands
        self.birth_date = birth_date
        self.note_id = note_id

    def __str__(self):
        return Print.record(self.note_id, self.name, self.commands,
                            self.birth_date, self.__class__.__name__,
                            self.__class__.__bases__[0].__name__)
    # f"ID: {self.note_id}\t Тип: {self.__class__.__name__}\t Родитель: {self.__class__.__bases__[0].__name__}\t Имя: {self.name}\t День рождения: {self.birth_date}\t Умения: {self.commands}"


class HomeAnimals(ParentAnimal):
    class_name = "HomeAnimal"

    def __init__(self, note_id, name, commands, birth_date, animal_type, parent_class):
        super().__init__(note_id, name, commands, birth_date)
        self.animal_type = animal_type
        self.parent_class = parent_class

    def __str__(self):
        # return super().__str__() + f"\t Тип животного: {self.animal_type}\t Родительский класс: {self.parent_class}"
        return super().__str__()


class PackAnimals(ParentAnimal):
    class_name = "PackAnimal"

    def __init__(self, note_id, name, commands, birth_date, animal_type, parent_class):
        super().__init__(note_id, name, commands, birth_date)
        self.animal_type = animal_type
        self.parent_class = parent_class

    def __str__(self):
        # return super().__str__() + f"\t Тип животного: {self.animal_type}\t Родительский класс: {self.parent_class}"
        return super().__str__()
