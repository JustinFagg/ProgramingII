def main():
    import random
    my_numbers = []
    for i in range(int(input("How many quick picks? "))):
        my_numbers_temp = []
        while len(my_numbers_temp) < 5:
            temp_random_number = random.randint(1, 45)
            if temp_random_number not in my_numbers_temp:
                my_numbers_temp.append(temp_random_number)
        my_numbers.append(my_numbers_temp)
        my_numbers_temp = []
    for i in range(len(my_numbers)):
        print(
            f"{my_numbers[i][0]:>3}{my_numbers[i][1]:>3}{my_numbers[i][2]:>3}{my_numbers[i][3]:>3}{my_numbers[i][4]:>3}")


main()