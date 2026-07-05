import random
number = random.randint(1,20)
guess = 0
chances = 4
print("Its me the sphinx from door 5 of the castle of doors")
for i in range(chances):
    guess = int(input("guess the number from 1-20: "))

    if guess > number:
        print("too high")
    elif guess < number:
        print("too low")
    elif guess == number:
        print("you got it right!")
        break
else:
    print("you ran out of guesses. hahaha! I am going to eat you")
