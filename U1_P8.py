while True:
    print("1.Area of Circle ")
    print("2.Area of Triangle ")
    print("3.Area of Square ")
    print("4.Simple Intrest ")
    print("5.Exit ")

    o = int(input("Select Operation :"))

    match o:
        case 1:
            pia = 3.14
            r = float(input("Enter a radius of circle"))
            area = pia * r * r
            print("Area of circle is :",area)
        case 2:
            base = float(input("Enter a base of Triangle :"))
            height = float(input("Enter a height of Triangle :"))
            area = (1/2) * base * height
            print("Area of Triangle is :",area)
        case 3:
            a = float(input("Enter a value of one side :"))
            area = a * a
            print("Area of square is :",area)
        case 4:
            p = int(input("Enter a amount :"))
            t = int(input("Enter a time in months :"))
            i = float(input("Enter a Intrest in percentage :"))
            intrest = (p * t * i)/100
            print("Simple Intrest is :",intrest)
        case 5:
                print("Exiting the program. Goodbye!")
                break
        case _:
            print("Choose a valid option :")
            continue
