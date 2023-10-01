"""Represents a travel destination or place of interest."""


# Create your Place class in this file


class Place:
    def __init__(self, name="", country="", priority=0, is_visited=False):
        self.name = name
        self.country = country
        self.priority = priority
        self.is_visited = is_visited

    def __str__(self):
        return f"{self.name} in {self.country} (priority {self.priority}) {'visited' if self.is_visited else ''}"

    def mark_visited(self):
        self.is_visited = True

    def mark_unvisited(self):
        self.is_visited = False

    def is_important(self):
        return self.priority <= 2
