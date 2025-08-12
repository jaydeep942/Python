# Write a program that evaluates an expression given by the user at run time using eval() function. Example: Enter and expression: 10+8-9*2- (10*2) Result: -20


# Take expression from the user
expression = input("Enter an expression: ")

# Evaluate the expression
try:
    result = eval(expression)
    print("Result:", result)
except Exception as e:
    print("Invalid expression! Error:", e)