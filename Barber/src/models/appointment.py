class Appointment:
    def __init__(self, id, customer, barber, service, date, time, status=False):
        self.id = id 
        self.customer = customer
        self.barber = barber
        self.service = service
        self.date = date
        self.time = time
        self.status = status
        
    def show_info (self):
        print(f"Id: {self.id}")
        print(f"Customer: {self.customer}")
        print(f"Barber: {self.barber}")
        print(f"Service: {self.service}")
        print(f"Date: {self.date}")
        print(f"Time: {self.time}")
        print(f"Status: {self.status}")
        
    def cancel (self):
        if self.status :
            self.status = False
            print("Cancel")
        else :
            print("Appointment already cancelled")
            
    def reschedule (self,new_date, new_time):
        self.date =new_date
        self.time =new_time
        print("Changed")
        
    