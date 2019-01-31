class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y




# class Circle(Point):
#         def __init__(self, Point, r):
#             super().__init__(Point.x, Point.y)
#             self.r = r
        
#         def get_area(self):
#             return ((self.r)**2)*(3.14)

#         def get_perimeter(self):
#             return self.r*2*(3.14)
        
#         def get_center(self):
#             return "({},{})".format(self.x, self.y)

#         def print(self):
#             print("Circle : ({}, {}), r : {}".format(self.x, self.y, self.r))

class Circle:
    def __init__(self, point, r):
        self.x = point.x
        self.y = point.y
        self.r = r

    def get_area(self):
            return ((self.r)**2)*(3.14)

    def get_perimeter(self):
        return self.r*2*(3.14)
    
    def get_center(self):
        return "({},{})".format(self.x, self.y)

    def print(self):
        print("Circle : ({}, {}), r : {}".format(self.x, self.y, self.r))
 


p1 = Point(3,5)
c1 = Circle(p1,3)

p1 = Point(0, 0) 
c1 = Circle(p1, 3) 
print(c1.get_area()) 
print(c1.get_perimeter()) 
print(c1.get_center()) 
c1.print() 
p2 = Point(4, 5) 
c2 = Circle(p2, 1) 
print(c2.get_area()) 
print(c2.get_perimeter()) 
print(c2.get_center()) 
c2.print()