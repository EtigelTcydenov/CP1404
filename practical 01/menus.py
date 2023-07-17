name = input("Enter name: ")
choice = input("(H)ello\n(G)oodbye\n(Q)uit\n")
while choice != "Q":
    if choice == "H":
        print("Hello,", name)
    elif choice == "G":
        print("Goodbye ",name)
    else:
        print("Invalid number")
    name = input("Enter name: ")
    choice = input("(H)ello\n(G)oodbye\n(Q)uit\n")
print("Finished")