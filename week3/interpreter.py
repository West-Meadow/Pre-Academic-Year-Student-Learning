# Promting the user to enter an expression
expression = input("Enter an Expression: ")
#
#splittng the expressing by space so that we can deal with three values
x, y, z = expression.split(" ")

# since the user inpu is in string format, we type cast tp float (we need to return float answers)
x = float(x)
z = float(z)

# checking the values arithmetic expression entered by the user
if y == "+":
 # Then we assign the appropriace sign, according to user input
    answ = x+z
# we create a new variable to store our float answer and return only one decimal place
    rounded_answ= round(answ,1)
    print(rounded_answ)

elif y == "-":
    answ = x-z
    rounded_answ= round(answ,1)
    print(rounded_answ)

elif y == "*":
    answ = x*z
    rounded_answ= round(answ,1)
    print(rounded_answ)
    

# checking the values arithmetic expression entered by the use
elif y == "/":
# since it is division need to check if the user is not deviding by zero
   
    answ = x/z
    rounded_answ= round(answ,1)
    print(rounded_answ)

else:
 print("Undefined")
