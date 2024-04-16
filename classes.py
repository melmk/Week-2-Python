class Point():
    # def __init is a method or function that will automatically be called anytime an object of this class is created
    # all functions that operate on objects themselves (methods) take the self argument (the object we are currently dealing with) 
    # other included arguments are the args we will provide when we create the object, in this case, x and y coordinates for a point
    def __init__(self, x, y):
        self.x = x # this assigns the value from the input argument, x, to the x property of the current object (self) so that we can store the value
        self.y = y
        

p = Point(10, 8)

print(f"The x coordinate of point is {p.x}. The y coordinate is {p.y}")