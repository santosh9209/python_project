# Week 4: Functions
# Application: Modular Logistics Management

vehicles = []

def add_vehicle():
    v_id = input("Vehicle ID: ").strip().upper()
    if validate_id(v_id):
        print("Vehicle ID already exists.")
        return
        
    driver = input("Driver Name: ").strip().title()
    location = input("Current Location: ").strip().title()
    vehicles.append([v_id, driver, location])
    print(f"Vehicle {v_id} added.")

def validate_id(v_id):
    for v in vehicles:
        if v[0] == v_id:
            return True
    return False

def view_vehicles():
    print(f"\n{'ID':<10} | {'DRIVER':<15} | {'LOCATION'}")
    print("-" * 40)
    for v in vehicles:
        print(f"{v[0]:<10} | {v[1]:<15} | {v[2]}")

def search_vehicle():
    query = input("Search by ID/Driver: ").strip().lower()
    for v in vehicles:
        if query in v[0].lower() or query in v[1].lower():
            print(f"Found: {v[0]} - {v[1]} ({v[2]})")
            return
    print("Not found.")

def main():
    while True:
        print("\n1. Add | 2. View | 3. Search | 4. Exit")
        choice = input("Choice: ")
        if choice == '1': add_vehicle()
        elif choice == '2': view_vehicles()
        elif choice == '3': search_vehicle()
        elif choice == '4': break

if __name__ == "__main__":
    main()
