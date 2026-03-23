# Week 1: Python Setup + Basic Entry Script
# Concept: Variables, Data Types, Input/Print, F-strings
# Application: Dynamic Transport Logistics - Single Vehicle Entry

print("--- Dynamic Transport Logistics System ---")
print("Enter details for a new delivery vehicle:")

# Capturing variable data
vehicle_id = input("Enter Vehicle ID (e.g., V101): ")
driver_name = input("Enter Driver Name: ")
capacity_tons = float(input("Enter Load Capacity (in tons): "))
current_location = input("Enter Current Location: ")

# Printing output formatted clearly
print("\n--- Vehicle Registration Successful ---")
print(f"Vehicle ID: {vehicle_id}")
print(f"Driver Name: {driver_name}")
print(f"Load Capacity: {capacity_tons} tons")
print(f"Current Location: {current_location}")
print("---------------------------------------")
