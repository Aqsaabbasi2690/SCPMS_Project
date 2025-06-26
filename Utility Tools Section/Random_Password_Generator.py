import random
import string
length = int(input("Enter password length: "))
# this line Combine letters, numbers, and symbols
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(length))
print("Generated password:", password)
