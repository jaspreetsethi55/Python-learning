from abc import ABC,abstractmethod

class Shape():
    
    @abstractmethod
    def Area():
        pass
    
class Rectangle(Shape):

    @staticmethod
    def Area():
        area =  5*5
        return area
        
class square(Shape):
    
    @staticmethod
    def Area():
        area =  10*10
        return area
        

class Main():
    def Area():
        for shape in Shape.__subclasses__():
            area = shape.Area()
            print(shape,area)
            
if __name__ == '__main__':  
    Main.Area()
