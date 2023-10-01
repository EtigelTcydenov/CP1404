"""(Incomplete) Tests for Place class."""
from place import Place

def run_tests():
    """Test Place class."""

    # Test empty place (defaults)
    print("Test empty place:")
    default_place = Place()
    print(default_place)
    assert default_place.name == ""
    assert default_place.country == ""
    assert default_place.priority == 0
    assert not default_place.is_visited

    # Test initial-value place
    print("Test initial-value place:")
    new_place = Place("Malagar", "Spain", 1, False)
    print(new_place)
    assert new_place.name == "Malagar"
    assert new_place.country == "Spain"
    assert new_place.priority == 1
    assert not new_place.is_visited

    # Test marking place as visited
    print("Test marking place as visited:")
    new_place.mark_visited()
    print(new_place)
    assert new_place.is_visited

    # Test marking place as unvisited
    print("Test marking place as unvisited:")
    new_place.mark_unvisited()
    print(new_place)
    assert not new_place.is_visited

    # Test important place determination
    print("Test checking if place is important:")
    important_place = Place("SamplePlace", "Country", 2, False)
    assert important_place.is_important()

run_tests()
