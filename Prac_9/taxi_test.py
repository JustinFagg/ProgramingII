from Prac_9.taxi import Taxi


def main():
    """Demo test code to show how to use car class."""
    my_taxi = Taxi("Prius 1", 100)
    my_taxi.drive(40)
    print(my_taxi)
    print(f"{my_taxi.get_fare()}")
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(str(my_taxi))
    print(f"{my_taxi.get_fare()}")


main()
