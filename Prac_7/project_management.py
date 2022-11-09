"""
project management
Estimate: 60 minutes
Actual: Has been 120 mins
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
        print(my_projects[i].__repr__(), file=opened_file)


def display_projects(projects):
    sorted_projects = sorted(projects)
    completed_projects = [sorted_projects[i] for i in range(len(sorted_projects)) if sorted_projects[i].is_completed()]
    uncompleted_projects = [sorted_projects[i] for i in range(len(sorted_projects)) if
                            not sorted_projects[i].is_completed()]
    print("Completed projects:")
    for project in completed_projects:
        print(project)
    print("Uncompleted projects:")
    for project in uncompleted_projects:
        print(project)


def display_filtered_projects(projects, date):
    date = date.split("/")
    year = date[2]
    month = date[1]
    day = date[0]
    for project in sorted(projects, key=lambda x: (x.start_year, x.start_month, x.start_day)):
        if project.start_year > year:
            print(project)
        elif project.start_year == year:
            if project.start_month > month:
                print(project)
            elif project.start_month == month:
                if project.start_day >= day:
                    print(project)


def add_new_project():
    return Project(input("Name: "), input("Start Date: "), int(input("Priority: ")), float(input("Cost Estimate: $")),
                   int(input("Completion Percent: ")))


def update_project(projects):
    for i in range(len(projects)):
        print(f"{i} {projects[i]}")
    choice = int(input("Project to Modify: "))
    projects[choice].priority = int(input("New Priority: "))
    projects[choice].completion_percentage = int(input("New Percentage: "))
    return projects


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
            display_projects(my_projects)
        elif choice == "F":
            display_filtered_projects(my_projects, input("Date "))
        elif choice == "A":
            my_projects.append(add_new_project())
        elif choice == "U":
            my_projects = update_project(my_projects)
        print(MENU)
        choice = input(">>> ").upper()


main()
