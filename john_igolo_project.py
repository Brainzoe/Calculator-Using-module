# main script
import calculator

def main():
    print("Welcome to the calculator app!")
    print("Available operations: +, -, *, /")

    operation = input("Enter operation (+, -, *, /): ")
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        if operation == "+":
            result = calculator.add(num1, num2)
        elif operation == "-":
            result = calculator.subtract(num1, num2)
        elif operation == "*":
            result = calculator.multiply(num1, num2)
        elif operation == "/":
            result = calculator.divide(num1, num2)
        else:
            print("Invalid operation")
            return
        
        print("Result:", result)
    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
