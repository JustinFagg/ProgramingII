"""
Client side reading guitars.csv
"""

from Prac_6.guitar import Guitar

FILE = 'guitars.csv'


def main():
    my_guitars = []
    opened_file = open(FILE, 'r')
    opened_file.readline()
    for line in opened_file:
        parts = line.strip().split(',')
        my_guitars.append(Guitar(parts[0], int(parts[1]), float(parts[2])))

    for i in range(len(my_guitars)):
        is_guitar_vintage_string = "(vintage)" if my_guitars[i].is_vintage() else ""
        print(f"Guitar {i + 1}: {my_guitars[i].name:>25} ({my_guitars[i].year:>4}),"
              f" worth $ {my_guitars[i].cost:10,.2f} {is_guitar_vintage_string}")


main()
