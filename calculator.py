print("Welcome to the Calculator!")
print("You can perform basic arithmetic operations: addition, subtraction, multiplication, division, modulo and exponentiation.")
print("Commands: 'add' for addition, 'sub' for subtraction, 'mul' for multiplication, 'div' for division, 'mod' for modulo, 'exp' for exponentiation, 'exit' to exit the program.")
print("------------------------------------------------------------------------------------------")

while True:
    command = input("Enter a command (add/sub/mul/div/mod/exp/exit): ").strip().lower()
    
    if command in ['add', 'sub', 'mul', 'div', 'mod', 'exp']:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            
            if command == 'add':
                result = num1 + num2
                print(f"The result of {num1} + {num2} is: {result}")
            elif command == 'sub':
                result = num1 - num2
                print(f"The result of {num1} - {num2} is: {result}")
            elif command == 'mul':
                result = num1 * num2
                print(f"The result of {num1} * {num2} is: {result}")
            elif command == 'div':
                if num2 != 0:
                    result = num1 / num2
                    print(f"The result of {num1} / {num2} is: {result}")
                else:
                    print("Error: Division by zero is not allowed.")
            elif command == 'mod':
                if num2 != 0:
                    result = num1 % num2
                    print(f"The result of {num1} % {num2} is: {result}")
                else:
                    print("Error: Modulo by zero is not allowed.")
            elif command == 'exp':
                result = num1 ** num2
                print(f"The result of {num1} ** {num2} is: {result}")
        except ValueError:
            print("Invalid input. Please enter numeric values.")
    
    elif command == 'exit':
        print("Exiting the Calculator. Goodbye!")
        break
    
    else:
        print("Invalid command. Please enter 'add', 'sub', 'mul', 'div', 'mod', 'exp' or 'exit'.")