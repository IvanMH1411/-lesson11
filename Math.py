class Math:
    @staticmethod
    def addition(num1, num2):
        if str.isdigit(str(num1)) and str.isdigit(str(num2)):
            print(f" Your result: {(float(num1) + float(num2)):.2f}")
        else:
            print("There is at least 1 non-number")

    @staticmethod
    def subtraction(num1, num2):
        if str.isdigit(str(num1)) and str.isdigit(str(num2)):
            print(f" Your result: {(float(num1) - float(num2)):.2f}")
        else:
            print("There is at least 1 non-number")

    @staticmethod
    def multiplication(num1, num2):
        if str.isdigit(str(num1)) and str.isdigit(str(num2)):
            print(f" Your result: {(float(num1) * float(num2)):.2f}")
        else:
            print("There is at least 1 non-number")

    @staticmethod
    def division(num1, num2):
        if str.isdigit(str(num1)) and str.isdigit(str(num2)):
            if not float(str(num2)) == 0:
                print(f" Your result: {(float(num1) / float(num2)):.2f}")
            else:
                print("Division by 0")
        else:
            print("There is at least 1 non-number")