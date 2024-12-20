import random
import string

def generate_password(length=12):
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    email = "   "  # Using your specified email
    print(f"Generating passwords for: {email}\n")
    length = int(input("Enter desired password length: "))

    # Infinite loop to generate passwords
    while True:
        password = generate_password(length)
        print(f"Generated password: {password}")
        

if __name__ == "__main__":
    main()
