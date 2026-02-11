import random
item_list=["Rock","Paper","scissor"]
user_choice=input("Enter your Move : Rock, Paper, Scissor = ")
computer_choice=random.choice(item_list)
print(f"User choice = {user_choice}, Computer Choice = {computer_choice}")
if user_choice == computer_choice:
    print("Both chooses same:= Match Tie")
elif user_choice =="Rock":
    if computer_choice =="Paper":
        print("Papers covers Rock = Computer Wins")
    else:
        print("Rock Smashes Scissor = You Wins")
elif user_choice == "Paper":
    if computer_choice == "Scissor":
        print("Scissor cuts paper = Computer Wins")
    else:
        print("Papers covers rock = You Wins")
elif user_choice == "Scissor":
    if computer_choice == "Paper":
        print("Scissor cuts paper = You Wins")
    else:
        print("Rocks Smashes Scissor = You Wins")