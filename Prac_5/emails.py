"""
Word Occurrences
Estimate: 30 minutes
Actual:   30 minutes
"""
full_info_list = {}

email = input("Email: ")
while email != "":
    email_name = (email.split("@")[0]).split(".")
    full_name = (" ".join(email_name)).title()
    user_input = input(f"Is your name {full_name}?  (Y/n) ").upper()
    if (user_input == "Y") or (user_input == ""):
        full_info_list[email] = full_name
    else:
        full_info_list[email] = input("Name: ")
    email = input("Email: ")

for email in full_info_list:
    print(f"{full_info_list[email]} ({email})")
