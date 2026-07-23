
pi = 3.14

pino = input("do you want to use pi? (yes/no)  ")
if pino == "yes":
    for x in range(1, 13):
        print (x, "x", pi, "=", x * pi)
if pino == "no":
    table = int(input("Enter the table of: "))
    for x in range(1, 13):
        print (x, "x", table, "=", x * table)