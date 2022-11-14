"""
Client side reading guitars.csv
"""

from Prac_6.guitar import Guitar

FILE = 'guitars.csv'


def main():
    my_guitars = []
    opened_file = open(FILE, 'r')
    for line in opened_file:
        parts = line.strip().split(',')
        my_guitars.append(Guitar(parts[0], int(parts[1]), float(parts[2])))
    opened_file.close()

    my_guitars.sort()

    for i in range(len(my_guitars)):
        is_guitar_vintage_string = "(vintage)" if my_guitars[i].is_vintage() else ""
        print(f"Guitar {i + 1}: {my_guitars[i].name:>25} ({my_guitars[i].year:>4}),"
              f" worth $ {my_guitars[i].cost:10,.2f} {is_guitar_vintage_string}")

    guitar_name = input("Name: ")
    while guitar_name != "":
        my_guitars.append(Guitar(guitar_name, int(input("Year: ")), float(input("Cost: "))))
        guitar_name = input("Name: ")

    opened_file = open(FILE, 'w')
    for i in range(len(my_guitars)):
        print(f"{my_guitars[i].name},{my_guitars[i].year},{my_guitars[i].cost}", file=opened_file)
    opened_file.close()


main()
