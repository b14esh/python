# Взаимодействие с переменнами LGPB
# Local
# Global


greeting = "Hello from global scope"

def greet():
    greeting = "Hello from enclosing scope"

    def nested():
        greeting = "Hello from local scope"
        print(greeting)
    nested()

greet()
print(greeting)

#
print("\n")
greeting1 = "Hello from global scope"
def greet1(greeting1):
    print(f'Greet in func: {greeting1}')
    greeting1 = "Hello from enclosing scope"
    print(f'Greet in func: {greeting1}')

    def nested1():
        greeting1 = "Hello from local scope"
        print(greeting1)
    nested1()
greet1("test")
print(greeting1)

print("\n")
greeting2 = "Hello from global scope"
def greet2():
    global greeting2
    print(f'Greet in func: {greeting2}')
    greeting1 = "Hello from enclosing scope"
    print(f'Greet in func: {greeting2}')

    def nested2():
        greeting2 = "Hello from local scope"
        print(greeting2)
    nested2()
greet2()
print(greeting2)