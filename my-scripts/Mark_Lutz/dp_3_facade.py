'''
It basically means face of building or outer lying interface of any complex system(that contains several sub systems)
It provides Interface(in form of Facade class) to some complex subsystems so as to provide ease to the user/client of the subsystems i.e. user/client can now directly call the Facade class to perform the actual tasks being provided via all sub systems
'''

class Washing():
    def wash(self):
        print("Washing..")
        
class Rinsing():
    def rinse(self):
        print("Rinsing")
        
class Spinning():
    def spin(self):
        print("Spinning")

class Washing_machine():
    def __init__(self):
        self.washing = Washing()
        self.rinsing= Rinsing()
        self.spinning = Spinning()
    
    def start_wash(self):
        self.washing.wash()
        self.rinsing.rinse()
        self.spinning.spin()
        
w = Washing_machine()
w.start_wash()
        
        

