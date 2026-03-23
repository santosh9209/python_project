# Main Application tying together Weeks 9-12 concepts
from logistics_system.services import FleetService
from logistics_system.validators import validate_capacity, DuplicateVehicleError, InvalidCapacityError
from logistics_system.analytics import generate_fleet_report

def main():
    service = FleetService()
    
    while True:
        print("\n=== Enterprise Logistics System ===")
        print("1. Register Vehicle")
        print("2. View Fleet")
        print("3. Run Analytics Report")
        print("4. Exit")
        
        choice = input("Enter choice: ").strip()
        
        if choice == '1':
            v_id = input("Vehicle ID: ").upper()
            driver = input("Driver Name: ").title()
            cap_str = input("Capacity (tons): ")
            
            try:
                cap_val = validate_capacity(cap_str)
                service.add_vehicle(v_id, driver, cap_val)
                print(f"Success: Registered {v_id}")
            except (DuplicateVehicleError, InvalidCapacityError, ValueError) as e:
                print(f"Error: {e}")
                
        elif choice == '2':
            fleet = service.get_all()
            if not fleet:
                print("Fleet is empty.")
            else:
                print("\n--- Current Fleet ---")
                for v in fleet.values():
                    print(f"[{v.id}] {v.driver_name} - {v.capacity_tons}t ({v.status})")
                    
        elif choice == '3':
            generate_fleet_report(service.get_all())
            
        elif choice == '4':
            print("Shutting down Logistics System.")
            break
        else:
            print("Invalid selection.")

if __name__ == "__main__":
    main()
