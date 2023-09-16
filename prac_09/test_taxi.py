from prac_09.taxi import Taxi


def taxi_test():
    my_taxi = Taxi("Prius 1", 100)
    my_taxi.drive(40)
    print("Taxi Details:")
    print(my_taxi)
    print(f"Current Fare: ${my_taxi.get_fare():.2f}")
    my_taxi.start_fare()
    my_taxi.drive(100)
    print("\nTaxi Details After Restart:")
    print(my_taxi)
    print(f"Current Fare: ${my_taxi.get_fare():.2f}")


taxi_test()
