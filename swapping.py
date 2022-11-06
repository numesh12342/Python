#Swapping of two numbers
#Approach one
while(True):
    #Taking input from the user
    P=float(input("Enter the first number::"))
    Q=float(input("Enter the second number::"))

    #To swap the values using comma operator

    P,Q = Q,P

    print("The value of P after swapping = ",P)
    print("The value of Q after swapping = ",Q)
    # To come out of the while loop    
    back = str(input("Enter 'quit' to exit or press any key to continue::"))
    if back == "quit":
        break
    
 #Approach number two 
while(True):
    R=float(input("Enter the first number::"))
    S=float(input("Enter the second number::"))   
    
    # To swap the value of two variables  
    # We will use third variable which is a temporary variable 
    temp1 = R
    R = S
    S = temp1
    
    print("The value of P after swapping = ",R)
    print("The value of Q after swapping = ",S)
    
    back = str(input("Enter 'quit' to exit or press any key to continue::"))
    if back == "quit":
        break
    
#Approach number three 
   
T = int( input("Please enter value for P: "))  
U = int( input("Please enter value for Q: "))  
   
# To Swap the values of two variables using Addition and subtraction operator  
T = T + U    
U = T - U   
T = T - U  
   
print ("The Value of P after swapping: ", T)  
print ("The Value of Q after swapping: ", U)    