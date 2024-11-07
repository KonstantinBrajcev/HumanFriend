import json


class FileManager:
    @staticmethod  # ОТКРЫТИЕ файла в режиме ЧТЕНИЯ
    def read_data(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    @staticmethod  # ОТКРЫТИЕ файла в режиме ЗАПИСИ
    def write_data(data, file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
