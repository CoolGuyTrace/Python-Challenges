#Functions Challenge 1 - Kilometers to miles converter
#Write a function called km_to_miles that takes kilometers as a parameter, converts it into miles and returns the result.

def km_to_miles(kilometers):
    return round(kilometers * 0.62137, 1)

print(km_to_miles(int(input("Enter a Kilometer to covert it into miles: "))))