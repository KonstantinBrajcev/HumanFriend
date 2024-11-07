from Print import Print


class Note:
    def __init__(self, note_id, name, commands, birth_date, animal_type, parent_class):
        self.note_id = note_id
        self.name = name
        self.commands = commands
        self.birth_date = birth_date
        self.animal_type = animal_type
        self.parent_class = parent_class

    # Строка для распечатки записей
    def __str__(self):
        return Print.record(self.note_id, self.name, self.commands,
                            self.birth_date, self.animal_type, self.parent_class)
    # f"ID: {self.note_id}\t Тип: {self.animal_type}\t Родитель: {self.parent_class}\t Имя: {self.name}\t День рождения: {self.birth_date}\t Умения: {self.commands}"
