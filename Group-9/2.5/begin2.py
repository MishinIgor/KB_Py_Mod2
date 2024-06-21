try:
    # Открытие файла для чтения
    f = open('file1.txt', 'r',encoding='utf-8')
    # Чтение данных из файла
    data = f.read()
    print(data)
    # Закрытие файла
    f.close()
    a = 5/0
except FileNotFoundError:
    print("Файл не найден")
    with open('file1.txt','w'):
        pass
except Exception as e:
    print("Произошла ошибка:", str(e))