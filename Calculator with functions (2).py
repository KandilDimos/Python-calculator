def get_operator():
   operator = input("Enter an operator (+ , - , / , * , **)")
   if operator != "+" and  operator != "-" and operator != "/"  and operator != "*" and operator != "**":
      print("Invalid operator. Try again")
      get_operator()
   return operator
   

def get_num1():
   num1 = float(input("Enter the 1st number: "))
   return num1

def get_num2():   
   num2 = float(input("Enter the 2nd number: "))
   return num2
   
def operation(a,b,c):   
   if a == "+":
      result = b + c
      return (round(result, 3))
   elif a == "-":
      result = b - c
      return (round(result, 3))
   elif a == "*":
      result = b * c
      return (round(result, 3))
   elif a == "/":
      if c == 0:
         print(f"You can't do a division by number 0. Try again.")
      else:
         result = b / c
         return (round(result, 3))
   elif a == "**":
      result = b ** c
      return (round(result, 3))

def calc():
   operator = get_operator()
   while(operator != "exit"):
      result = operation(operator,get_num1(),get_num2())
      print(f"Result is = {result}")
      operator = get_operator()
   else:
      print("You exited the programme.")  

calc()




