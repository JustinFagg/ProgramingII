"""
CP1404/CP5632 - Practical
"""

NAME_FILE = "name.txt"
NUMBER_FILE = "numbers.txt"


def main():
    """
    Write and read to two different files.
    """
    writing_user_name()
    reading_user_name()
    adding_first_two_lines()
    adding_all_numbers()


def writing_user_name():
    """
    Write user input to NAME_FILE.
    """
    user_name = input("My name is ")
    current_file = open(NAME_FILE, 'w')
    print(user_name, file=current_file)
    current_file.close()


def reading_user_name():
    """
    Print name from NAME_FILE
    """
    current_file = open(NAME_FILE, 'r')
    print(f"Your name is {current_file.read()}")
    current_file.close()


def adding_first_two_lines():
    """
    Add first two numbers together of NUMBER_FILE.
    """
    current_file = open(NUMBER_FILE, 'r')
    first_number_in_file = int(current_file.readline())
    second_number_in_file = int(current_file.readline())
    print(first_number_in_file + second_number_in_file)
    current_file.close()


def adding_all_numbers():
    """
    Add all numbers of NUMBER_FILE.
    """
    current_file = open(NUMBER_FILE, 'r')
    total_value = 0
    for line in current_file:
        total_value = total_value + int(line)
    print(total_value)
    current_file.close()


main()
