from vehicle import Vehicle
import ipdb

#* Notice the vehicle class is being called as an argument through the Car class.
class Car(Vehicle):
    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"

# ipdb.set_trace()