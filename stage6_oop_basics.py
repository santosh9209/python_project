# Week 6: OOP: Classes, Objects, Constructors
# Application: Object-Oriented Logistics Basics

class Route:
    def __init__(self, route_id, start, end, distance_km):
        self.route_id = route_id
        self.start = start
        self.end = end
        self.distance_km = distance_km
        
    def display_info(self):
        return f"Route {self.route_id}: {self.start} -> {self.end} ({self.distance_km}km)"

class Vehicle:
    def __init__(self, vehicle_id, driver_name, capacity_tons):
        self.vehicle_id = vehicle_id
        self.driver_name = driver_name
        self.capacity_tons = capacity_tons
        self.current_route = None
        
    def assign_route(self, route):
        self.current_route = route
        print(f"Assigned {route.route_id} to vehicle {self.vehicle_id}.")
        
    def display_info(self):
        print(f"\n[{self.vehicle_id}] Driver: {self.driver_name} | Capacity: {self.capacity_tons}t")
        if self.current_route:
            print(f"  Doing: {self.current_route.display_info()}")
        else:
            print("  Status: Idle")

def main():
    # Instantiate objects
    v1 = Vehicle("V1", "Alice", 10.5)
    v2 = Vehicle("V2", "Bob", 4.0)
    
    r1 = Route("R101", "New York", "Boston", 345)
    
    v1.display_info()
    v1.assign_route(r1)
    v1.display_info()
    
    v2.display_info()

if __name__ == "__main__":
    main()
