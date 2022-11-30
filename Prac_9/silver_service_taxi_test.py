from Prac_9.silver_service_taxi import SilverServiceTaxi


def main():
    """Demo test code to show how to use car class."""
    my_taxi = SilverServiceTaxi("Hummer", 200, 2)
    my_taxi.drive(18)
    print(my_taxi)
    print(f"${my_taxi.get_fare()}")


main()
