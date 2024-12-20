import hashlib

# Ask the user for the SHA-256 hash they want to crack
hash_to_crack = input("💥 Enter SHA-256 hash value to bruteforce: ").strip()

# Path to the wordlist (make sure this points to your actual file)
wordlist_path = '/home/kali/Downloads/wordlist.txt'

# Read the wordlist and try to match the hash
try:
    with open(wordlist_path, 'r') as f:
        for line in f:
            password = line.strip()
            # Calculate the SHA-256 hash
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            if hashed_password == hash_to_crack:
                print(f"Password found: {password}")
                break
        else:
            print("Password not found in the wordlist.")
except FileNotFoundError:
    print(f"Error: Wordlist file not found at {wordlist_path}. Please check the path.")
