import random
password = random.randint(10,50)




print("The aliens have taken over Earth!")
print("They are capturing humans")
print("We must escape")
print()
print("Oh no i forgot the password to my spaceship")
print("Its only 2 digit long and its from 10-50")
print("help me figure it out")
guess = int(input("what is number do you guess?"))
if guess == password:
    print("It worked!, let's escape")
    print("we will be stuck with each other for sometime. My name lasy")
    yoname = input("We will be stuck with each other for sometime. My name is lasy.what is your name?")
    print("Nice to meet you" + yoname + "!")
    print("lock the door. I will get us in the air")
    print("------------------------------------------------")
    print("Ok, tell me if any aliens are following us. I am going to call my friends")
    print()
    print("Me and our new friend" + yoname + "are in my spaceship. Where do you want to meet?")
    planedestination = random.randint(1,10)

    if planedestination < 5:
        print("ok got coordinates. Hey"+ yoname+ "we are meeting on a habitable system with the rest of the poopulation!")
    if planedestination > 4:
        print(yoname+ ": Oh no the aliens found us!Lasy:"" I have lost control! We are crashing!")
        print("game over")
else:

    print("ugh im so stupid. we have to find another way lets hide")
    print("Lets run to my house. Follow me! Its close by")
    print()
    print("Let me unlock it. Watch for aliens,")
    yoname = input("what is your name?")
    print("I am lasy. We will be stuck with each other for sometime" + yoname + "lets go")
    print("I did it. ... Oh no the aliens are inside but i dont see them. They left there guns on the table grab them and follow me")
    
    quietly = random.randint(1,10)

    if quietly >= 5:
        print("Yes we are in my room , you lock the door. i will call my friends for pick up")
        print()
        print("---------------")
        print("can you pick us up? there are aliens")
        print("...................")
        print("Me and our new friend " + yoname + " are in my room we will wait for you ")
        print("we will be fine.""End call")
        print("dum dum dum")
        print("The aliens found us. there about break the door.jump on my bed. i have a secret hatch to the roof")
        print("the hatch is locked and the key is either on the table or in the wardrobe. we only have time to look in one spot!")
        spot = input("where do you look? table or wardrobe?")
        if spot == "table":
            print(yoname + "Its not here. AAh the aliens")
            print()
            print("game over you lose")
        if spot == "wardrobe":
            print("Yes the key is here! We can escape!")
            print()
            print("My friends are here! Quick! Jump into the spaceship")
            print("Sara: Hello"  + yoname +  "You are part of our crew now i guess. Lasy told me about you. Our other crew member, Talia is on planet hestia.")
            print()
            trip = random.randint(1,10)
            if trip <5:
                print()
                print("Narrator: 5 minutes later...Lasy: We have landed. Everyone: Hi Talia.")
                print("Talia: Hi" + yoname + " I am talia. You have already met everyone. so lets start helping everyone else.")
                print("Sara: We are going to help people settle in this planet.")
                print("Yoname: Sounds great, i can't wait to start our new life here!")
                print("game over. You win")
            if trip > 5:
                print()
                print("There is a debris field. NOOOO, we crashed")
                print("game over. You lose")

            if trip == 5:
                print("Narrator: You find an amazing system where every planet is habitable and the entire system is concelead in a space pocket. Any ship can easily get is or out.")
                print("You call everyone there and everyone calls you hero. The team of Talia, Sara and Lasy welcome you to the crew. ")  
                print()
                print("game over.you win. legendary ending unlocked")
            
    if quietly <= 4: 
        print("Narrator:You slip in magical goo and fall to the floor with a loud thud")
        print("Lasy:Oh no the aliens spotted us!!!!")
        print("use your gun!!")
        print("game over. you lose")
