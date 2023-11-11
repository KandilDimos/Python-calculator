

operator = input("Enter an operator (+ , - , * , /  ): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))


if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
else:
    print(f"{operator} is not a valid operator")

if num2 == 0:
  print(f"You can't do a division by number 0. Try again.")


if num1 == 0:
  print(f"You can't do a division by number 0. Try again.")


while True:
  operator = input("Enter an operator (+ , - , * , /  ): ")

  if operator == 'exit':
            print("Exiting the calculator.")
            break

 
            
  