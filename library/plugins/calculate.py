class Calculate:
    def __init__(self):
        self.val = 0

    def set_value(self, val):
        self.val = val
        return self
    
    def add(self, val):
        self.val += val
        return self.val
    
    def subtract(self, val):
        self.val -= val
        return self.val
    
    def multiply(self, val):
        self.val *= val
        return self.val
    
    def output(self, method):
        if method == 'stdout':
            print(self.val)