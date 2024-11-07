from Command import Command
from Counter import Counter
import os

os.system('clear')  # Очистка консоли
while True:
    file_path = 'notes.json'
    print("-----------МЕНЮ----------",
          "1 -> ДОБАВИТЬ ЖИВОНОЕ",
          "2 -> ВЫВЕСТИ ВСЕХ ЖИВОТНЫХ",
          "3 -> ВЫВЕСТИ ОДНО ЖИВОТНОЕ",
          "4 -> РЕДАКТИРОВАТЬ ЖИВОТНОЕ",
          "5 -> УДАЛИТЬ ЖИВОТНОЕ",
          "0 -> ВЫХОД",
          "-------------------------",
          sep='\n')
    command = input("Введите № меню: -> ")
    commander = Command(file_path)

    if command == '1':  # ДОБАВЛЕНИЕ новой записи
        # commander.add()
        with Counter() as counter:
            try:
                commander.add(counter)
            except Exception as e:
                print(f"Ошибка: {e}")
    elif command == '5':  # УДАЛЕНИЕ записи из JSON
        commander.delete()
    elif command == '4':  # РЕДАКТИРОВАНИЕ записи
        commander.edit()
    elif command == '2':  # ЧТЕНИЕ всех сохраненных записей из JSON
        commander.read_all()
    elif command == '3':  # ЧТЕНИЕ сохраненных записей из JSON
        commander.read_nom()
    elif command == '0':  # ВЫХОД из программы
        break
    else:
        print("-------------------------\n",
              "Вы ввели неверную команду!")
