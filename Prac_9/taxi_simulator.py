from Prac_9.silver_service_taxi import SilverServiceTaxi
from Prac_9.taxi import Taxi

MENU = """q)uit, c)hoose taxi, d)rive\n>>> """


def main():
    """Demo test code."""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    bill_to_date = 0
    print("Let's drive!")
    choice = (input(MENU)).lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available: ")
            i = 0
            for taxi in taxis:
                print(f"{i} - {taxi}")
                i += 1
            current_taxi = int(input("Choose taxi: "))
            if current_taxi > len(taxis) - 1:
                print("Invalid taxi choice")
        elif choice == "d":
            if not current_taxi:
                print("You need to choose a taxi before you can drive")
            else:
                print(f"{taxis[current_taxi]}")
                taxis[current_taxi].drive(int(input("Drive how far? ")))
                print(f"Your {taxis[current_taxi].name} trip cost you ${taxis[current_taxi].get_fare()}")
                bill_to_date =+ taxis[current_taxi].get_fare()
        print(f"Bill to date: {bill_to_date}")
        choice = (input(MENU)).lower()


main()


