minimal_amount = 8


def main():
    password = get_password()
    print_password_asterisks(password)


def get_password():
    user_password = input("Enter your password: ")
    while len(user_password) < minimal_amount:
        print("Error! Minimal length of password should be 8 symbols.")
        user_password = input("Enter your password: ")
    return user_password


def print_password_asterisks(password):
    print(len(password) * "*")


main()
