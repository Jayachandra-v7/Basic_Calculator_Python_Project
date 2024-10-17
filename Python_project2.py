
def get_number(number):
    while True:

        operand = input("Number" + str(number) + ":")
        try:
            return operand
        except: 
            print("Invalid Number, try again")


operand = get_number(1)
operand2 = get_number(2)

sign = input("sign: ")




result = 0 

if sign == "+":
    result = float(operand) + float(operand2)
elif sign == "-":
    result = float(operand) - float(operand2)
elif sign == "/":
    if operand2 != 0:
        result = float(operand) / float(operand2)
    else: 
        print("Division by zero")
    result = float(operand) / float(operand2)
elif sign == "*":
    result = operand * operand2
else:
    print("Invalid Sign, try again")
print(result)
