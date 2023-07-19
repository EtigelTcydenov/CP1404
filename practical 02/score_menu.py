import random
MENU = """Menu:
(G)et a valid score (must be 0-100 inclusive)
(P)rint result
(S)how stars
(Q)uit"""

def main():
    score = get_valid_score()
    choice = ""
    while choice != "Q":
        print(MENU)
        choice = input(">>> ").upper()
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = get_score_result(score)
            print(f"Result: {result}")
        elif choice == "S":
            show_stars(score)
        elif choice == "Q":
            print("Farewell! Thank you for using the program.")
        else:
            print("Invalid input, please try again.")


def get_valid_score():
    while True:
        try:
            score = float(input("Enter a valid score (0-100 inclusive): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid score. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_score_result(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def show_stars(score):
    stars = int(score)
    print("*" * stars)


main()
