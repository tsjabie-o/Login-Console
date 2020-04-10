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

# Checks if given password and username match, report true or false


def passwordCheck(username, password):
    database = open('database.txt', 'r')
    for line in database:
        words = line.split()
        if words[0] == username and words[1] == password:
            database.close()
            return True
    database.close()
    return False

# Checks if given username exists, reports true or false


def usernameCheck(username):
    database = open('database.txt', 'r')
    for line in database:
        words = line.split()
        if words[0] == username:
            database.close()
            return True
    database.close()
    return False

# Starts the logging in process


def login():
    print("Please enter your username")
    username = input()
    while not usernameCheck(username):
        print(
            "That is not an existing username.\nPlease try again or type 'signup' to signup")
        username = input()
        if username == 'signup':
            signUp()
            break
    else:
        print("Enter your password")
        password = input()
        while not passwordCheck(username, password):
            print("Incorrect password, please try again")
            password = input()
        else:
            print("Logged in!")


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
