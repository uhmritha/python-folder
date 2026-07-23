import random 

place = ["pluto", "moon", "somewhere over the rainbow", "outer space", "mars"]
person1 = ["an assassin", "a detective", "a spy", "a ninja", "a pirate"]
verb = ["killing", "meeting", "stealing", "trading", "exploring"]
person2 = ["a wizard", "a fairy", "a robot", "a ghost", "a mermaid"]
said1 = ["I will kill you.", "Give me your gold.", "You are fat.", "Do you want to rob a bank?"]
said2 = ["Give me your soul!", "You are a fool!", "Never!", "Let's do it!"]
item = ["sword", "shield", "banana", "magic wand", "laser gun"]

# Using f-strings makes string concatenation much cleaner and easier to read
print(f"{random.choice(person1)} was walking around {random.choice(place)} when they were {random.choice(verb)} {random.choice(person2)} who said \"{random.choice(said1)}\" and {random.choice(person2)} said \"{random.choice(said2)}\"") 
print(f"Suddenly {random.choice(person1)} grabbed a {random.choice(item)} and started {random.choice(verb)} {random.choice(person2)}")
print(f"then a group of {random.choice(person1)} {random.choice(verb)} {random.choice(person2)} who said \"{random.choice(said1)}\" and {random.choice(person2)} said \"{random.choice(said2)}\"")
print(f"then the ghost got bored and grabbed a {random.choice(item)} and said {random.choice(said1)} and then {random.choice(verb)} and ran away screaming {random.choice(said2)}")