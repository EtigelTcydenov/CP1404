"""..."""
# Copy your first assignment to this file, then update it to use Place class
# Optionally, you may also use PlaceCollection class

from place import Place
from place import Place
from placecollection import PlaceCollection
import csv
import random


def main():
    # Main function to run the Travel Tracker program.
    data_filename = "temp.csv"
    places_collection = load_data(data_filename)

    print("Travel Tracker 1.0 - by Your Name")
    print(f"{len(places_collection.places)} places loaded from {data_filename}")

    while True:
        print("\nMenu:")
        print("L - List places")
        print("R - Recommend random place")
        print("A - Add new place")
        print("M - Mark a place as visited")
        print("Q - Quit")

        choice = input(">>> ").strip().lower()

        if choice == 'l':
            display_places(places_collection)
        elif choice == 'r':
            recommend_place(places_collection)
        elif choice == 'a':
            add_place(places_collection)
        elif choice == 'm':
            mark_as_visited(places_collection)
        elif choice == 'q':
            save_data(data_filename, places_collection)
            print(f"{len(places_collection.places)} places saved to {data_filename}")
            print("Have a nice day :)")
            break


def load_data(filename):
    """
        Load place data from a CSV file.
        filename: Name of the CSV file to read from.
        PlaceCollection object with places loaded from the file.
        """
    places_collection = PlaceCollection()
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            place = Place(row[0], row[1], int(row[2]), row[3] == 'v')
            places_collection.add_place(place)
    return places_collection


def display_places(places_collection):
    # Display a list of places.
    print("List of Places:")
    for index, place in enumerate(places_collection.places, start=1):
        status = '*' if not place.is_visited else ' '
        print(f"{status}{index}. {place.name:<10} in {place.country:<20} Priority: {place.priority}")


def recommend_place(places_collection):
    # Recommend a random unvisited place from the list
    unvisited_places = [place for place in places_collection.places if not place.is_visited]
    if unvisited_places:
        random_place = random.choice(unvisited_places)
        print(f"Not sure where to visit next?\nHow about... {random_place.name} in {random_place.country}?")
    else:
        print("No places left to visit!")


def add_place(places_collection):
    # Get user input to add a new place to the list.
    city = input("Name: ").strip()
    while not city:
        print("Input cannot be blank")
        city = input("Name: ").strip()

    country = input("Country: ").strip()
    while not country:
        print("Input cannot be blank")
        country = input("Country: ").strip()

    priority = input("Priority: ")
    while not priority.isdigit():
        print("Invalid input; enter a valid number")
        priority = input("Priority: ")

    new_place = Place(city, country, int(priority), False)
    places_collection.add_place(new_place)
    print(f"{city} in {country} (priority {priority}) added to Travel Tracker")


def mark_as_visited(places_collection):
    # Mark a specified place from the list as visited.
    display_places(places_collection)
    place_number = input("Enter the number of a place: ")
    while not place_number.isdigit() or int(place_number) < 1 or int(place_number) > len(places_collection.places):
        print("Invalid place number")
        place_number = input("Enter the number of a place: ")

    selected_place = places_collection.places[int(place_number) - 1]
    if selected_place.is_visited:
        print(f"You have already visited {selected_place.name}")
    else:
        selected_place.is_visited = True
        print(f"{selected_place.name} in {selected_place.country} visited!")


def save_data(filename, places_collection):
    # Save the places to a CSV file.
    with open(filename, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        for place in places_collection.places:
            csv_writer.writerow([place.name, place.country, place.priority, 'v' if place.is_visited else 'n'])


if __name__ == "__main__":
    main()
