# Initial instructions for user
def initialInstruction():
    print("Welcome. Please enter 'login' to log in, or type 'signup' to create a new account")
    firstInput = input()
    return firstInput

# Method for signing up


def signUp():
    print("Creating new user account...")
    print('Please enter username:')
    username = input()
    print("Please enter password")
    password = input()
    print("Please enter password again")
    password_2 = input()
    while password != password_2:
        print('Passwords do not match, please enter again')
        password = input()
        password_2 = input()
    else:
        account_str = username + " " + password + "\n"
        database = open("database.txt", "a")
        database.write(account_str)
        database.close()
        print('Account created!')

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
