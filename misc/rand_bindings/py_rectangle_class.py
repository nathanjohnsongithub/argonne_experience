# import numpy as np
# from random import randint

class Rectangle:
    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height
        # self.square = width == height

    def area (self):
        return self.width*self.height
    
    # def __str__(self):
       
    #     temp =  "Name:   " + str(self.name) 
    #     temp += "\nWidth:  " + str(self.width) 
    #     temp += "\nHeight: " + str(self.height) 
    #     temp += "\nArea:   " + str(self.height*self.width) 
    #     temp += "\nIs it a square? "
    #     if self.square:
    #         temp += "yes\n"
    #     else:
    #         temp += "no\n"

    #     return temp
    
    # def __add__(self, other):
    #     temp = Rectangle("",0,0)
    #     temp.name = self.name + "-" + other.name
    #     temp.width = self.width + other.width
    #     temp.height = self.height + other.height
    #     temp.square = temp.height == temp.width
    #     return temp

    # def print_3d(self):
        
    #     print("")
    #     for i in range(self.width):
    #         print("* ", end="")
    #     print("")


    #     for i in range(1, self.height-1):
    #         print("* ", end="")
    #         for j in range(self.width - 2):
    #             print("  ", end="")
    #         print("* ")

    #     for i in range(self.width):
    #         print("* ", end="")
    #     print("\n")

