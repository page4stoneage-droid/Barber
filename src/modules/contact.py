class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        self.favorite = False
        
        self.history = []
        self.history.append("Contact Created")


    def show_info(self):
        print(f"Name = {self.name}")
        print(f'Phone = {self.phone}')
        print(f'Email = {self.email}')

                

            

        