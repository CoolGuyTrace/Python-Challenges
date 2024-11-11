#Functions Challenge 6 – Is a palindrome?
#Create a function called is_palindrone that checks to see if a given string is a palindrome or not.

def is_palindrome(string):
    backwards_string = string [::-1]
    if string.lower() == backwards_string.lower():
        return True
    else:
        return False
    
print(is_palindrome(input("Enter a string: ")))