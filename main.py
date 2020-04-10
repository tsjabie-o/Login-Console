import time
import os

# Making a clearscreen command using os


def clear(): return os.system('cls')

# Initial instructions for user


def initialInstruction():
    clear()
    print("Welcome. Please enter 'login' to log in, or type 'signup' to create a new account")
    firstInput = input()
    return firstInput

# Methods for interaction with user via print statements


def prt_signUpStart():
    clear()
    print("Preparing to create account")
    time.sleep(3)
    clear()
    time.sleep(1)
    print("Please enter a username, password, and a confirmation of your password")
    time.sleep(1)
    print("The username and password may not contain any spaces")


def prt_signUpSucces():
    clear()
    print("Passwords match")
    time.sleep(1)
    clear()
    time.sleep(1)
    print("Adding account to database. Please wait")
    time.sleep(3)
    print("Account created!")
    time.sleep(1)
    clear()
    time.sleep(1)
    print("Type 'login' to log in, or type 'signup' to create another account")


def prt_loginStart():
    clear()
    print("Preparing to log in...")
    time.sleep(2)
    clear()
    time.sleep(1)
    print("Please enter username:")


def prt_loginBadUsername():
    clear()
    print("That username does not exist.")
    time.sleep(1)
    print("Please try again. Or type 'signup' to create a new account")


def prt_loginPass(username):
    clear()
    time.sleep(1)
    print("Hi {}".format(username))
    time.sleep(1)
    print("Please enter your password")


def prt_loginIncorrPass(username):
    clear()
    time.sleep(1)
    print("Checking password...")
    time.sleep(2)
    clear()
    time.sleep(1)
    print("That password is incorrect, {}".format(username))
    time.sleep(1)
    print("Please try again")


def prt_loginSucces(username):
    time.sleep(1)
    print("Checking password...")
    time.sleep(2)
    print("Password correct")
    time.sleep(1)
    clear()
    time.sleep(1)
    print("Logging in...")
    time.sleep(3)
    clear()
    time.sleep(1)
    print("Logged in. Welcome back, {}".format(username))
# Method handling signing up


def signUp():
    prt_signUpStart()
    username = input()
    password = input()
    password_2 = input()
    while password != password_2:
        clear()
        print('Passwords do not match, please enter both again')
        password = input()
        password_2 = input()
    else:
        prt_signUpSucces()
        account_str = username + " " + password + "\n"
        database = open("database.txt", "a")
        database.write(account_str)
        database.close()
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
    prt_loginStart()
    username = input()
    while not usernameCheck(username):
        prt_loginBadUsername()
        username = input()
        if username == 'signup':
            signUp()
            break
    else:
        prt_loginPass(username)
        password = input()
        while not passwordCheck(username, password):
            prt_loginIncorrPass(username)
            password = input()
        else:
            prt_loginSucces(username)


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
