import random
password = []
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!#$%&()*+"
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))

for i in range(0, nr_letters):
    password.append(letters[i])
for i in range(0, nr_symbols):
    password.append(symbols[i])
for i in range(0, nr_numbers):
    password.append(numbers[i])
    
random.shuffle(password)
password = "".join(password)
print(f"Your password is: {password}")