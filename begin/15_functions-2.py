pp = "________________________________________________________________________"
def create_record(name, telephon, address):
    """Create record"""
    record = {
        'name' : name,
        'phone': telephon,
        'address': address,
    }
    return record

user1 = create_record("Vasya", "+73420342305820358","Tunis")
user2 = create_record("Petia", "+324235252626", "sadsad")
print(user1)
print(user2)
print(pp)
# * перед persons не определенное количество
def give_award(medal, *persons):
    """Give medal persons"""
    for person in persons:
        #print("Tovarish " + person.title() + "nagrojdaetsa" + medal)
        print(f"Tovarish {person.title()} nagrojdaetsa {medal}")
give_award("Za berlin", "Vasia", "Petya")
give_award("Za london", "Valentin", "Petya", "Alexander")
print(pp)
