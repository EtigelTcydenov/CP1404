import csv
from guitar import Guitar

def load_guitars():
    guitars = []
    with open('guitars.csv', 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            name, year, cost = row
            guitar = Guitar(name, int(year), float(cost))
            guitars.append(guitar)
    return guitars


def display_guitars(guitars):
    for guitar in guitars:
        print(guitar)


def add_guitar(guitars):
    name = input("Enter the name: ")
    year = int(input("Enter the year: "))
    cost = float(input("Enter the cost: "))
    new_guitar = Guitar(name, year, cost)
    guitars.append(new_guitar)


def save_guitars(guitars):
    with open('guitars.csv', 'w', newline='') as file:
        csv_writer = csv.writer(file)
        for guitar in guitars:
            csv_writer.writerow([guitar.name, guitar.year, guitar.cost])


if __name__ == "__main__":
    guitars = load_guitars()
    print("Guitars:")
    display_guitars(guitars)
    guitars.sort()
    print("\nOldest to Newest:")
    display_guitars(guitars)
    add_guitar(guitars)
    print("\nUpdated List of Guitars:")
    display_guitars(guitars)
    save_guitars(guitars)
    print("\nGuitars saved")