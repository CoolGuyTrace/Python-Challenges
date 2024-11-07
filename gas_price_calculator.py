#Functions Challenge 7 – Fuel cost calculator
#Write a function called fuel_cost that takes a distance as a required argument, 
#mpg (default 50 mpg) and fuel cost (default $1 a litre) as optional arguments. The function should return the cost in dollars.

def fuel_cost(distance, mpg=50, fuelCost=1):
    return (distance / mpg)*fuelCost

print(fuel_cost(int(input("Enter the distance: "))))