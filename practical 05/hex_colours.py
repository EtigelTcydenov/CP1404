COLOURS = {
    "Celeste": "#b2ffff",
    "Champagne": "#f7e7ce",
    "Chocolate": "#d2691e",
    "Coquette": "#ff3800",
    "Kombu Green": "#354230",
    "Laser Lemon": "#ffff66",
    "Moccasin": "#ffe4b5",
    "Pale": "#db7093",
    "Selective Yellow": "#ffba00"
}

print("Available color names:")
for color_name in COLOURS:
    print(color_name)

while True:
    input_color = input("Enter a color name: ").strip().title()
    if input_color == "":
        break

    try:
        color_code = COLOURS[input_color]
        print(f"{input_color.capitalize()} is {color_code}")
    except KeyError:
        print("Invalid color name. Please try again.")
