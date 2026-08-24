from models.customer import Customer

class CustomerService:
    def __init__(self):
        self.customers = []
        
    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)
        else:
            print("Already added")

    def show_customers(self):
        if not self.customers:
            print("List is Empty!!")
            return
        for i in self.customers:
            i.show_info()
    
    def search_customers(self, customer):
        found = False
        for i in self.customers:
            if i == customer:
                found = True
                customer.show_info()
                break
        if not found:
            print("Not Found")
    
    def delete_customers(self, customer):
            if customer in self.customers:
                self.customers.remove(customer)
                print("Deleted")
            else :
               print("Not Found") 