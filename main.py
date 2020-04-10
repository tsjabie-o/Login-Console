# Initial instructions for user
def initialInstruction():
    print("Welcome. Please enter 'login' to log in, or type 'signup' to create a new account")
    firstInput = input()
    return firstInput


# Saving initial user input
firstInput = initialInstruction()

# Checking for legit input
while firstInput != 'login' and firstInput != 'signup':
    print("Invalid input. Type 'login' to login, or 'signup' to create new account")
    firstInput = input()
else:
    print("Sure")
