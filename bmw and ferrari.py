from abc import ABC, abstractmethod
 
class Vehicle(ABC):
    
    @abstractmethod
    def fuel_type(self):
        """Abstract method for fuel type"""
        pass
        
    @abstractmethod
    def max_speed(self):
        """Abstract method for maximum speed"""
        pass
 
class BMW(Vehicle):
    def fuel_type(self):
        return "Diesel"
        
    def max_speed(self):
        return "240 km/h"
 
class Ferrari(Vehicle):
    def fuel_type(self):
        return "Petrol"
        
    def max_speed(self):
        return "350 km/h"

def display_vehicle_info(vehicle_obj):
    print(f"Fuel Type: {vehicle_obj.fuel_type()}")
    print(f"Max Speed: {vehicle_obj.max_speed()}")
    print("-" * 20)
 
if __name__ == "__main__":
    bmw_car = BMW()
    ferrari_car = Ferrari()
    
    print("--- BMW Details ---")
    display_vehicle_info(bmw_car)
    
    print("--- Ferrari Details ---")
    display_vehicle_info(ferrari_car)