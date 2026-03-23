# Week 2: Conditionals & Loops
# Application: Menu-Driven Logistics Manager

vehicles = []

while True:
    print("\n--- Logistics Manager Menu ---")
    print("1. Add Vehicle")
    print("2. View Vehicles")
    print("3. Exit")
    
    choice = input("Enter choice (1-3): ")
    
    if choice == '1':
        v_id = input("Vehicle ID: ")
        capacity = float(input("Capacity (tons): "))
        if capacity <= 0:
            print("Invalid capacity. Must be > 0.")
            continue
        vehicles.append(f"{v_id} ({capacity} tons)")
        print("Vehicle added.")
    elif choice == '2':
        print("\n--- Registered Vehicles ---")
        if not vehicles:
            print("No vehicles registered.")
        else:
            for v in vehicles:
                print(f"- {v}")
    elif choice == '3':
        print("Exiting Logistics Manager.")
        break
    else:
        print("Invalid choice. Try again.")
