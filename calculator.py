from pip import main


class Calculator:

    def input(self):
        self.input1 = int(input("Input 1: "))
        self.input2 = int(input("Input 2: "))

    def adder(self):
        print("Addition: Please input 2 numbers")
        self.input()
        return self.input1+self.input2

    def subtractor(self):
        print("Subtraction: Please input 2 numbers")
        self.input()
        return self.input1-self.input2

    def multiplier(self):
        print("Multiplication: Please input 2 numbers")
        self.input()
        return self.input1*self.input2

    def divider(self):
        print("Division: Please input 2 numbers")
        self.input()
        return self.input1/self.input2

    def clear(self):
        print("Calculator Cleared")
        return 0

if __name__ == "__main__":
    cal = Calculator()

    print(cal.adder())
    print(cal.subtractor())
    print(cal.multiplier())
    print(cal.divider())
    print(cal.clear())