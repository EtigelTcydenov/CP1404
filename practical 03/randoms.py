import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

"""
first line shows random number in a range from 5 to 20
largest one was 20 
smallest one was 5


second line shows random number in a range from 3 to 10 with a step: 2
smallest one was 3
largest one: 9


third line shows random numbers in a range from 2.5 to 5.5 
smallest one: 2.588641993376381
largest one: 5.32815622774391
"""

print(random.randint(1,100))