class Calculator:
    @staticmethod
    def plus(a, b):
        return a+b
    
    @staticmethod
    def subtract(a, b):
        return a-b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @staticmethod
    def square(a):
        return a ** 2
    
    @staticmethod
    def factorial(a):
        if a < 2:
            return 1

        result = 1
        for num in range(1, a+1):
            result *= num

        return  result

def demo():
    return f'Demo method'