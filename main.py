class Employee:
    def __init__(self):
        self.set_name()
        self.set_number()
    def set_name(self):
        self.name = str(input("Enter the name:"))
    def set_number(self):
        self.number = int(input("Enter the number:"))
    def get_name(self):
        print(self.name)
    def get_number(self):
        print(self.number)

class ProductionWorker(Employee):
    def __init__(self):
        super().__init__()
        self.set_shift()
        self.set_rate()
    def set_name(self):
        super().set_name()
    def set_number(self):
        super().set_number()
    def set_shift(self):
        self.shift = int(input("Enter shift 1 or 2:"))
    def set_rate(self):
        self.rate = float(input("Enter rate:"))
    def get_name(self):
        super().get_name()
    def get_number(self):
        super().get_number()
    def get_shift(self):
        print(self.shift)
    def get_rate(self):
        print(self.rate)

product = ProductionWorker()
product.get_name()
product.get_number()
product.get_shift()
product.get_rate()