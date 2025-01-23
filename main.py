
class RetailItem:
    def __init__(self, description, units, price):
        self.description = description
        self.units = units
        self.price = price

item1 = RetailItem("Jacket",12,59.95)
item2 = RetailItem("Designer jeans", 40,34.95)
item3 = RetailItem("Shirt",20,24.95)


class CashRegister:
    def __init__(self):
        self.items = []
    def purchase_item(self,item):
        self.items.append(item)
    def get_total(self):
        return sum((item.price*item.units) for item in self.items)
    def show_items(self):
        for item in self.items:
            print(f"Description: {item.description}, Units: {item.units}, Price: {item.price}")
    def clear(self):
        self.items = []


register = CashRegister()
register.purchase_item(item1)
register.purchase_item(item2)
register.purchase_item(item3)
print(register.get_total())
register.show_items()
register.clear()
register.show_items()
