# Week 9: Multi-Module Architecture
# Defines the core classes used across the system

class LogisticsEntity:
    def __init__(self, entity_id):
        self._entity_id = entity_id
        self.__status = "Active"

    @property
    def id(self): return self._entity_id
    
    @property
    def status(self): return self.__status

    @status.setter
    def status(self, val): self.__status = val


class Vehicle(LogisticsEntity):
    def __init__(self, entity_id, driver_name, capacity_tons):
        super().__init__(entity_id)
        self.driver_name = driver_name
        self.capacity_tons = capacity_tons

    def to_dict(self):
        return {
            "driver_name": self.driver_name,
            "capacity_tons": self.capacity_tons,
            "status": self.status
        }
