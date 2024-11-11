#Functions Challenge 9 – Is a prime number?
#Write a function called is_prime that takes an integer as an argument and checks if it is a prime number or not, returning a Boolean.

def is_prime(number):
    if number == 2:
        return True
    elif number == 1:
        return False
    for i in range(2, number):
        if number % i == 0 and i != number:
            return False
        else:
            return True
        

print(is_prime(int(input("Enter a number: "))))