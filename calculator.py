#basic calculator

class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def add(self):
        return num1+num2

    def subtract(self):
        return num1-num2

    def multiply(self):
        return num1*num2

    def division(self):
        if num2!=0:
            return num1/num2
        else:
            return "division by 0 not allowed"

print("\n\n CALCULATOR \n\n")

num1=float(input("enter first numrber"))
num2=float(input("enter second numrber"))
calc=Calculator(num1,num2)

print(f"{num1}+{num2}={calc.add()}")
print(f"{num1}-{num2}={calc.subtract()}")
print(f"{num1}*{num2}={calc.multiply()}")
print(f"{num1}/{num2}={calc.division()}")