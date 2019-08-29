import random




def guessGame():

    random_number = random.randrange(1, 50000)
    win = False

    print("This is a guessing game.\n")
    print("I'll think of a number between one and fifty thousand\n",
          "and you have 20 guesses to get it right!\n")
    print("Oh, and I'll let you know if you guess high or low.\n")
    print("Wait! Do you want more detailed hints or less detailed hints?\n")
    difficulty = input("Type \'more\' or \'less\'\n")
    difficulty = difficulty.lower()

    if difficulty != "more" and difficulty != "less":
        print("Well, I don't understand your preference...\n\n",
              "oh well, we'll play anyway, with the more detailed hints.\n")
        difficulty = "more"
        
    if difficulty == "more":
        print("This is the easier difficulty.\n")
        count = 0
        while count < 21 and not win:
            if count == 19:
                print("Last guess! Good luck... \n")
            user_guess = int(input("What's your guess?\n"))
            count += 1
            print("Guess", count)
            if user_guess < 1 or user_guess > 50000:
                print("Your guess is out of range, please play nicer next time.\n")
            if user_guess == 1022:
                print("Your name's not Vanessa is it? LOL.\n")
            if user_guess == random_number:
                print("Congratulations!! You win!!\n", "It took you %s tries.\n" % count)
                win = True
            elif user_guess > random_number:
                if user_guess - random_number < 9:
                    print("You guessed high, and you're SUPER close.\n")
                elif user_guess - random_number < 49:
                    print("You guessed high, and you're very close.\n")
                elif user_guess - random_number < 99:
                    print("You guessed high, and you're close.\n")
                elif user_guess - random_number < 249:
                    print("You guessed high, and you're getting closer.\n")
                elif user_guess - random_number < 499:
                    print("You guessed high, and you're closing in on it.\n")
                elif user_guess - random_number < 999:
                    print("You guessed high, and you're in the ballpark.\n")
                elif user_guess - random_number < 2499:
                    print("You guessed high, and you're in the same city.\n")
                elif user_guess - random_number < 4999:
                    print("You guessed high, and you're getting warmer.\n")
                elif user_guess - random_number < 9999:
                    print("You guessed high, and you're still a ways off.\n")
                elif user_guess - random_number < 14999:
                    print("You guessed high, and you're not close.\n")
                elif user_guess - random_number < 19999:
                    print("You guessed high, and yet you're super cold.\n")
                else:
                    print("You guessed high, and you're basically a million or more off.\n")
            elif user_guess < random_number:
                if random_number - user_guess < 9:
                    print("You guessed low, and you're SUPER close.\n")
                elif random_number - user_guess < 49:
                    print("You guessed low, and you're very close.\n")
                elif random_number - user_guess < 99:
                    print("You guessed low, and you're close.\n")
                elif random_number - user_guess < 249:
                    print("You guessed low, and you're getting closer.\n")
                elif random_number - user_guess < 499:
                    print("You guessed low, and you're closing in on it.\n")
                elif random_number - user_guess < 999:
                    print("You guessed low, and you're in the ballpark.\n")
                elif random_number - user_guess < 2499:
                    print("You guessed low, and you're in the same city.\n")
                elif random_number - user_guess < 4999:
                    print("You guessed low, and you're getting warmer.\n")
                elif random_number - user_guess < 9999:
                    print("You guessed low, and you're still a ways off.\n")
                elif random_number - user_guess < 14999:
                    print("You guessed low, and you're not close.\n")
                elif random_number - user_guess < 19999:
                    print("You guessed low, and you're super cold.\n")
                else:
                    print("You guessed low, and you're like, a million or more off.\n")
        if count == 21:
            print("Too bad, you lost, game over, man, game over.\n")

    else:
        print("Okay, this is the harder difficulty.\n")
        count = 0
        while count < 21 and not win:
            if count == 19:
                print("Last guess! Good luck... \n")
            user_guess = int(input("What's your guess?\n"))
            count += 1         
            print("Guess", count)
            if user_guess < 1 or user_guess > 50000:
                print("Your guess is out of range, please play nicer next time.\n")
            if user_guess == 1022:
                print("Your name's not Vanessa, is it? LOL!\n")
            if user_guess == random_number:
                print("Congratulations!!! You win!!\n")
                print("It took you %s tries to get it.\n" % count)
                win = True
            elif user_guess > random_number:
                print("You guessed high.\n")
            elif user_guess < random_number:
                print("You guessed low.\n")
        if count == 21:
            print("Game over. You lose.", "A loo hoo, ser.\n")
    print("Thanks for playing!\n\n")
    
        

play = input("Want to play?  y/n?")

    
while play == "y":
    print("Great, let's play!")
    guessGame()
    play = input("want to play again? y/n?\n")

if play == "n":
    print("Okay, well, that's fine, I guess.")
