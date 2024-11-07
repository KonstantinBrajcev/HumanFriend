from os import name


class ParentAnimal:
    class_name = "ParentAnimal"

    def __init__(self, note_id, name, commands, birth_date):
        self.name = name
        self.commands = commands
        self.birth_date = birth_date
        self.note_id = note_id

    def __str__(self):
        return f"ID: {self.note_id}\t Тип: {self.__class__.__name__}\t Родитель: {self.__class__.__bases__[0].__name__}\t Имя: {self.name}\t День рождения: {self.birth_date}\t Умения: {self.commands} ПРЕДОК"


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
