def get_operator():
    operator = input("Enter an operator (+ , - , /, * , **) or type 'exit' to exit. ")
    if operator != "+" and  operator != "-" and operator != "/"  and operator != "*" and operator != "**" and operator != "exit":
        print("Invalid operator. Try again.")
        get_operator()
    return operator

def get_num1():
    num1 = float(input("Enter the 1st number: "))
    return num1

def get_num2():
    num2 = float(input("Enter the 2nd number: "))
    return num2

def operation(a, b, c):
    if a == "+":
        return round(b + c, 3)
    elif a == "-":
        return round(b - c, 3)
    elif a == "*":
        return round(b * c, 3)
    elif a == "/":
        if c == 0:
            print("You can't divide by 0. Try again.")
        else:
            return round(b / c, 3)
    elif a == "**":
        return round(b ** c, 3)

def calc():
    while 1:
        operator = get_operator()
        if operator == "exit":
            print("You just exited the programme.")
            break
        
        num1 = get_num1()
        num2 = get_num2()

        result = operation(operator, num1, num2)
        print(f"Result is = {result}")

calc()
