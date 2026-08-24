
class Customer:
    def __init__(self, id, name, phone):
        self.name = name
        self.phone = phone
        self.id = id
        
    def show_info(self):
        print(f"Customer Name: {self.name}")
        print(f"Customer Id: {self.id}")
        print(f"Customer Phone {self.phone}")    
    
    def update_phone(self,new_phone):
        self.phone = new_phone