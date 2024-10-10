keepplaying = True 
while keepplaying ==True:
    number1 = int(input("Enter your first number"))
    number2 = int(input("Enter your second number"))
    operator = input("Enter your operation or quit to exit")


    match operator:
        case"+":
            result = number1 + number2
            print(f"{number1} + {number2} = {result}")
        case"-":
            result = number1 - number2
            print(f"{number1} - {number2} = {result}")
        case"/":
            if number1 ==0 or number2 ==0: 
                print("Error you cant divide by 0")
            else: 
                result = number1 / number2
                print(f"{number1} / {number2} = {result}")
        case"*":
            result = number1 * number2
            print(f"{number1} * {number2} = {result}") 
        case"quit":
            print("quitting application")
            break 
    
    

