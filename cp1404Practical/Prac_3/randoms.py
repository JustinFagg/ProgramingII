def main():
    """
    CP1404 - Practical
    """
    import random

    print(random.randint(5, 20))  # line 1
    print(random.randrange(3, 10, 2))  # line 2
    print(random.uniform(2.5, 5.5))  # line 3

    # What did you see on line 1?
    # 5
    # What was the smallest number you could have seen, what was the largest?
    # smallest is 5 biggest is 20
    # What did you see on line 2?
    # 7
    # What was the smallest number you could have seen, what was the largest?
    # smallest is 3 largest is 9
    # Could line 2 have produced a 4?
    # no
    # What did you see on line 3?
    # 3.5163373319262208
    # What was the smallest number you could have seen, what was the largest?
    # smallest is 2.5 largest is 5.5
    print(random.randint(1, 100))


main()
