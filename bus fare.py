class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity
 
    def fare(self):
        return self.capacity * 100
 
 
class Bus(Vehicle):
    def fare(self):
        base_fare = super().fare()
        
        maintenance_charge = base_fare * 0.10
        total_fare = base_fare + maintenance_charge
        return total_fare
 
 
if __name__ == "__main__":
    school_bus = Bus("School Bus", 12, 50)
    
    print(f"Vehicle Name: {school_bus.name}")
    print(f"Total Bus Fare: {school_bus.fare()}")