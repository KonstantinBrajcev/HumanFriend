import Print
import json
from Animals import Dog
from Animals import Cat
from Animals import Hamster
from Animals import Horse
from Animals import Camel
from Animals import Donkey
from Note import Note
from FileManager import FileManager


class NoteManager:

    def __init__(self):  # ИНИЦИАЛИЗАЦИЯ выполнения команд
        self.notes = []

    def read_all_from_json(self, file_path):  # Читаем животных из JSON
        data = FileManager.read_data(file_path)
        if data:
            for note in data:
                animal = self.get_animal_instance(note)
                print(str(animal))  # Печать через ПРЕДКА
        else:
            Print.print_none(self, "записи")

    def add_note(self, animal, file_path):
        data = FileManager.read_data(file_path)  # считываем
        max_id = max([note['note_id'] for note in data], default=0)
        max_id += 1  # Новый номер
        new_note = animal
        new_note.note_id = max_id
        new_note.animal_type = new_note.__class__.__name__
        new_note.parent_class = new_note.__class__.__bases__[0].__name__
        self.notes.append(new_note)
        data = FileManager.read_data(file_path)
        data.append(new_note.__dict__)
        FileManager.write_data(data, file_path)

        # Печать через ПРЕДКА+
        Print.print_new(self, max_id, new_note, file_path)

    def read_nom_from_json(self, nom_id, file_path):  # Читаем животных из JSON
        nom_id = int(nom_id)
        if self.check_existence(nom_id, file_path):
            data = FileManager.read_data(file_path)
            note_found = False
            self.notes = [Note(**note) for note in data]
            for note in self.notes:
                if note.note_id == nom_id:
                    Print.print_nom(self, note)  # Печать через НОТУ+
                    note_found = True
            if not note_found:
                Print.print_none(self, nom_id)
        else:
            Print.print_none(self, nom_id)

    def del_from_json(self, id_to_del, file_path):
        id_to_del = int(id_to_del)  # Преобразование в целое число
        if self.check_existence(id_to_del, file_path):
            data = FileManager.read_data(file_path)
            data = [note for note in data if note['note_id'] != id_to_del]
            FileManager.write_data(data, file_path)
            Print.print_del(self, id_to_del)
        else:
            Print.print_none(self, id_to_del)

    def edit_from_json(self, id_to_edit, new_name, new_commands, new_birth_date, file_path):
        id_to_edit = int(id_to_edit)  # Преобразование в целое число
        data = FileManager.read_data(file_path)
        edit_note = None
        for note in data:
            if note['note_id'] == id_to_edit:
                note['name'] = new_name
                note['commands'] = new_commands
                note['birth_date'] = new_birth_date
                edit_note = Note(
                    note['note_id'], note['name'], note['commands'],
                    note['birth_date'], note['animal_type'], note['parent_class'])
                break
        FileManager.write_data(data, file_path)
        Print.print_edit(self, edit_note)  # Печать через НОТУ+

    def check_existence(self, id_to_edit, file_path):
        data = FileManager.read_data(file_path)
        for note in data:
            if note['note_id'] == int(id_to_edit):
                return True
        return False

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
