print("\nI WANT TO SOLVE YOUR PROBLEMS\n\n")
print("AVAILABLE FUNCTIONS ARE LISTED DOWN BELOW\n")
print("1) Basic Operations (addition, subtraction, multiplication, division)\n2) Quadratic Equations\n3) Simple Derivative\n4) Simple Integral\n")
print("Example Imput: 2\n\n")
choice = input("Choice of Operation: ")
a=0
if choice == "1" :
    print("Example Operation Input: - ")
    print("addition: + ; subtraction: - ; multiplication: * ; division: / ")
    firstNumber = float (input ("First number: "))
    while a==0 : 
        operation = input("Choose operator: ")
        nextNumber = float (input ("Next number: "))
        if type(nextNumber)!=float :
            print("\n\nNon-Number Type Input Detected. Terminating Calculator.")
        if operation == "+" :
            firstNumber = firstNumber + nextNumber

        if operation == "-" :
            firstNumber = firstNumber - nextNumber

        if operation == "*" :
            firstNumber = firstNumber * nextNumber

        if operation == "/" :
            firstNumber = firstNumber / nextNumber

        print("Result: ",firstNumber)
if choice == "2" :
    print("Quadratic equations are written as: ax^2 + bx + c")
    print("Example Input: 3 ")
    a = float( input("Value of a: ") )
    b = float( input("Value of b: ") )
    c = float( input("Value of c: ") )
    delta = pow(b,2) - 4*a*c
    if delta < 0 :
        print("This equation has only imaginary solutions.")
    if delta == 0 :
        print("Discriminant is equal to zero.")
        x = (-b + pow(delta,1/2))/2*a
        print("x1 = x2 = ",x)
    if delta > 0 :
        print("Discriminant is greater than zero. ",delta)
        x1 = (-b + pow(delta,1/2))/(2*a)
        print("x1 = ",x1)
        x2 = (-b - pow(delta,1/2))/(2*a)
        print("x2 = ",x2)
        print("Roots of this equation: ", x1 ," , ", x2)
        print("Sum of roots: ",x1+x2)
        print("Product of roots: ",x1*x2)
if choice == "3" :
    print("By saying simple i really mean simple derivative that is written as: ax^b")
    print("Example Input: 3.1415 ")
    a = float( input("Value of a: ") )
    b = float( input("Value of b: ") )
    print("Derivative of ",a,"x^",b," is: ",a*b,"x^",b-1)
if choice == "4" :
    print("By saying simple i really mean simple integral that is written as: ax^b")
    print("Example Input: 2.7182 ")
    a = float( input("Value of a: ") )
    b = float( input("Value of b: ") )
    print("Integral of ",a,"x^",b," is: ",a/(b+1),"x^",b+1)