def calc(number1,operator,number2):
   number1 = int(input("Enter 1st number : "))
   operator = input("Choose any Opertaor ( - , + , * , / ) : ")
   number2 = int(input("Enter 2nd number : "))
   if operator == "+":
        return number1 + number2
   elif operator == "-":
        return number1 - number2
   elif operator == "*":
        return number1 *number2
   elif operator == "/":
        return number1 / number2
   else :
        return (f"{(operator)} is invalid")
   
        
   
Calculating = True
while Calculating:
    calculator = calc(any,any,any)
    print(f"Your Total = {calculator:.2f}")
    if Calculating == False:
        break
    