from abc import ABC, ABSTRACTMETHOD

class Cloud_Resource(ABC):

    @ABSTRACTMETHOD
    def get_description(self):
        pass

    @ABSTRACTMETHOD
    def get_price(self):
        pass

class VirtualMachine(Cloud_Resource):

    def get_price(self):
        return 100.0
    
    def get_description(self):
        return "Simple virtual machine"
    
class DataBase(Cloud_Resource):
    
    def get_price(self):
        return 250.0
    
    def get_description(self):
        return "Database"
    
class ResourceGroup(Cloud_Resource):
    def __init__(self, price):
        self.price = price

        self.bunch_price = []
    
    # Here i'm gonna add individual price to list of items (Children)

    def add_item(self, price):
        self.bunch_price.append(price)

    # Here i'm gonna sum all the price of items (Children) and return the total price of the group
    def get_price(self, bunch_price):
        total = 0
        for price in bunch_price:
            total += price
        return total
    