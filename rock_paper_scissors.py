import random
user= int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
comp= random.randint(0,2)
print(f"Computer chose: {comp}")
if user == comp:
    print("It's a draw!")
elif (user == 0 and comp == 2) or (user == 1 and comp == 0) or (user == 2 and comp == 1):
    print("You win!")
else:
    print("You lose!")