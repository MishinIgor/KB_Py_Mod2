try:
    f = open('savemygame.txt','x',encoding='utf-8')
    f.write('My game saved')
    f.close()
except FileExistsError:
    f = open('savemygame.txt','w',encoding='utf-8')
    if input('Файл уже сохранён, нажмите +, если хотите перезаписать\n') == '+':
        f.write('My game saved and i happy!!!')
    f.close()
