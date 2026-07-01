password = "STILNONEOFYOBUISNESS"
aliens = 50




print("Oh no aliens are invading earth!")
print("We need to figure out the password so we can acess Earth's global protection system")
print()
print("-------------------------------------------------------------")
print("      WELCOME TO THE GLOBAL PROTECTION SYSTEM")
print("-------------------------------------------------------------")
print("       (please enter the password)")
print()

while aliens < 10000:   
    guess = input("what is the password?").upper()
     
    if guess == password:
    
        print()
        print("We unlocked the weapons!!! Lets destroy the aliens!! hahahahahhhahahahhahahhahah")
        break

    else:
        print()
        print("wrong password")
        aliens = aliens ** 2

    if aliens > 10000:
        print("No we failed!!!!!! Come we must jump into my spaceship!")
        
        break
    

