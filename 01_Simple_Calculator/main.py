from calculator import Calculator
from color import colors,fg,bg

calculator = Calculator()   # Create an instance of the Calculator class
header = calculator.header()

while True:

    # Display menu
    calculator.menu()

    choice = calculator.menuChoice()

    # Exit
    if choice == 6:
        calculator.exit()
        break

    # Choice
    if choice != 5:
        try:
            num1 = int(input(fg.green+"\nEnter the number 1: "+colors.reset))
            num2 = int(input(fg.green+"Enter the number 2: "+colors.reset))
        except ValueError:
            print(fg.red+"\n\t❌ Value error! please enter valid number"+colors.reset)
            continue
    else:
        # Previous result
        print(fg.green+f"\nprevious result: {calculator.result}"+colors.reset)
        num1 = calculator.result
        try:
            num2 = int(input(fg.green+"Enter the number 2: "+colors.reset))
            choice = calculator.menuChoice()
            if choice == 6:
                calculator.exit()
                break
        except ValueError:
            print(fg.red+"\n\t❌ Value error! please enter valid number"+colors.reset)
            continue


    # Choice cases
    if choice == 1:
        result = calculator.add(num1, num2)
        message = f'Addition of {num1} and {num2} is:'
        calculator.boxoutput(message, result)
    elif choice == 2:
        result = calculator.sub(num1, num2)
        message = f'Subtraction of {num1} and {num2} is:'
        calculator.boxoutput(message,result)
    elif choice == 3:
        result = calculator.mul(num1, num2)
        message = f"Multiplication of {num1} and {num2} is"
        calculator.boxoutput(message,result)
    elif choice == 4:
        if num2 == 0:
            print("Error division by zero")
        else:
            result = calculator.div(num1, num2)
            message = f"Division of {num1} and {num2} is"
            calculator.boxoutput(message,result)
