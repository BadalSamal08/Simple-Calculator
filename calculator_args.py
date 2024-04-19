import argparse
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        r = self.num1 + self.num2
        result = 'The sum of ' + str(self.num1) + ' and ' + str(self.num2) + ' is ' + str(r)
        print(result)
        return result

    def subtract(self):
        r = self.num1 - self.num2
        result = 'The subtraction of ' + str(self.num1) + ' and ' + str(self.num2) + ' is ' + str(r)
        print(result)
        return result

    def mul(self):
        r = self.num1 * self.num2
        result = 'The multiplication of ' + str(self.num1) + ' and ' + str(self.num2) + ' is ' + str(r)
        print(result)
        return result

    def divide(self):
        r = self.num1 / self.num2
        result = 'The division of ' + str(self.num1) + ' and ' + str(self.num2) + ' is ' + str(r)
        print(result)
        return result

if __name__ == '__main__':

    #initializing parser
    parser = argparse.ArgumentParser(description='calculator arguments')
    #adding arguments
    parser.add_argument('-num1', "--number1", required=True,type=float,help='Enter an integer for first number')
    parser.add_argument('-num2', "--number2", required=True, type=float, help='Enter an integer for second number')

    args = parser.parse_args()

    print(args.number1)
    print(args.number2)

    operation = Calculator(args.number1,  args.number2)
    operation.add()
    operation.mul()