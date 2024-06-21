while True:
    try:
        f = open('file.txt','x')
        f.write('New Save')
        f.close()
        break
    except FileExistsError:
        vibor = input('Файл уже создан, хотите перезаписать?(+ если да):')
        if vibor == '+':
            f = open('file.txt','w')
            f.write('Save agen')
            f.close()
            break
        
    