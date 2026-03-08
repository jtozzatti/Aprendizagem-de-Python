user_name = input("enter a user name: ")

if len(user_name) > 12:
    print("your username can't be more than 12 characters")

elif user_name.find(" ") != -1:
    print("your username can't contain spaces")

else:
    print(f"successful, welcome {user_name}")