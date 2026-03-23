# Week 7: Encapsulation & Inheritance
# Application: Specialized Fleet Categories

class LogisticsEntity:
    """Base Class (Inheritance)"""
    def __init__(self, entity_id):
        self._entity_id = entity_id # Protected attribute
        self.__status = "Active"    # Private attribute (Encapsulation)

    def get_id(self):
        return self._entity_id
        
    def set_status(self, status):
        self.__status = status
        
    def get_status(self):
        return self.__status
        
    def display(self):
        print(f"Entity: {self.get_id()} Status: {self.get_status()}")

class Truck(LogisticsEntity):
    """Subclass inheriting LogisticsEntity specifically for long-haul heavy vehicles."""
    def __init__(self, entity_id, max_load_tons):
        super().__init__(entity_id)
        self.max_load_tons = max_load_tons
        
    def display(self):
        print(f"[Truck {self.get_id()}] Load Capacity: {self.max_load_tons}t | Status: {self.get_status()}")

class DeliveryVan(LogisticsEntity):
    """Subclass specifically for last-mile delivery."""
    def __init__(self, entity_id, parcels_limit):
        super().__init__(entity_id)
        self.parcels_limit = parcels_limit
        
    def display(self):
        print(f"[Van {self.get_id()}] Max Parcels: {self.parcels_limit} | Status: {self.get_status()}")

def main():
    t1 = Truck("T-Heavy-01", 25.5)
    v1 = DeliveryVan("V-City-05", 150)
    
    t1.set_status("In Transit")
    v1.set_status("Idle (Garage)")
    
    fleet = [t1, v1]
    for vehicle in fleet:
        vehicle.display() # Demonstrates Polymorphism / Inherited methods

if __name__ == "__main__":
    main()
