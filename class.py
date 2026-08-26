class vechile:

    def __init__(self,name,max_speed,milage):
        self.name = name
        self.max_speed = max_speed
        self.milage = milage

class bus (vechile):
    pass

school_bus = bus("I HATE SCHOOL",80,12)
print("name",school_bus.name,"speed",school_bus.max_speed,"milage",school_bus.milage)