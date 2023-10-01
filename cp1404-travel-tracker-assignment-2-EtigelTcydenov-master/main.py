"""
Name: Tcydenov Etigel
Date: 30.09.2023
Brief Project Description: Travel Tracker is an interactive program designed to help users manage their global travel
goals. It offers functionalities to add, view, and update travel destinations using a straightforward menu. All data is
efficiently stored in and retrieved from a CSV file.
GitHub URL: https://github.com/EtigelTcydenov/CP1404
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from placecollection import PlaceCollection
from place import Place


class MainWidget(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "horizontal"
        self.place_collection = PlaceCollection()
        self.place_collection.load_places('places.csv')
        self.place_buttons = []

        # Left side of the GUI
        self.left_layout = BoxLayout(orientation="vertical", size_hint=(0.2, 1))
        self.add_widget(self.left_layout)

        self.spinner = Spinner(text="Visited", values=("Visited", "Priority", "Country", "Name"))
        self.spinner.bind(text=self.update_places_list)
        self.left_layout.add_widget(Label(text="Sort by"))
        self.left_layout.add_widget(self.spinner)

        # Add the "Add new place..." label
        self.left_layout.add_widget(Label(text="Add new place..."))

        self.left_layout.add_widget(Label(text="Name:"))
        self.name_input = TextInput()
        self.name_input.bind(text=self.on_text_change)
        self.left_layout.add_widget(self.name_input)

        self.left_layout.add_widget(Label(text="Country:"))
        self.country_input = TextInput()
        self.country_input.bind(text=self.on_text_change)
        self.left_layout.add_widget(self.country_input)

        self.left_layout.add_widget(Label(text="Priority:"))
        self.priority_input = TextInput()
        self.priority_input.bind(text=self.on_text_change)
        self.left_layout.add_widget(self.priority_input)

        add_button = Button(text="Add Place")
        add_button.bind(on_press=self.add_place)
        self.left_layout.add_widget(add_button)

        clear_button = Button(text="Clear")
        clear_button.bind(on_press=self.clear_fields)
        self.left_layout.add_widget(clear_button)

        self.right_layout = BoxLayout(orientation="vertical", size_hint=(0.8, 1))
        self.add_widget(self.right_layout)

        self.places_to_visit_label = Label(
            text=f"Places to visit: {self.place_collection.get_number_of_unvisited_places()}")
        self.right_layout.add_widget(self.places_to_visit_label)

        # Add dynamic status label
        self.status_label = Label(text="Welcome!")

        self.update_places_list(None, "Visited")  # Call this to initialize the buttons

    def on_text_change(self, instance, value):
        name = self.name_input.text.strip()
        country = self.country_input.text.strip()
        priority_str = self.priority_input.text.strip()

        try:
            priority = int(priority_str)
            if priority < 1:
                self.status_label.text = "Priority must be > 0"
                return
        except ValueError:
            pass  # We'll handle this later

        if not name or not country or not priority_str:
            self.status_label.text = "All fields must be completed"
            return

        if not priority_str.isdigit():
            self.status_label.text = "Please enter a valid number"

    def update_places_list(self, instance, value):
        # Remove existing buttons
        for btn in self.place_buttons:
            self.right_layout.remove_widget(btn)

        # Sorting
        if value == "Visited":
            places = sorted(self.place_collection.places, key=lambda x: x.is_visited)
        elif value == "Priority":
            places = sorted(self.place_collection.places, key=lambda x: x.priority)
        elif value == "Country":
            places = sorted(self.place_collection.places, key=lambda x: x.country)
        else:
            places = sorted(self.place_collection.places, key=lambda x: x.name)

        # Add sorted buttons
        for place in places:
            color = (1, 0, 0, 1) if not place.is_visited else (0, 1, 0, 1)
            btn = Button(text=f"{place.name}, {place.country} - priority {place.priority}", background_color=color)
            btn.bind(on_press=self.toggle_visit_status)
            self.right_layout.add_widget(btn)
            self.place_buttons.append(btn)

        # Ensure the status label remains at the bottom
        if self.status_label.parent:
            self.status_label.parent.remove_widget(self.status_label)
        self.right_layout.add_widget(self.status_label)

    def toggle_visit_status(self, instance):
        place_name = instance.text.split(',')[0]
        for place in self.place_collection.places:
            if place.name == place_name:
                if place.is_visited:
                    place.is_visited = False
                    instance.background_color = (1, 0, 0, 1)
                    self.status_label.text = f"You need to visit {place_name}."
                else:
                    place.is_visited = True
                    instance.background_color = (0, 1, 0, 1)
                    self.status_label.text = f"You visited {place_name}."
                break
        self.places_to_visit_label.text = f"Places to visit: {self.place_collection.get_number_of_unvisited_places()}"

    def add_place(self, instance):
        name = self.name_input.text
        country = self.country_input.text

        # Validation checks as before
        if not name or not country or not self.priority_input.text:
            self.status_label.text = "All fields must be completed."
            return

        try:
            priority = int(self.priority_input.text)
        except ValueError:
            self.status_label.text = "Please enter a valid number."
            return

        if priority < 1:
            self.status_label.text = "Priority must be > 0."
            return

        # Create a new Place instance and add to PlaceCollection
        new_place = Place(name, country, priority, False)
        self.place_collection.add_place(new_place)

        # Append the new place data to the places.csv file
        with open('places.csv', 'a') as f:
            f.write(f'{name},{country},{priority},n\n')  # 'n' indicates not visited

        # Refresh the list of buttons
        self.update_places_list(None, self.spinner.text)

        # Clear the input fields
        self.clear_fields(None)

    def clear_fields(self, instance):
        self.name_input.text = ""
        self.country_input.text = ""
        self.priority_input.text = ""


class MyApp(App):
    title = "TravelTracker"

    def build(self):
        return MainWidget()


if __name__ == "__main__":
    MyApp().run()
