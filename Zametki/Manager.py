from Animals import Dog, Cat, Hamster, Horse, Camel, Donkey
from FileManager import FileManager
from Note import Note
import Print


class NoteManager:

    def __init__(self, file_path):
        # ИНИЦИАЛИЗАЦИЯ выполнения команд
        self.file_path = file_path
        self.notes = []

    def load_notes(self):
        # Загружаем данные из файла
        self.notes = FileManager.read_data(self.file_path)

    def save_notes(self):
        # Сохраняем данные в файл
        FileManager.write_data(self.notes, self.file_path)

    def find_note_by_id(self, note_id):
        # ПОиск записи по ID
        for note in self.notes:
            if note['note_id'] == note_id:
                return note
        return None

    def read_all_from_json(self):
        # Читаем животных из JSON
        self.load_notes()  # Загружаем записи из файла
        if self.notes:
            for note in self.notes:
                animal = self.get_animal_instance(note)
                print(str(animal))  # Выводим запись
        else:
            Print.print_none(self, "записи")  # Выводим запись

    def add_note(self, animal):
        # Добавление новой записи
        max_id = max([note['note_id']
                     for note in self.notes], default=0) + 1  # Новый номер
        animal.note_id = max_id
        self.notes.append(animal.__dict__)
        self.save_notes()  # Записываем данные
        Print.print_new(self, max_id, animal, self.file_path)  # Выводим запись

    def read_nom_from_json(self, nom_id):  # Читаем животных из JSON
        note_found = self.find_note_by_id(int(nom_id))
        if note_found:
            Print.print_nom(self, Note(**note_found))  # Выводим запись
        else:
            Print.print_none(self, nom_id)  # Выводим запись

    def del_from_json(self, id_to_del):
        self.notes = [
            note for note in self.notes if note['note_id'] != int(id_to_del)]
        self.save_notes()  # Записываем данные
        Print.print_del(self, id_to_del)  # Выводим запись

    def edit_from_json(self, id_to_edit, new_name, new_commands, new_birth_date):
        for note in self.notes:
            if note['note_id'] == int(id_to_edit):
                if new_name:
                    note['name'] = new_name
                if new_commands:
                    note['commands'] = new_commands
                if new_birth_date:
                    note['birth_date'] = new_birth_date
                break
        self.save_notes()  # Записываем данные

    def get_animal_instance(self, note_data):
        animal_type = note_data['animal_type']
        parent_class = note_data['parent_class']
        note_id = note_data['note_id']
        name = note_data['name']
        commands = note_data['commands']
        birth_date = note_data['birth_date']
        if animal_type == "Dog":
            return Dog(note_id, name, commands, birth_date, animal_type, parent_class)
        elif animal_type == "Cat":
            return Cat(note_id, name, commands, birth_date, animal_type, parent_class)
        elif animal_type == "Hamster":
            return Hamster(note_id, name, commands, birth_date, animal_type, parent_class)
        elif animal_type == "Horse":
            return Horse(note_id, name, commands, birth_date, animal_type, parent_class)
        elif animal_type == "Camel":
            return Camel(note_id, name, commands, birth_date, animal_type, parent_class)
        elif animal_type == "Donkey":
            return Donkey(note_id, name, commands, birth_date, animal_type, parent_class)
        else:
            return Note(note_id, name, commands, birth_date, animal_type, parent_class)
