user_name = input("Enter name: ")
MENU = """(H)ello
(G)oodbye
(Q)uit"""
print(MENU)
choice = input(">>>").upper()
while choice != "Q":
    if choice == "H":
        print("Hello" , user_name)
    elif choice == "G":
        print("Goodbye", user_name)
    else:
        print("Invalid choice")
    print(MENU)
    choice = input(">>>").upper()
print("Finished.")