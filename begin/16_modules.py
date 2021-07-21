# Все функции во втором файле mod16.py
###import mod16

#START----------- это переехало в файл mod16.py
#def aaa():
#    print("AAAA")
#def bbb():
#    print("BBBB")
#def ccc():
#    print("CCCC")
#def ddd():
#    print("DDDD")
#def pp():
#    print("_______________________________________________")
# END ---------- это переехало в файл mod16.py

# ---- MAIN так мы вызывали когда модули жили тут
#aaa()
#bbb()
#ccc()
#ddd()
#pp()

#!!! чет с ходу нехера не заработало пошол разбиратся почему .......
#import sys
#print(sys.path) # хотелось увидеть окружения env

#import pkgutil # а этим модулем хотелось увидеть все модули каторые загрузились
#search_path = ['.'] # Используйте None, чтобы увидеть все модули, импортируемые из sys.path
#all_modules = [x[1] for x in pkgutil.iter_modules(path=search_path)]
#print(all_modules) # Увидел что моудль mdd16 подрубается ...... но всеравно нехера не работает.....

## почитали почитали.....
# вызывается следуещим образом имя_модуля.имя_функции ......... :)

#---------MAIN
###mod16.aaa()
###mod16.bbb()
###mod16.ccc()
###mod16.ddd()
###mod16.pp()


#что бы не писать mod16.aaa() делается так
from mod16 import *
# можно вызвать что то конретное например aaa
#from mod16 import aaa
aaa()
bbb()
ccc()
ddd()
pp()

