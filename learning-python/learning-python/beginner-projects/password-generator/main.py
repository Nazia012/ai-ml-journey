import random

chars = "abcdef12345"

length = int(input("Enter password length: "))

password = ""

for i in range(length):
    password += random.choice(chars)

print(password)
