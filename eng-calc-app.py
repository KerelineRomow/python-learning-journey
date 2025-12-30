import math

class Calculator:
    def __init__(self):
        self.history = []

    def add_to_history(self, operation, result):
        self.history.append(f"{operation} = {result}")

    def show_history(self):
        if not self.history:
            print("\n--- History is empty ---")
        else:
            print("\n--- Calculation History ---")
            for entry in self.history:
                print(entry)


class EngineeringCalculator(Calculator):

    def add(self, a, b):
        res = a + b
        self.add_to_history(f"{a} + {b}", res)
        return res

    def subtract(self, a, b):
        res = a - b
        self.add_to_history(f"{a} - {b}", res)
        return res

    def multiply(self, a, b):
        res = a * b
        self.add_to_history(f"{a} * {b}", res)
        return res

    def divide(self, a, b):
        try:
            res = a / b
            self.add_to_history(f"{a} / {b}", res)
            return res
        except ZeroDivisionError:
            return "Error: Division by zero!"

    def square_root(self, a):
        if a < 0:
            return "Error: Negative number!"
        res = math.sqrt(a)
        self.add_to_history(f"sqrt({a})", res)
        return res


def main():
    calc = EngineeringCalculator()

    print("--- Professional CLI Calculator (OOP) ---")

    while True:
        print("\nActions: +, -, *, /, sqrt, history, exit")
        choice = input("Select operation: ").lower().strip()

        if choice == 'exit':
            print("Closing the program. Goodbye!")
            break
        elif choice == 'history':
            calc.show_history()
            continue

        try:
            if choice == 'sqrt':
                num = float(input("Enter number: "))
                print(f"Result: {calc.square_root(num)}")
            elif choice in ['+', '-', '*', '/']:
                num1 = float(input("First number: "))
                num2 = float(input("Second number: "))

                if choice == '+':
                    print(f"Result: {calc.add(num1, num2)}")
                elif choice == '-':
                    print(f"Result: {calc.subtract(num1, num2)}")
                elif choice == '*':
                    print(f"Result: {calc.multiply(num1, num2)}")
                elif choice == '/':
                    print(f"Result: {calc.divide(num1, num2)}")
            else:
                print("Invalid input. Please choose from the list.")
        except ValueError:
            print("Error: Please enter valid numeric values!")


if __name__ == "__main__":
    main()
