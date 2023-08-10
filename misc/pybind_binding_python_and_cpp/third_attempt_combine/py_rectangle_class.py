class Rectangle:
    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height
        # self.square = width == height

    def area (self):
        return self.width*self.height

    def __str__(self):
        temp =  "Name:   " + str(self.name) 
        temp += "\nWidth:  " + str(self.width) 
        temp += "\nHeight: " + str(self.height) 

        return temp   

