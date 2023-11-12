

operator = input(f"Enter an operator (+ , - , * , / , ** ): ")
num1 = float(input(f"Enter the 1st number: "))
num2 = float(input(f"Enter the 2nd number: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    if num1 == 0:
       print(f"You can't do a multiplication by number 0. Try again.") 
    if num2 == 0:
       print(f"You can't do a multiplication by number 0. Try again.") 
    else:
        result = num1 * num2
        print(round(result, 3))

elif operator == "/":
    if num1 == 0:
     print(f"You can't do a division by number 0. Try again.")
    if num2 == 0:
     print(f"You can't do a division by number 0. Try again.")
    else:
        result = num1 / num2
        print(round(result, 3))
    result = num1 / num2
    print(round(result, 3))
elif operator == "**":
    result = num1 ** num2
    print(round(result, 3))

else:
    print(f"{operator} is not a valid operator")

if num2 == 0:
   print(f"You can't do a division by number 0. Try again.")


if num1 == 0:
    print(f"You can't do a division by number 0. Try again.")


while 1:
  operator = input(f"Enter an operator (+ , - , * , / , ** ): Or type 'exit' to exit the calculator. ")
  if operator == 'exit':
            print(f"You just exited from  the calculator.")
            break
  num1 = float(input(f"Enter the 1st number: "))
  num2 = float(input(f"Enter the 2nd number: "))

   
 
            

  if operator == "+":
    result = num1 + num2
    print(round(result, 3))
  elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
  elif operator == "*":
    if num2 == 0:
       print(f"You can't do a multiplication by number 0. Try again.") 
    if num2 == 0:
       print(f"You can't do a multiplication by number 0. Try again.") 
    else:
        result = num1 * num2
        print(round(result, 3))
  elif operator == "/":
    if num2 == 0:
     print(f"You can't do a division by number 0. Try again.")
    if num2 == 0:
     print(f"You can't do a division by number 0. Try again.")
    else:
        result = num1 / num2
        print(round(result, 3))
    result = num1 / num2
    print(round(result, 3))
  elif operator == "**":
    result = num1 ** num2
    print(round(result, 3))

  else:
    print(f"{operator} is not a valid operator")

  if num2 == 0:
   print(f"You can't do a division by number 0. Try again.")


  if num1 == 0:
    print(f"You can't do a division by number 0. Try again.")
