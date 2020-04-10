# Initial instructions for user
def initialInstruction():
    print("Welcome. Please enter 'login' to log in, or type 'signup' to create a new account")
    firstInput = input()
    return firstInput

# Method for signing up


def signUp():
    print("Preparing to create new account")
    print('Please enter username:')
    print("Usernames may not contain spaces!")
    username = input()
    print("Thank you. Please enter password. \nPasswords may not contain spaces either!")
    password = input()
    print("For confirmation, please enter password again")
    password_2 = input()
    while password != password_2:
        print('Passwords do not match, please enter both again')
        password = input()
        password_2 = input()
    else:
        print("Passwords match!")
        print("Adding account to database")
        account_str = username + " " + password + "\n"
        database = open("database.txt", "a")
        database.write(account_str)
        database.close()
        print('Account created!')
        print("To login, type 'login', to create another account type 'signup'")
        userinput = input()
        while userinput != 'login' and userinput != 'signup':
            print(
                "Invalid input. Type 'login' to login, or 'signup' to create new account")
            userinput = input()
        else:
            if userinput == 'login':
                login()
            else:
                signUp()

# Method for login


def login():
    print("Please enter username")
    username = input()
    while username != "tsjabie.o":
        print("That's not a username I know \nPlease enter a valid username or type 'signup' to create a new account")
        username = input()
        if username == 'signup':
            signUp()
            break
    else:
        print("Enter password:")
        password = input()
        while password != "pphard":
            print("Password not correct. Please try again")
            password = input()
        else:
            print("Succesfully logged in!")


# Saving initial user input
firstInput = initialInstruction()

# Checking for legit input, asking user again if not legit
while firstInput != 'login' and firstInput != 'signup':
    print("Invalid input. Type 'login' to login, or 'signup' to create new account")
    firstInput = input()
else:
    if firstInput == "signup":
        signUp()
    else:
        login()
