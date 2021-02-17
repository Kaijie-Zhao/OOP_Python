class ContactList(list):
    """Extend class list with search by name method.
       Return a list of all matching contact with the input name and empty list if no match up found"""

    def search(self, name):
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts


class Contact:
    all_contacts = ContactList()

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        Contact.all_contacts.append(self)

    def show_all(self):
        for contact in self.all_contacts:
            print("{0}: {1}".format(contact.name, contact.phone))

    def show(self):
        print("{0}: {1}".format(self.name, self.phone))


class Supplier(Contact):
    def order(self, order):
        print("Place an order of '{0}' to {1}".format(order, self.name))


class Customer(Contact):

    def __init__(self, name, phone, id):
        super().__init__(name, phone)
        self.id = id

    def show(self):
        print("{0}: {1}".format(self.id, self.name))


if __name__ == '__main__':

