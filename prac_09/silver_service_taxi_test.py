from prac_09.SilverServiceTaxi import SilverServiceTaxi  # Adjust the import based on your directory structure

def main():
    my_silver_taxi = SilverServiceTaxi("Hummer", 200, 4)
    my_silver_taxi.start_fare()
    my_silver_taxi.drive(18)
    print(f"Fare details for {my_silver_taxi.name}:")
    print(my_silver_taxi)

if __name__ == "__main__":
    main()
