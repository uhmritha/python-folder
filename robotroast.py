import random

endgame = "nothing"
while endgame != "exit":
    rudeanswer = ""
    user_reply = input("Do you like robots? (yes/no/exit) ")
    if user_reply == "exit":
        endgame = "exit"
    elif user_reply == "yes":
        print("Good, you better")
        print("lets play a game. you guess what number i am thinking of form 1, 10")
        robotnum = int(input("what number do you guess?"))
        if robotnum == random.randint(1, 10):
            print("good job looks like mortals are not stupid")
            print("game over ")
        else:
            print("wrong, you are very foolish")
            print("game over ")
    elif user_reply == "maybe":
        print("make a decision mortal")
        print("game over")
    elif user_reply == "no":
        print("how unfortunate, i didnt think i would have to term inate you")
        print("game over ")
    elif "fat" in user_reply:
        print("you will pay for your rudeness")
        rudeanswer = input("how would you like to be terminated?")
    else:
        else_reply = input("why are mortals so indecisive? Pick an answer child")
        if else_reply == "because we want to be":
            print("how stupid")
            print("game over ")
        elif else_reply == "maybe your too decisive":
            toodecisive = input("would you like to explain how that is possible?, foolish mortal")
            if toodecisive == "you dont think your actions through":
                print(" haha, you should consider checking the dictionary, clown.")
                print("game over ")
            elif toodecisive == "its okay to say you dont know":
                print("then go harder on yourself")
                print("game over ")
            elif toodecisive == "i actually dont know....its okay to say that":
                print("not with the knowlege of a robot, being human is easy")
                print("game over ")
        elif else_reply == "because we are thinking of a creative answer":
            creativeaswer = input("whats the point in a creative answer if you cant give me an answer?")
            if creativeaswer == "wouldnt you like to know":
                print("just give me an answer!!!!!!")
                print("game over ")
            elif creativeaswer == "i am thinking of one, be patient":
                print("hurry up")
                print("game over ")
            elif creativeaswer == "be quiet robot":
                print("fine, now you will know what its like when NOONE ANSWERS YOU")
                print("game over ")
            


        elif else_reply == "yes, heres your answer":
            print("finally, we robots prefer quick answers")
        elif else_reply == "no, you fat robot" or "fat" in else_reply:
            print("you will pay for your rudeness")
            
            rudeanswer = input("how would you like to be terminated?")

    if rudeanswer:
        if rudeanswer == "quickly":
            print("how boring... goodbye")
            print("game over ")
        elif rudeanswer == "slowly":
            print("perhaps you are not as boring after all... byeee")
            print("game over ")
        elif rudeanswer == "magically":
            print("interesting, get me a wand human. Time to begain termination! hahahahaha")
            print("game over you winnn!!!!!!")
        elif rudeanswer == "im sorry":
            print("too late. knife it is")
            print("game over ")
        else:
            print("Once foolish, always foolish")
            print("game over ")
        