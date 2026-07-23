import random
number = random.randint(1,20)
guess = 0
chances = 4
exit = 0
print("Its me the sphinx from door 5 of the castle of doors")
play = input("Do you want to play a game?(yes/no): ").strip().lower()
while exit != 1:
    if play == "yes":
        for i in range(chances):
            guess = int(input("guess the number from 1-20: "))

            if guess > number:
                print("too high")
            elif guess < number:
                print("too low")
            elif guess == number:
                print("you got it right!")
                print("Your turn. you think of a number. I will try to guess it")
                
                low = 1
                high = 20
                sphinx_wonrch = False
                
                for x in range(chances):
                    if low > high:
                        print("YOU CHEATED! i AM GOING TO EAT YOU!")
                        sphinx_wonrch = True
                        break
                    yoturn = random.randint(low, high)
                    print("my guess is ", yoturn)
                    accuracy = input("is it higher, lower, or correct?: ").strip().lower()
                    
                    if accuracy == "correct":
                        print("Haha! I got it right!")
                        sphinx_wonrch = True
                        break
                    elif accuracy == "higher":
                        low = yoturn + 1
                    elif accuracy == "lower":
                        high = yoturn - 1
                    else:
                        print("Please type 'higher', 'lower', or 'correct'.")
                
                if not sphinx_wonrch:
                    print("Aw, I ran out of guesses! You win the overall game!")
                
                exit = 1
                break
        else:
            print("you ran out of guesses.The number was " , number)
            print("hahaha. I am going to eat you!")
            exit = 1
    elif play == "no":
        exit = 1

    
