pp = "--------------------------------------------"


#def napechat_privetstvie():
def napechat_privetstvie(name):
    """Print Privetstvie"""
    #print("Congratuletion, vish all the best")
    print("Congratuletion " + name + ", vish all the best!")
    #print("Hello Hello  Hello Hello Hello Hello Hello Hello !!!")

#def aaaa():
#    print("AAAA")

#-------------------------------------------------
print(pp)
#napechat_privetstvie()
#napechat_privetstvie()
#aaaa()
print(pp)
napechat_privetstvie("Denis")
napechat_privetstvie("Vasiii")
napechat_privetstvie("Purty")
print(pp)
def summa(x,y):
    print(x+y)

summa(10, 20)
print(pp)

def summa1(x , y):
    s = x + y
    return s

x = summa1(33, 22)
print(x)
print(pp)
def summa1(x , y):
    return x + y

x = summa1(77, 22)
print(x)
print(pp)

# фактор
#2! = 1 * 2
#3! = 1 * 2 * 3
#4! = 1 * 2 * 3 * 4

def factorial(x):
    """calculate factorial namber x """
    otvet = 1
    for i in range(1, x + 1):
        otvet = otvet * i
    return otvet
print(factorial(1))
print(factorial(5))
print(pp)
for i in range(1,10):
    #print(str(i) + "!\t = " + str(factorial(i)))
    print(f"{i} + !\t = {factorial(i)}")
print(pp)