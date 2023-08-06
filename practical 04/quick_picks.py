import random

# Constants
MIN_NUMBER = 1
MAX_NUMBER = 45
NUM_NUMBERS = 6


def generate_quick_pick():
    return sorted(random.sample(range(MIN_NUMBER, MAX_NUMBER + 1), NUM_NUMBERS))


def main():
    num_quick_picks = int(input("How many quick picks? "))
    for _ in range(num_quick_picks):
        quick_pick = generate_quick_pick()
        print(" ".join(str(number).rjust(2) for number in quick_pick))


main()
