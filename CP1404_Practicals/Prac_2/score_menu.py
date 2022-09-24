def main():
    menu = """Grade score out of 100 """
    print(menu)
    user_score = int(input("> "))
    while user_score != -1:
        print(score_decoder(user_score))
        print_score_as_stars(user_score)
        print(menu)
        user_score = int(input("> "))


def score_decoder(score):
    if score < 0:
        return "Invalid score"
    elif score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_score_as_stars(user_score):
    print("*" * user_score)


main()
