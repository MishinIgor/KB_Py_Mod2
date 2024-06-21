# Открытие файла для чтения
f = open('file.txt', 'r',encoding='utf-8')
# Чтение данных из файла
for line in f:
    print(line,end='')
# Закрытие файла
f.close()
# Открытие файла для записи
f = open('file.txt', 'a',encoding='utf-8')
# Запись данных в файл
f.write('Hello, world!')
# Закрытие файла
f.close()
# Открытие файла для чтения
f = open('file.txt', 'r',encoding='utf-8')
# Чтение данных из файла и обработка
data = f.read()
print(data)
# Закрытие файла
f.close()
f = open('file.txt', 'a',encoding='utf-8')
f.write('\nВ этом мире слишком мало место, чтобы я столько хлеба испёк! :)')
f.close()
