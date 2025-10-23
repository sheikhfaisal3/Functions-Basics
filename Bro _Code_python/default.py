import time 

def count(end,start=1):
    start = int(input("countdown Starting from ? : "))
    end = int(input("countdown ends at ? : "))
    if start < end :
        for  x in range (start,end+1):
            print(x)
            time.sleep(1)
        print("Countdown Done")
    else:
        if start > end:  
            for  x in range (start,end-1,-1):
                print(x)
                time.sleep(1)
        print("Reverse Countdown Done")

count(any)  

    