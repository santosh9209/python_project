# Week 3: Strings & Lists
# Application: Vehicle Listing & Search

# Storing vehicles as a list of lists: [id, driver, location]
vehicles = []

while True:
    print("\n--- Fleet Dashboard ---")
    print("1. Add Vehicle")
    print("2. View All Vehicles")
    print("3. Search Vehicle")
    print("4. Exit")
    
    choice = input("Choice: ")
    
    if choice == '1':
        v_id = input("Vehicle ID: ").strip().upper()
        driver = input("Driver Name: ").strip().title()
        location = input("Current Location: ").strip().title()
        vehicles.append([v_id, driver, location])
        print("Added securely.")
        
    elif choice == '2':
        print(f"\n{'ID':<10} | {'DRIVER':<15} | {'LOCATION'}")
        print("-" * 40)
        for v in vehicles:
            print(f"{v[0]:<10} | {v[1]:<15} | {v[2]}")
            
    elif choice == '3':
        query = input("Enter Vehicle ID or Driver to search: ").strip().lower()
        found = False
        for v in vehicles:
            if query in v[0].lower() or query in v[1].lower():
                print(f"Match: {v[0]} - Driven by {v[1]} at {v[2]}")
                found = True
        if not found:
            print("No matching vehicle found.")
            
    elif choice == '4':
        break
