import random

score = 0

while True:
    try:
        user_input = input("Enter rock, paper, or scissors: ").lower()

        while user_input not in ["rock", "paper", "scissors"]:
            user_input = input("Enter rock, paper, or scissors: ").lower()

        options = ["rock", "paper", "scissors"]
        computer_choice = random.choice(options)

        print(f"Computer chose: {computer_choice}")

        if user_input == computer_choice:
            print("It's a tie!")
        elif user_input == "rock":
            if computer_choice == "paper":
                print("You lose!")
            else:
                print("You win!")
                score += 1
        elif user_input == "paper":
            if computer_choice == "scissors":
                print("You lose!")
            else:
                print("You win!")
                score += 1
        elif user_input == "scissors":
            if computer_choice == "rock":
                print("You lose!")
            else:
                print("You win!")
                score += 1

        play_again = input("Do you want to play again? (y/n)").lower()
        while play_again not in ["y", "n"]:
            play_again = input("Do you want to play again? (y/n)").lower()

        if play_again != "y":
            print(f"Your score is: {score}")
            break

    except KeyboardInterrupt:
        print(f"\nYour score is: {score}")
        print("You exited the game!")
        break