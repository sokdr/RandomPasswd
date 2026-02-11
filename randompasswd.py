import secrets
import string

print("*" * 50) 
print("Welcome to the password generator\n ")
print("*" * 50)



def password_generator():

    while True:
        pass_length = int(input("Please enter the password length: Please choose between 12 and 20 characters length: "))
        if pass_length < 12 or pass_length > 20:
            print(f"Enter between 12 and 20 characters. ")
            continue

        for passwd in range(3):
            password = "".join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for passwd in range(pass_length))
            print(password)


        

password_generator()
