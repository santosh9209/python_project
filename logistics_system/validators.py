# Week 11: Exceptions & Validation

class InvalidCapacityError(Exception):
    """Raised when vehicle capacity is <= 0"""
    pass

class DuplicateVehicleError(Exception):
    """Raised when trying to add an already existing vehicle ID"""
    pass

def validate_capacity(cap_str):
    try:
        val = float(cap_str)
        if val <= 0:
            raise InvalidCapacityError(f"Invalid capacity {val}. Must be strictly positive.")
        return val
    except ValueError:
        raise ValueError("Capacity input must be a valid number.")
