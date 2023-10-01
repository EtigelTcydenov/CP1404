"""Represents a collection of travel destinations or places of interest."""


import csv
from place import Place


class PlaceCollection:
    def __init__(self):
        self.places = []

    def __str__(self):
        return "\n".join(str(place) for place in self.places)

    def load_places(self, filename='places.csv'):
        with open(filename, 'r') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                name, country, priority, visited_status = row
                is_visited = visited_status == 'v'
                self.places.append(Place(name, country, int(priority), is_visited))

    def save_places(self, filename='places.csv'):
        with open(filename, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            for place in self.places:
                visited_status = 'v' if place.is_visited else 'n'
                writer.writerow([place.name, place.country, place.priority, visited_status])

    def add_place(self, place):
        self.places.append(place)

    def sort(self, key):
        if key == "priority":
            self.places.sort(key=lambda place: (place.priority, place.name))

    def get_number_of_unvisited_places(self):
        return sum(1 for place in self.places if not place.is_visited)
