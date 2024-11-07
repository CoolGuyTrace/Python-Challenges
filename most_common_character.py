#Functions Challenge 8 – Most common character
#Create a function called most_common_char that takes a string as a argument and the returns the most common character in that string.
import collections

def most_common_char(userString):
    return F"The most common character is {(collections.Counter(userString).most_common(1)[0])}"

print(most_common_char(input("Enter a string: ")))