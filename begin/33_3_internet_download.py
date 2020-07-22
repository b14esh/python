from urllib import request
import sys

myUrl = "https://b14esh.com/img/b14esh/200w1.png" # что качаем
myFile = "O:\\mykartinka.png" # куда качаем

try:
     print(f"Start download from: >>> {myUrl} \n\t\t\t\t To: >>> {myFile}")
     request.urlretrieve(myUrl, myFile)
except Exception:
    print("AHTUNG!!!")
    print(sys.exc_info()[1])
    exit()
print(f"File Downloaded and saved >>> {myFile}")