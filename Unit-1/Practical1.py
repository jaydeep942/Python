# Write a program to swap two numbers without taking a temporary variable

def SwapNumber(a,b):
    a= a +b 
    b= a-b
    a= a-b
    print("After swapping: a =", a, "b =", b)


SwapNumber(45,78)