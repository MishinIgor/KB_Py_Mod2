try:
    # Открытие файла для чтения
    f = open('file.txt', 'r')


    # Чтение данных из файла
    data = f.read()
    print(data)


    # Закрытие файла
    f.close()
    a = 5/0
except FileNotFoundError:
    print("Файл не найден")
except PermissionError:
    print("Нет доступа к файлу")
except Exception as e:
    print("Произошла ошибка:", str(e))