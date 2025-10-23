#Table using function metho you can choose range as well .

def table(x,yr):
    x = int(input("Which number's table should i show you : "))
    yr = int(input("Enter the range ('starting is 1') choose ending  : "))
    print(f"----------Table of {x} form 1 to {yr}----------")
    for i in range(yr):
        print(x,"*", i+1 ,"=",x*(i+1) )
    print("---------------END------------------")
table(any,any)
