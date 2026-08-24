
class Service:
    def __init__(self, name, price, duration):
        self.name = name
        self.price = price
        self.duration = duration
        
    def show_info(self):
        print(f"Service Name: {self.name}")
        print(f"Service Price: {self.price}")
        print(f"Service Duration {self.duration}")    
    
    def update_price(self,new_price):
        self.price = new_price