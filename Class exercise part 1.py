# Suppose we have a class called "Receipt" and we wanted receipts to have "Items" in the receipt.
# Items can be 1 or more. In other words, ONE receipt holds MANY items.
# To achieve this, we can store the items in a LIST.
# We can also use a method to add items to the list.

# Class Exercise (Part 1)
# This will use ALL the concepts we learned.
# Create an Item class. Item holds the sku, name, price of the item.
# Item holds a T/F value indicating if it's taxable or not.

class Receipt:
    items = []

    def __init__(self, item):
        self.item = item

    def add_item(self, item):
        self.item = item
        self.items.append(item)

        print(self.items)


class Item:
    def __init__(self, sku, name, price, taxable):
        self.sku = sku
        self.name = name
        self.price = price
        self.taxable = taxable

        item = [sku, name, price, taxable]

        r = Receipt(item)
        r.add_item(item)


i = Item('1', 'bread', '3.50', True)
j = Item('2', 'soda', '1.50', False)
