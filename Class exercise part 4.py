
# Class Exercise Part 4 (Put it together)
# Ask questions in a loop as follows: Add an item to the order, blank line terminates
# Item name? Taxable?  (True/False)
# At the end, print out:
# Order summary:
# Customer Name and Date
# Listing of Items and a Sign saying taxable or not (write a T)
# The raw total
# The tax
# The grand total

import datetime


class Customer:
    def __init__(self, customer_id, customer_name):
        self.customer_id = customer_id
        self.customer_name = customer_name


class Receipt:
    items = []

    def __init__(self, item):
        self.item = item
        self.c = Customer('1', 'Nongyao')

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
        print('Order Summary\n')
        print('Customer Name: ' + str(self.c.customer_name))
        print('Date: ' + str(self.purchase_datetime) + '\n')
        print('Item ' + str(len(self.items)) + ': ' + str(self.item[1]) + ' (' + str(self.item[3])[0] + ')\t\t' + str(self.item[2]))
        print('\nSubtotal: ' + str(self.total))
        print('Tax: ')
        print('Grand Total: ' + str(self.total))


i = Item('1', 'bread', '3.50', True)
j = Item('2', 'soda', '1.50', False)