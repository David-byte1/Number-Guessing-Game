import random
while True: #outer loop controls replay
    #select difficulty level
    while True:
        #loop until a valid difficulty level is selected
        difficulty = input("Select difficulty level (easy, medium, hard): ").strip().lower()
        if difficulty == "easy":
        #pick a number from 1 to 10
            secret_number = random.randint(1, 10)
            max_number = 10
            break
        elif difficulty == "medium":
            #pick a number from 1 to 20
            secret_number = random.randint(1, 20)
            max_number = 20
            break
        elif difficulty == "hard":
            #pick a number from 1 to 50
            secret_number = random.randint(1, 50)
            max_number = 50
            break
        else:
            print("Invalid difficulty level! Please choose easy, medium, or hard.")
            #count the number of attempts
    attempts = 0
    max_attempts = 3
        #check if the guess is correct
    while attempts <max_attempts:
        try:
            #ask the player to guess the number
            guess = int(input(f"Guess a number between 1 and {max_number}: "))
            attempts += 1
            if guess == secret_number:
            #if guess is correct, congratulate the player
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
            elif guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")    
        except ValueError:
            print(f"Invalid input! Please enter a number between 1 and {max_number}.")
        continue
    if attempts == max_attempts and guess != secret_number:
        # If the user has used all attempts, reveal the secret number           
        print(f"Sorry, you've used all {max_attempts} attempts. The secret number was {secret_number}.")        
        #replay the game
    replay = input("Do you want to play again? (yes/no): ").strip().lower()
    if replay != "yes":
        print("Thanks for playing!")
        break

        