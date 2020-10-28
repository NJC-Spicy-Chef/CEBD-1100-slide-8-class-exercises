# Class Exercise (Part 2)
# Create a Order class
# It holds many items
# It holds the date of purchase (datetime.datetime.now())
# It can add an item. It can remove an item. It can get the total price of all the items in the sale
# It can PRINT an order summary.

import datetime


class Receipt:
    items = []

    def __init__(self, item):
        self.item = item

    def add_item(self, item):
        self.item = item
        self.items.append(item)


class Item:
    def __init__(self, sku, name, price, taxable):
        self.sku = sku
        self.name = name
        self.price = price
        self.taxable = taxable

        item = [sku, name, price, taxable]

        o = Order(item)
        o.add_item(item)
        o.total_price(item)
        o.order_summary()


class Order(Receipt):
    def __init__(self, item):
        super().__init__(item)
        self.item = item
        self.purchase_datetime = datetime.datetime.now()
        self.total = 0.0

    def add_item(self, item):
        super().add_item(item)

    def remove_item(self, item):
        self.item = item
        self.items.remove(item)

    def total_price(self, item):
        self.item = item
        for x in self.items:
            self.total += float(x[2])

    def order_summary(self):
        print('Order summary\n')
        print('Customer Name: ')
        print('Date: ' + str(self.purchase_datetime) + '\n')
        print('Item: ' + str(self.item[1]) + ' (Taxable: ' + str(self.item[3])[0] + ')')
        print('Subtotal: ' + str(self.item[2]) + '\n')
        print('Tax: \n')
        print('Grand Total: ' + str(self.total))


i = Item('1', 'bread', '3.50', True)
j = Item('2', 'soda', '1.50', False)
