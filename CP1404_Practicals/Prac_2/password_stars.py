minimum_password_length = int(input("Password Length: "))
user_password = input("Password: ")
while minimum_password_length > len(user_password):
    print("Password needs to be longer")
    user_password = input("Password: ")
print("*" * len(user_password))
