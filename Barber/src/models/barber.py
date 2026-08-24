
class Barber:
    def __init__(self,id, name, speciality):
        self.name = name
        self.speciality = speciality
        
    def show_info(self):
        print(f"Barber Name: {self.name}")
        print(f"Barber Speciality: {self.speciality}")    
    
    def update_speciality(self,new_speciality):
        self.speciality = new_speciality
        