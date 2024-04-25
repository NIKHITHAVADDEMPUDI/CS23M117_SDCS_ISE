class Calculator:
    
    def __init__(self):
        pass
    
    def multiply(self, x, y):
        #MULTIPLY TWO NUMBERS AND RETURN PRODUCT
        return x * y
    
    def divide(self, x, y):
        if y == 0:
            #DIVIDE TWO NUMBERS AND RETURN THE QUOTIENT
            raise ValueError("Division by zero!")
        return x / y
