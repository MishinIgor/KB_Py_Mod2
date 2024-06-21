f = open('file.txt', 'r', encoding='utf-8')

# Чтение данных из файла
for line in f:
    print(line,end='\n')

# Закрытие файла
f.close()

# Открытие файла для записи
f = open('file1.txt', 'w')

# Запись данных в файл
f.write('Hello, world!')

# Закрытие файла
f.close()

# Открытие файла для чтения
f = open('file1.txt', 'r')

# Чтение данных из файла и обработка
data = f.read()
print(data[:5])

# Закрытие файла
f.close()
