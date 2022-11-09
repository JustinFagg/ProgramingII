"""
project management
Estimate: 60 minutes
Actual:
"""

from Prac_7.project import Project

MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""


def load_file(readable_file):
    my_projects = []
    opened_file = open(readable_file, 'r')
    opened_file.readline()
    for line in opened_file:
        parts = line.strip().split('\t')
        my_projects.append(Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4])))
    print(my_projects)


def save_to_file():
    print("save")


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            file = input("FileName: ")
            load_file(file)
        elif choice == "S":
            file = input("FileName: ")
            save_to_file(file)
        elif choice == "D":
            print("D")
            # disply
        elif choice == "F":
            print("F")
            # filter
        elif choice == "A":
            print("A")
            # Addnew
        elif choice == "U":
            print("U")
            # update
        print(MENU)
        choice = input(">>> ").upper()


main()
