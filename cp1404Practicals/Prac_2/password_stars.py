def main(minimum_password_length):
    user_password = method_name(minimum_password_length)
    print_hidden_password(user_password)
    return user_password


def print_hidden_password(user_password):
    print("*" * len(user_password))


def method_name(minimum_password_length):
    user_password = input("Password: ")
    while minimum_password_length > len(user_password):
        user_password = input("Password: ")
    return user_password


main(5)

