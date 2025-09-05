class contact: #create a clas:s
    def __init__(self): #init is the constrctor in python if u dnt use it u hv to set things manlly
        self.contacts = {}#and empty dict to store nam nd numbers
    def add_contact(self, name, phone):#add the contact name as the key then phone as value
        self.contacts[name] = phone
    def del_contact(self, name):
        if name in self.contacts:#check if nam exist if yes remove if no cntact not found
            del self.contacts[name]
    def search(self, name):
        if name in self.contacts:#looks for the name in dict 
            return self.contacts[name]
    def show_all_contacts(self):#loops throuh all contact in dict
        if not self.contacts:
            print("no contacts")
        else:
            for name, phone in self.contacts.items():#prints eact name with its num
                print(f"{name}: {phone}")
book = contact()
book.add_contact("alice", "07034564466")
book.add_contact("bob", "08088887666")
print(book.search("alice"))
book.del_contact("bob")
book.show_all_contacts()
