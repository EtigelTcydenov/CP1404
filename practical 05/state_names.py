"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

for name, long_name in CODE_TO_NAME.items():
    print(f"{name} is {long_name}")

for name in CODE_TO_NAME:
    try:
        state_code = input("Enter short state: ").upper()
        if state_code == "":
            break
        print(state_code, "is", CODE_TO_NAME[state_code])
    except KeyError:
        print("Invalid short state")

