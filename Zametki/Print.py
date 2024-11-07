class Print:
    @staticmethod
    def record(note_id, name, commands, birth_date, animal_type, parent_class):
        return (f"ID: {note_id}\t Тип: {animal_type}\t Родитель: {parent_class}\t "
                f"Имя: {name}\t День рождения: {birth_date}\t Умения: {commands}")


def print_none(self, nom):
    print("-------------------------\n",
          f"Животное № {nom} не найдено.")


def print_all(self, notes):
    print("-------------------------")
    for note in notes:
        print(str(note))  # Неправильный формат получаемых данных


def print_edit(self, edit_note):
    print("-------------------------\n",
          f"--- Обновленная запись: ---\n{str(edit_note)}")  # переход на НОТУ+


def print_new(self, max_id, new_note, file_path):
    print("-------------------------\n",
          f"Животное № {max_id} записано в файл {file_path}.\n"
          f"{str(new_note)}")  # переход на ПРЕДКА+


def print_nom(self, note):
    print("-------------------------\n",
          f"{str(note)}")  # переход на НОТУ+


def print_del(self, id_to_del):
    print("-------------------------\n",
          f"Животное № {id_to_del} удалено.")
