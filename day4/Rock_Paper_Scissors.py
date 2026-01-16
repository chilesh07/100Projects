import random
# 0 = Rock , 1 = Paper , 2 = Scissor


user_choice = int(input("Enter your choice (0 Rock, 1 Paper, 2 Scissors) : "))
computer_choice= random.randint(0,2)
print(f"computer chose {computer_choice}")

if user_choice >= 3 or user_choice < 0:
    print('Invalid Choice! You lose')
elif user_choice == 0 and  computer_choice == 2 :
    print('You Won!')
elif computer_choice == 0 and  user_choice == 2 :
    print('You Lose!')
elif user_choice > computer_choice:
    print('You Win!')
elif computer_choice > user_choice:
    print('You Lose!')
else:
    print('Its a Draw!')





