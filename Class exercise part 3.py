# Class Exercise (Part 3)
# Add a "Customer" class, that contains a customer (with at least a customer_id and a customer_name).
# Add this to the Receipt class to link a receipt to a customer.

# Class Exercise (Part 3)
# Add a "Customer" class, that contains a customer (with at least a customer_id and a customer_name).
# Add this to the Receipt class to link a receipt to a customer.

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