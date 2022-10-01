"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator != 0:
        fraction = numerator / denominator
        print(fraction)
    else:
        print("Cannot divide by zero!")
except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")

#When will a ValueError occur?
# when the input of either numerator or denominator are something other than a number such as a letter
#When will a ZeroDivisionError occur?
# when the denominator is entered as 0
#Could you change the code to avoid the possibility of a ZeroDivisionError?
# yeah by using an if statment