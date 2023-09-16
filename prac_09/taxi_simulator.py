from prac_09.taxi import Taxi
from prac_09.SilverServiceTaxi import SilverServiceTaxi


def main():
    print("Let's drive!")
    current_taxi = None
    bill_to_date = 0.0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    while True:
        print_menu()
        user_choice = input(">>> ").lower()

        if user_choice == 'q':
            break
        elif user_choice == 'c':
            display_available_taxis(taxis)
            current_taxi = choose_taxi(taxis)
        elif user_choice == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                drive_taxi(current_taxi)
                trip_cost = current_taxi.get_fare()
                bill_to_date += trip_cost
                print(f"Your trip cost you ${trip_cost:.2f}")
                print(f"Bill to date: ${bill_to_date:.2f}")
        else:
            print("Invalid option")

    print(f"Total trip cost: ${bill_to_date:.2f}")
    print("Taxis are now:")
    display_available_taxis(taxis)


def print_menu():
    print("q)uit, c)hoose taxi, d)rive")


def display_available_taxis(taxis):
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxis):
    try:
        choice = int(input("Choose taxi: "))
        if 0 <= choice < len(taxis):
            return taxis[choice]
        else:
            print("Invalid taxi choice")
            return None
    except ValueError:
        print("Invalid input")
        return None


def drive_taxi(taxi):
    try:
        distance = float(input("Drive how far? "))
        taxi.drive(distance)
    except ValueError:
        print("Invalid input")


main()
