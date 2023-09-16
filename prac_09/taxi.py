"""
CP1404/CP5632 Practical
Car class
"""
from prac_09.car import Car

class Taxi(Car):
    price_per_km = 1.23
    def __init__(self, name, fuel):
        super().__init__(fuel)
        self.name = name
        self.current_fare_distance = 0

    def __str__(self):
        return f"{super().__str__()}, {self.current_fare_distance}km on current fare, ${self.price_per_km:.2f}/km"

    def get_fare(self):
        fare = self.price_per_km * self.current_fare_distance
        return round(fare, 1)

    def start_fare(self):
        self.current_fare_distance = 0

    def drive(self, distance):
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven
