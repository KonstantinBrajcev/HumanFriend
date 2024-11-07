from Animals import Dog, Cat, Hamster, Horse, Camel, Donkey
from Manager import NoteManager


class Command:

    def __init__(self, file_path):  # ИНИЦИАЛИЗАЦИЯ запросов команд
        self.file_path = file_path
        from Manager import NoteManager
        self.manager = NoteManager(file_path)

    def add(self, counter):  # ДОБАВЛЕНИЕ нового животного
        animal_type = input(
            "Введите тип животного (Dog, Cat, Hamster, Horse, Camel, Donkey): ")
        name = input("Введите имя животного: ")
        birth_date = input("Введите день рождения в формате YYYY-MM-DD: ")
        commands = input("Введите умения через запятую: ")

        if not all([animal_type, name, birth_date, commands]):
            raise Exception("Все поля должны быть заполнены!")

        # Создание экземпляра животного
        animal_classes = {
            "Dog": Dog,
            "Cat": Cat,
            "Hamster": Hamster,
            "Horse": Horse,
            "Camel": Camel,
            "Donkey": Donkey
        }

        if animal_type in animal_classes:
            animal = animal_classes[animal_type](0, name, commands, birth_date, animal_type, "HomeAnimals" if animal_type in [
                                                 "Dog", "Cat", "Hamster"] else "PackAnimals")
            self.manager.add_note(animal)
            counter.add()
        else:
            print("Неверный тип животного!")

    def delete(self):  # УДАЛЕНИЕ животного из JSON
        id_to_del = input(f"Введите ID удаляемой записи: ")
        self.manager.del_from_json(id_to_del)

    def edit(self):  # РЕДАКТИРОВАНИЕ животного
        id_to_edit = input(f"Введите ID редактируемой записи: ")
        # Загружаем существующие записи
        self.manager.load_notes()
        # Получаем старые данные
        old_animal_data = self.manager.find_note_by_id(int(id_to_edit))

        if old_animal_data:
            # old_animal = Note(**old_animal_data)
            # Выводим старые данные
            print(f"----- Старые данные животного: -----")
            print(f"Имя: {old_animal_data['name']}")
            print(f"Умения: {old_animal_data['commands']}")
            print(f"Дата рождения: {old_animal_data['birth_date']}")
            print(f"----- Новые данные животного: -----")
            # Запрашиваем новые данные
            new_name = input(
                "Новое имя (оставьте пустым, чтобы не менять): ") or old_animal_data['name']
            new_commands = input(
                "Новые умения (оставьте пустым, чтобы не менять): ") or old_animal_data['commands']
            new_birth_date = input(
                "Новая дата рождения (оставьте пустым, чтобы не менять): ") or old_animal_data['birth_date']

            self.manager.edit_from_json(
                id_to_edit, new_name, new_commands, new_birth_date)
            print(f"Запись {id_to_edit} успешно обновлена!")
        else:
            print("Запись не найдена.")

    def read_all(self):  # ЧТЕНИЕ животных из JSON
        self.manager.read_all_from_json()

    def read_nom(self):  # ЧТЕНИЕ живонтого из JSON
        nom_id = input("Введи ID записи: ")
        self.manager.read_nom_from_json(nom_id)
