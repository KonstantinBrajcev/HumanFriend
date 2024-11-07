from Parent import ParentAnimal, HomeAnimals, PackAnimals


class Dog(HomeAnimals, ParentAnimal):
    class_name = "Dog"

    def __init__(self, note_id, name, commands, birth_date, animal_type, parent_class):
        super().__init__(note_id, name, commands, birth_date, animal_type, parent_class)
        self.animal_type = animal_type
        self.parent_class = parent_class


class Cat(HomeAnimals, ParentAnimal):
    class_name = "Cat"

    def __init__(self, note_id, name, commands, birth_date, animal_type, parent_class):
        super().__init__(note_id, name, commands, birth_date, animal_type, parent_class)
        self.animal_type = animal_type
        self.parent_class = parent_class


class Hamster(HomeAnimals, ParentAnimal):
    class_name = "Hamster"

    def __init__(self, note_id, name, commands, birth_date, animal_type, parent_class):
        super().__init__(note_id, name, commands, birth_date, animal_type, parent_class)
        self.animal_type = animal_type
        self.parent_class = parent_class


class Horse(PackAnimals, ParentAnimal):
    class_name = "Horse"

    def __init__(self, note_id, name, commands, birth_date, animal_type, parent_class):
        super().__init__(note_id, name, commands, birth_date, animal_type, parent_class)
        self.animal_type = animal_type
        self.parent_class = parent_class


class Camel(PackAnimals, ParentAnimal):
    class_name = "Camel"

    def __init__(self, note_id, name, commands, birth_date, animal_type, parent_class):
        super().__init__(note_id, name, commands, birth_date, animal_type, parent_class)
        self.animal_type = animal_type
        self.parent_class = parent_class


class Donkey(PackAnimals, ParentAnimal):
    class_name = "Donkey"

    def __init__(self, note_id, name, commands, birth_date, animal_type, parent_class):
        super().__init__(note_id, name, commands, birth_date, animal_type, parent_class)
        self.animal_type = animal_type
        self.parent_class = parent_class
