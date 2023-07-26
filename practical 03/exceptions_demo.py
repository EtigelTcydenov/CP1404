"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
when user puts not int data type
2. When will a ZeroDivisionError occur?
when user divides numerator to 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("You cannot divide by 0, please change your choice")
        denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator
    print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
print("Finished.")
