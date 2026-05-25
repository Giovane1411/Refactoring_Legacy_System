from abc import ABC, abstractmethod

class CloudResource(ABC):

    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_price(self):
        pass

class VirtualMachine(CloudResource):

    def get_price(self):
        return 100.0
    
    def get_description(self):
        return "Simple virtual machine"
    
class DataBase(CloudResource):
    
    def get_price(self):
        return 250.0
    
    def get_description(self):
        return "Database"
    
class ResourceGroup(CloudResource):
    def __init__(self):
        self._children: list[CloudResource] = []
    
    # Here i'm gonna add individual price to list of items (Children)

    def add_item(self, resource: CloudResource):
        self._children.append(resource)

    # Here i'm gonna sum all the price of items (Children) and return the total price of the group
    def get_price(self):
        return sum(r.get_price() for r in self._children)
    
    def get_description(self):
        return f"Group with {len(self._children)} resources"
    
class ServiceDecorator(CloudResource):

    
    def __init__(self, resource :CloudResource):
        self.resource = resource
    
    @abstractmethod
    def get_price(self):
        pass

    @abstractmethod
    def get_description(self): 
        pass
    

class AutomaticBackup(ServiceDecorator):

    def __init__(self, resource: CloudResource):
        super().__init__(resource)
    
    def get_price(self):
        return 50.0 + self.resource.get_price()
    
    def get_description(self):
        return "+ Backup"

class FirewallPremium(ServiceDecorator):
    
    def __init__(self, resource: CloudResource):
        super().__init__(resource)

    def get_price(self):
        return 80.0 + self.resource.get_price()
    
    def get_description(self):
        return "+ Firewall"

class Support24x7(ServiceDecorator):

    def __init__(self, resource: CloudResource):
        super().__init__(resource)
    
    def get_price(self):
        base = self.resource.get_price()
        return base + (10 * (base/100))
    
    def get_description(self):
        return "+ VIP Support"
