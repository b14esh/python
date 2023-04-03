file = None
try:
    file = open(r'c:\file\zxc.txt')
    data = file.read()
except FileNotFoundError as ex:
    print(f'Error has occured. Description: {ex.strerror}')
else:
    print('maybe else')
finally: # будет испольненно в любом случае
    print('Final')
    if file:
        file.close()
print('doing some work here')