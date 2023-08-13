def extract_name(email):
    parts = email.split('@')[0].split('.')
    name_parts = [part.title() for part in parts]
    return ' '.join(name_parts)


def main():
    user_data = {}

    while True:
        email = input("Email: ")

        if email == "":
            break

        if email in user_data:
            name = user_data[email]
        else:
            name = extract_name(email)
            confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()
            if confirmation == 'n':
                name = input("Name: ")

        user_data[email] = name

    print("\nUser data:")
    for email, name in user_data.items():
        print(f"{name} ({email})")

main()
