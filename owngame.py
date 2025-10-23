import random

#you can juss roll the dice to get any random num b/w 1 and 6 (1 and 6 included).
dices ={
    1:("┌─────────┐", 
       "│         │", 
       "│    ●    │", 
       "│         │", 
       "└─────────┘" ),
    2:("┌─────────┐", 
       "│         │", 
       "│  ●   ●  │", 
       "│         │", 
       "└─────────┘" ), 
    3:("┌─────────┐", 
       "│ ●       │", 
       "│    ●    │", 
       "│       ● │", 
       "└─────────┘" ), 
    4:("┌─────────┐", 
       "│  ●   ●  │", 
       "│         │", 
       "│  ●   ●  │", 
       "└─────────┘" ),
    5:("┌─────────┐", 
       "│  ●   ●  │", 
       "│    ●    │", 
       "│  ●   ●  │", 
       "└─────────┘" ),
    6:("┌─────────┐", 
       "│  ●   ●  │", 
       "│  ●   ●  │", 
       "│  ●   ●  │", 
       "└─────────┘" ),           
}

while True:
    dice =random.randint(1,6)
    user = input("Press 'r' for Dice Roll : ")
    if user == "r":
            for i in dices.get(dice):
                print(i)
    else:
         print(f"{user} is invalid")            
            
