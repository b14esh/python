# Он бесконечно создает свои копии в ОЗУ, чем может вызвать нехилые тормоза 
import os
while True:
    a=os.fork()