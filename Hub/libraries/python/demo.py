generated_password = input("SET PASSWORD: ") # Asks for a password input to generate
password = input("PASSWORD: ") # Asks for a password input

if generated_password == "" or password == "": # Checks for nil inputs
    print("Inputs were found nil")
    exit() # stops continuing program

if password == generated_password: # Compares the input string to correct password var
    name = input("NAME: ") # Name input
    if name == "Ai": # Checks the validity of the user
        print(f"Welcome, {name}")
        print() # Blank line
    else:
        print("User not valid")
else:
    print("Incorrect Password!")