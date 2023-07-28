import os
print('\033[32mCALCULATOR')
#putting the inputs
def calculator():
    x = float(input('First number= '))
    operation = input('Operation = ')
    y = float(input('Second number= '))
    return x, y, operation

x, y, operation = calculator()

#making the inputs work
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y
def percentage(x,y):
    return (x*100)/y


#main function of the calculator
#addition
if operation == '+':
    print(add(x, y))
#subtraction
elif operation == '-':
    print(subtract(x, y))
#multiplication    
elif operation == '*' or operation == '×':
    print(multiply(x, y))
#division
elif operation == '/' or operation == '÷':
    print(divide(x, y))
    if y == 0:#Zero division error
        print('\033[31mCannot divide by 0')
elif operation == "%":
	  print(percentage(x,y))
else:
    print('\033[31msyntax error')#syntax error



os.system('cmd /c "pause"')#stops powershell/command prompt from closing

