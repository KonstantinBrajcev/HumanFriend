class Counter:
    def __init__(self):
        self.count = 0

    def add(self):
        self.count += 1

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None and self.count > 0:
            print(f"Количество добавленных животных: {self.count}")
        else:
            print("Ошибка при работе с объектом Counter!")
        return True
