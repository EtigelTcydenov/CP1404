from prac_09.unreliable_car import UnreliableCar


def main() -> object:
    my_car = UnreliableCar("My Car", 50, 70)
    distance_driven = my_car.drive(30)
    print(f"Actual distance driven: {distance_driven} km")
    print(my_car)


main()
