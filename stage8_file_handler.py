# Week 8: File Handling
# Application: CSV and JSON Storage for Vehicles & Routes
import json
import csv
import os

VEHICLES_FILE = "vehicles.json"
ROUTES_FILE = "routes.csv"

def save_vehicles(vehicles_dict):
    try:
        with open(VEHICLES_FILE, 'w') as f:
            json.dump(vehicles_dict, f, indent=4)
        print("Vehicles saved to JSON.")
    except Exception as e:
        print(f"Error saving vehicles: {e}")

def load_vehicles():
    if not os.path.exists(VEHICLES_FILE):
        return {}
    try:
        with open(VEHICLES_FILE, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading vehicles: {e}")
        return {}

def save_route_log(route_id, v_id, start, end):
    file_exists = os.path.isfile(ROUTES_FILE)
    try:
        with open(ROUTES_FILE, 'a', newline='') as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["RouteID", "VehicleID", "Start", "End"])
            writer.writerow([route_id, v_id, start, end])
        print("Route appended to CSV.")
    except Exception as e:
        print(f"Error appending route log: {e}")

if __name__ == "__main__":
    # Test Data
    test_vehicles = {
        "V10": {"driver": "Anna", "capacity": 5.0},
        "V20": {"driver": "Ben", "capacity": 10.0}
    }
    save_vehicles(test_vehicles)
    loaded = load_vehicles()
    print("Loaded dictionary:", loaded)
    save_route_log("R1", "V10", "Warehouse A", "Store B")
