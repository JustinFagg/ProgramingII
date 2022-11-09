"""
project management
Estimate: 60 minutes
Actual: Has been 40 mins to this point, Break time
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
    opened_file.close()
    return my_projects


def save_to_file(writable_file, my_projects):
    opened_file = open(writable_file, 'w')
    for i in range(len(my_projects)):
        print(
            f"{my_projects[i].name}\t{my_projects[i].start_date}\t{my_projects[i].priority}\t{my_projects[i].cost_estimate}\t{my_projects[i].completion_percentage}",
            file=opened_file)


def main():
    my_projects = []
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            file = input("FileName: ")
            my_projects = load_file(file)
        elif choice == "S":
            file = input("FileName: ")
            save_to_file(file, my_projects)
        elif choice == "D":
            print("D")
            # display
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
