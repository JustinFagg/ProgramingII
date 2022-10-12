"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data"


def main():
    data = get_data()
    print(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    list_of_info = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        list_of_info.append(parts)
    input_file.close()
    display_info(list_of_info)


def display_info(list_of_info):
    for i in range(0, len(list_of_info), 1):
        print(f"{list_of_info[i][0]} is taught by {list_of_info[i][1]} and has {list_of_info[i][2]} students")


main()