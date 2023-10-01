"""(Incomplete) Tests for PlaceCollection class."""
from placecollection import PlaceCollection
from place import Place


def run_tests():
    """Test PlaceCollection class."""

    # Test empty PlaceCollection (defaults)
    print("Test empty PlaceCollection:")
    place_collection = PlaceCollection()
    print(place_collection)
    assert not place_collection.places

    # Test loading places
    print("Test loading places:")
    place_collection.load_places('places.csv')
    print(place_collection)
    assert place_collection.places

    # Test adding a new Place with values
    print("Test adding new place:")
    place_collection.add_place(Place("Smithfield", "Australia", 5, False))
    print(place_collection)

    # Test sorting placesz
    print("Test sorting - priority:")
    place_collection.sort("priority")
    print(place_collection)

    # Test getting number of unvisited places
    print("Test getting number of unvisited places:")
    print(place_collection.get_number_of_unvisited_places())
    # Assuming the initial data you provided, the output should be 2 (Lima and Rome).

    # Test saving places
    print("Test saving places:")
    place_collection.save_places('test_output.csv')


run_tests()
