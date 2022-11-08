"""
Client side playing Guitar class.
"""

from Prac_6.guitar import Guitar


def main():
    my_guitars = []
    guitar_name = input("Name: ")
    while guitar_name != "":
        my_guitars.append(Guitar(guitar_name, int(input("Year: ")), float(input("Cost: "))))
        guitar_name = input("Name: ")

    print("\n... snip ...\n\nThese are my guitars:")
    for i in range(len(my_guitars)):
        is_guitar_vintage_string = "(vintage)" if my_guitars[i].is_vintage() else ""
        print(f"Guitar {i + 1}: {my_guitars[i].name:>25} ({my_guitars[i].year:>4}),"
              f" worth $ {my_guitars[i].cost:10,.2f} {is_guitar_vintage_string}")


main()
