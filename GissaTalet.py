import random as rand

namn = input("Vad heter du? ->")

print(f"Hej {namn} och välkommen till spelet")

slump = rand.randint(1,10)

giss = int(input("Gissa ett tal mellan 1-10 ->"))

if giss == slump:
    print("Rätt!")
else:
    print(f"Tyvärr, det var {slump}")