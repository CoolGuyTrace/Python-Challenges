#Functions Challenge 2 – Divisible by 11 checker
#Write a function called is_divisable_by_11 that takes an integer as an parameter and returns whether it is divisible by 11 or not.

def is_divisable_by_11(number):
    if number % 11 == 0:
        return True
    else:
        return False
    

print(is_divisable_by_11(int(input("Enter a number to see if it is divisible by 11: "))))