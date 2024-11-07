#Functions Challenge 4 – Hexagon area calculator
#Write a function called hexagon_area that takes the length of a side of a regular hexagon as a parameter and returns the area of the hexagon.

import math

def hexagon_area(side):
    return round((3*math.sqrt(3)/2)*side**2, 2)

print(hexagon_area(int(input("Enter the side length of a hexagon: "))))
