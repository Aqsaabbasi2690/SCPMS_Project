import os
if not os.path.exists("data/logged_in.txt"):
    print("Access Denied. Please log in first.")
    exit()


import random
import string
length = int(input("Enter password length: "))
# this line Combine letters, numbers, and symbols
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(length))
print("Generated password:", password)
