# Week 5: Dictionaries, Sets, Tuples
# Application: Rich Data Model for Logistics

# Dictionary for rich vehicle records, Set for unique active route IDs
vehicles = {}
active_routes = set()

def add_vehicle():
    v_id = input("Vehicle ID: ").strip().upper()
    if v_id in vehicles:
        print("Vehicle ID already exists.")
        return
        
    driver = input("Driver Name: ").strip().title()
    capacity = float(input("Load Capacity (tons): "))
    
    # Using a dictionary to store details
    vehicles[v_id] = {
        "driver": driver,
        "capacity": capacity,
        "location": "HQ",
        "route_history": []
    }
    print(f"Vehicle {v_id} added.")

def assign_route():
    v_id = input("Vehicle ID to assign: ").strip().upper()
    if v_id not in vehicles:
        print("Vehicle not found.")
        return
        
    route_id = input("Route ID (e.g., R10): ").strip().upper()
    if route_id in active_routes:
        print("Route ID is already actively assigned.")
        return
        
    start_point = input("Start Location: ").strip().title()
    end_point = input("End Location: ").strip().title()
    
    # Tuple representing an immutable route pair
    route_tuple = (start_point, end_point)
    
    active_routes.add(route_id)
    vehicles[v_id]["route_history"].append(route_tuple)
    vehicles[v_id]["location"] = "On Route"
    print(f"Route {route_id} {route_tuple} assigned to {v_id}.")

def view_vehicles():
    for v_id, details in vehicles.items():
        print(f"\nID: {v_id}")
        print(f"  Driver:   {details['driver']}")
        print(f"  Capacity: {details['capacity']} t")
        print(f"  Location: {details['location']}")
        print(f"  Routes:   {details['route_history']}")

def main():
    while True:
        print("\n1. Add Vehicle | 2. Assign Route | 3. View All | 4. Exit")
        choice = input("Choice: ")
        if choice == '1': add_vehicle()
        elif choice == '2': assign_route()
        elif choice == '3': view_vehicles()
        elif choice == '4': break

if __name__ == "__main__":
    main()
