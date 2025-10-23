import random 

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

dice = []
total =0 
num_of_dice =int(input("How many dice? : "))
#loop for adding random numbe in list.
for j in range (num_of_dice):     #here  random numbes from user decides how many times loop work.
    dice.append(random.randint(1,6))  #here numbers from 1 to 6 gets add into the list of dice and .
#loop for dice display
for i in range (num_of_dice):        #here we can acess list items one by one.
    for line in dices.get(dice[i]):    #with help of we can get the dice we had to print
        print(line)
# for line in range (5):
#     for die in dice:
#         print(dices.get(die)[line],end=" " )
#     print()


#loop for total
for k in dice :
    total += k
print(f"total = {total}")
