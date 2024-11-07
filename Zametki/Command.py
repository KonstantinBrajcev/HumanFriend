from Manager import NoteManager
from Animals import Dog
from Animals import Cat
from Animals import Hamster
from Animals import Horse
from Animals import Camel
from Animals import Donkey

manager = NoteManager()


class Command:

    def __init__(self, file_path):  # ИНИЦИАЛИЗАЦИЯ запросов команд
        self.file_path = file_path

    def add(self, counter):  # ДОБАВЛЕНИЕ нового животного
        animal_type = input(
            "Введите тип животного (Dog, Cat, Hamster, Horse, Camel, Donkey): ")
        name = input("Введите имя животного: ")
        birth_date = input("Введите день рождения в формате YYYY-MM-DD: ")
        commands = input("Введите умения через запятую: ")

        if not all([animal_type, name, birth_date, commands]):
            raise Exception("Все поля должны быть заполнены!")

        if animal_type == "Dog":
            animal = Dog(0, name, commands, birth_date,
                         "Dog", "HomeAnimals")
        elif animal_type == "Cat":
            animal = Cat(0, name, commands, birth_date,
                         "Cat", "HomeAnimals")
        elif animal_type == "Hamster":
            animal = Hamster(0, name, commands, birth_date,
                             "Hamster", "HomeAnimals")

        elif animal_type == "Horse":
            animal = Horse(0, name, commands, birth_date,
                           "Horse", "PackAnimals")
        elif animal_type == "Camel":
            animal = Camel(0, name, commands, birth_date,
                           "Camel", "PackAnimals")
        elif animal_type == "Donkey":
            animal = Donkey(0, name, commands, birth_date,
                            "Donkey", "PackAnimals")
        else:
            print("Неверный тип животного!")
            return
        manager.add_note(animal, self.file_path)
        counter.add()

    def delete(self):  # УДАЛЕНИЕ животного из JSON
        id_to_del = input(f"Введите ID удаляемой записи: ")
        manager.del_from_json(id_to_del, self.file_path)

    def edit(self):  # РЕДАКТИРОВАНИЕ животного
        id_to_edit = input(f"Введите ID редактируемой записи: ")
        if manager.check_existence(id_to_edit, self.file_path):
            new_name = input("Новое имя: ")
            new_commands = input("Новые умения: ")
            new_birth_date = input("Новое день рождение: ")
            manager.edit_from_json(id_to_edit, new_name,
                                   new_commands, new_birth_date, self.file_path)
        else:
            NoteManager.print_none(self, id_to_edit)

    def read_all(self):  # ЧТЕНИЕ животных из JSON
        manager.read_all_from_json(self.file_path)

    def read_nom(self):  # ЧТЕНИЕ живонтого из JSON
        nom_id = input("Введи ID записи: ")
        manager.read_nom_from_json(nom_id, self.file_path)
