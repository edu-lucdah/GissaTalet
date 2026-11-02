import random as rand

namn = input("Vad heter du? ->")

print(f"Hej {namn} och välkommen till spelet")



for i in range(3):
    
    slump = rand.randint(1,10)
    
    giss = int(input(f"Försök {i+1} Gissa talet mellan 1-10 ->"))

    if giss == slump:
        print("Rätt!")
        break
    else:
        print(f"Tyvärr, det var {slump}")