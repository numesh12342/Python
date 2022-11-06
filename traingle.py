#Find the area of triangle 
#Area of a triangle = (s*(s-a)*(s-b)*(s-c))**1/2 #**=power
while(True):
    #Taking input from user for the three sides of the triangle
    a = float(input("Enter first side:"))
    b = float(input("Enter second side:"))
    c = float(input("Enter third side:"))

    #calculate the semi-perimeter
    #Mathematicl formula , s=(a+b+c)/2

    s = (a+b+c)/2
    print("The semiperimeter of the triangle is:",s)

    #Calculate the area of the traingle

    Area = (s*(s-a)*(s-b)*(s-c))**0.5
    print("The area of the traingle is::",Area)
    
    back = str(input("Enter 'quit' to exit from the loop or hit 'enter' to continue::"))
    if back == "quit":
        break