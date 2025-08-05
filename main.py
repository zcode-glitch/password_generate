import random
import string

print("Welcome to the Password Generator! By ZCode")
print("This program will generate a random password for you.")

while True:
    len_password = int(input("Enter how long you want your password to be: "))
    if len_password < 7 or len_password > 9:
        print("Password length must be 8 characters. Please try again.")
        continue

    low = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation	

    ress = low + upper + num + symbols

    backup = random.sample(ress,len_password)
    password = "".join(backup)

    print(password)
    
    cont = input("Do you want to generate another password? (yes/no): ").lower()
    if cont == 'yes':
        print("Exiting the password generator.")
        break
    elif cont == 'no':
        continue