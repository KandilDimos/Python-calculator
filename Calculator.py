operator = input("Enter an operator (+ , - , x , /  ): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))


if operator == "+":
    result = num1 + num2   
    print(result)
if operator == "-":
    result = num1 - num2       
if operator == "x":
    result = num1 * num2 
    print(result)  
if  operator == "/":
    result = num1 / num2 
    print (f"The result is : {round(result, 3)}")
    



else:
   


   print(f"{operator} is an  invalid operator")
