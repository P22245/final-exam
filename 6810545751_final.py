class Person:
    def __init__(self,name):
        self.name = name
    
    def introduce(self):
        print(f"Hi, I'm {self.name}.")
        return
    
class Customer(Person):
    def __init__(self,name,address):
        self.name = name
        self.address = address
    
    def place_order(self,item):
        self.item = item
        return
    
class Driver(Person):
    def __init__(self,name,vehicle):
        self.name = name
        self.vehicle = vehicle

    def deliver(self,order,customer):
        self.customer = customer
        self.order = order
        print(f"{self.name} is delivering {self.order} to {self.customer} using {self.vehicle}.")
        return
    
class DeliveryOrder:
    def __init__(self,customer,item,status):
        self.customer = customer
        self.item = item
        self.status = status

    def assign_driver(self,driver):
        self.driver = driver
        print("Order Summary: ")
        print(f"Item: {self.item}")
        print(f"Customer: {self.customer}")
        print(f"Status: {self.status}")
        print(f"Driver: {self.driver}")
        return

    def summary(self):
        print(f"Order for {self.item} → delivered")
        return

# main code
user1 = Customer(name="Alice", address="none")
user1.introduce()
user2 = Customer(name="Bob", address="none")
user2.introduce()
user3 = Driver(name="David", vehicle="motorcycle")
user3.introduce()
print()
order1 = DeliveryOrder(customer=user1.name, item="Laptop",status="preparing")
order1.assign_driver(driver=user3.name)
print()
order2 = DeliveryOrder(customer=user2.name, item="Headphones",status="preparing")
order2.assign_driver(driver=user3.name)
print()
user3.deliver(order=order1.item,customer=user1.name)
user3.deliver(order=order2.item,customer=user2.name)
print()
print("Final Status: ")
order1.summary()
order2.summary()