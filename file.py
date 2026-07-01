import random

exitchoice = "nothing"
while exitchoice != "exit":
    print("you are in a very mysterious castle")
    print("there are 4 doors, Choose, 1, 2, 3, 4, or 5")
    playerchoice = input("Which door do you choose? ")
    
    if playerchoice == "1":
        print("there is a sleepy lion in the room")
        print("you can sneak behind him or steal his keys. Choose 1 for sneaking and 2 for stealing")
        lion = input("what do you choose to do? ")
        if lion == "1":
            print("the lion wakes up and eats you")
        elif lion == "2":
            print("good job you succesfully grabbed his keys and now can escape the castle")
            print("game over you win")
        else:
            print("nothing happens")

    elif playerchoice == "2":
        print("there is and angry ogre, he hits you with his bat")
        print("game over you lose")

    elif playerchoice == "3":
        print("there is a fire breathing dragon")
        print("burns you to a crisp")
        print("game over you lose")

    elif playerchoice == "4":
        print("there is a witch's room but the witch is in the shower")
        print("you can either run out the door and out of the castle or steal her potions. choose 1 for run and 2 for steal")
        witch = input("what do you choose?")
        if witch == "1":
            print("the door is locked the witch finds you and you die!")
            print("game over you lose!")
        elif witch == "2":
            print("you grab her potions but the witch comes out of the shower. You throw the potions at her and she turns into a frog!")
            print("you go to a different door and try again")

    elif playerchoice == "5":
        print("you enter a room with a sphinx")
        print("Guess what number the sphinx is thinking of (between 1-10)")
        number = int(input("what number do you think it is?"))
        if number == random.randint(1, 10):
            print("you may pass")
            print("game over you win")
        else:
            print("you guess the wrong number the sphinx eats you")
            print("game over you lose!")

    else:
        print("you went through a non - existant door,")
        print("game over you lose!")
