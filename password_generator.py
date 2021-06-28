# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

pass_word = ""
for i in range(1, nr_letters + 1):
    pass_word += random.choice(letters)

for i in range(1, nr_numbers + 1):
    pass_word += random.choice(numbers)

for i in range(1, nr_symbols + 1):
    pass_word += random.choice(symbols)

# for i in range(0, nr_letters):
#     ind = random.randint(0, len(letters) - 1)
#     pass_word += letters[ind]
#
# for i in range(0, nr_numbers):
#     ind = random.randint(0, len(numbers) - 1)
#     pass_word += numbers[ind]
#
# for i in range(0, nr_symbols):
#     ind = random.randint(0, len(symbols) - 1)
#     pass_word += symbols[ind]


# Easy version
print(f"Easy version.\nYour password is {pass_word}")

# Hard version
password_list = []
for i in range(0, nr_letters):
    ind = random.randint(0, len(letters) - 1)
    password_list += letters[ind]

for i in range(0, nr_numbers):
    ind = random.randint(0, len(numbers) - 1)
    password_list += numbers[ind]

for i in range(0, nr_symbols):
    ind = random.randint(0, len(symbols) - 1)
    password_list += symbols[ind]

print(password_list)
random.shuffle(password_list)
print(password_list)
pass_word = str.join("", password_list)
# Easy version
print(f"Hard version.\nYour password is {pass_word}")