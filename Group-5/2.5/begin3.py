while True:
    try:
        # Открытие файла для чтения
        f = open('file1.txt', 'r',encoding='utf-8')
        # Чтение данных из файла
        data = f.read()
        print(data)
        # Закрытие файла
        f.close()
        a = 5/0
        break
    except FileNotFoundError:
        print("Файл не найден")
        f = open('file1.txt','w',encoding='utf-8')
        f.write('Ну теперь такой файл есть')
        f.close()
    except Exception as e:
        print("Произошла ошибка:", str(e))
        break