from models.barber import Barber


class BarberService :
    def __init__(self):
       self.barber_db = [] 
       
    def add_barber(self, barber):
        if barber not in self.barber_db:
            self.barber_db.append(barber)
        else:
            print("Already added")
    
    def show_barbers(self):
            if not self.barber_db:
                print("No Barber found")
                return
            for i in self.barber_db:
                i.show_info()
    
    def search_barber(self, barber):
        found = False
        for i in self.barber_db:
            if i == barber:
                found = True
                barber.show_info()
            if not found:
                print("No matches!")
                
    def delete_barber(self, barber):
        if barber in self.barber_db:
            self.barber_db.remove(barber)
            print("Deleted!!")
        else :
            print("Not Found!")
            
                