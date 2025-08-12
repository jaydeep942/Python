# Take expression from the user
expression = input("Enter an expression: ")

# Evaluate the expression
try:
    result = eval(expression)
    print("Result:", result)
except Exception as e:
    print("Invalid expression! Error:", e)