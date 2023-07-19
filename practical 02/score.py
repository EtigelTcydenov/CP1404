import random


def main():
    user_score = float(input("Enter score: "))
    result = get_score_result(user_score)
    print(result)

    random_score = random.uniform(0, 100)
    result = get_score_result(random_score)
    print(f"Random Score: {random_score:.2f};\n{result}")


def get_score_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
