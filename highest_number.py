#Functions Challenge 3 – Highest number
#Write a function called get_highest that takes 2 numbers as parameters and returns the highest of the 2 numbers.

def get_highest(num1, num2):
    if num1-num2 < 0:
        return (F"{num2} is greater than {num1}")
    elif num1-num2 > 0:
        return (F"{num1} is greater than {num2}")
    elif num1-num2 == 0:
        return "They are the same number!"
    
print(get_highest(int(input("Enter a number: ")), int(input("Enter another number: "))))

 