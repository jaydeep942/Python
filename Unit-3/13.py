# Write a program to show method overloading to find sum of two
# or three numbers

class MathOperations:
    # Method to find sum (handles 2 or 3 numbers)
    def sum(self, a = None, b= None , c=None):

        if(a != None and b!= None and c!=None):
            return a + b + c
        elif(a != None and b!= None):
            return a + b    
        elif(a != None):
            return a
        else:
            return print("No values provided")


# Main Program
m = MathOperations()

# Calling with 1 arguments
print("Sum of 1 numbers:", m.sum(10))

# Calling with 2 arguments
print("Sum of 2 numbers:", m.sum(10, 20))

# Calling with 3 arguments
print("Sum of 3 numbers:", m.sum(10, 20, 30))

# no passing any value 
print(f"not passing any value: { m.sum()}")