f = open('file.txt','a',encoding='utf-8')
hleb = ['Булка-белого','Булка-чёрного']
f.write('\n')
f.writelines(hleb)
f.close()