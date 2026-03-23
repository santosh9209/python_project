import json
import os
from .models import Vehicle
from .validators import DuplicateVehicleError

class FleetService:
    def __init__(self, file_path="fleet_data.json"):
        self.file_path = file_path
        self.vehicles = self._load()

    def _load(self):
        if not os.path.exists(self.file_path):
            return {}
        try:
            with open(self.file_path, 'r') as f:
                data = json.load(f)
                # Reconstruct Objects from dictionary
                fleet = {}
                for k, v in data.items():
                    obj = Vehicle(k, v["driver_name"], v["capacity_tons"])
                    obj.status = v.get("status", "Active")
                    fleet[k] = obj
                return fleet
        except Exception as e:
            print(f"Warning: Failed to load data -> {e}")
            return {}

    def _save(self):
        data = {k: v.to_dict() for k, v in self.vehicles.items()}
        try:
            with open(self.file_path, 'w') as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            print(f"Error saving data -> {e}")

    def add_vehicle(self, v_id, driver, capacity):
        if v_id in self.vehicles:
            raise DuplicateVehicleError(f"Vehicle '{v_id}' already registered!")
        
        new_v = Vehicle(v_id, driver, capacity)
        self.vehicles[v_id] = new_v
        self._save()
        return new_v
        
    def get_all(self):
        return self.vehicles
