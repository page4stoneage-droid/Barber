import os 
import getpass

class BarberShop:
    def __init__(self):
        self.users = {}          
        self.appointments = {}
        self.current_user = None
    
    def clear_screen (self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def register (self):
        self.clear_screen()
        print("--- Register Panel ---")
        username = input("Username : ")
        
        if username in self.user :
            print("\n[Error] This username is already taken!")
        else :
            password =getpass.getpass("Password : ")
            if len(password) < 8 :
                print("\n[Error] Password must be at least 8 characters.")
            else :
                self.users[username]=password
                print("\n[Success] Registration complete! Please login.")
            
        input("\nPress to continue!")
    
    def login (self):
        self.clear_screen()
        print('---Login Panel---')
        username = input("Username : ")
        password = input("Password : ")
        
        if username in self.users and self.users[username]==password:
            self.current_user = username
            print('Successful')
        else :
            print("\n[Error] Invalid username or password.")

        input("\nPress Enter to continue...")    
        
    def book_time(self):
        self.clear_screen()
        print("--- Book Appointment ---")
        if not self.current_user:
            print("[Error] You must login first to book an appointment!")
            input("\nPress Enter to continue...")
            return 
        else : 
            time =input('Enter your desired time : ')
            if time in self.appointments.values:
                print(f"\n[Error] Sorry, {time} is already booked.")
            else :
                self.appointments[self.current_user]=time
                print(f"\n[Success] {time} booked successfully")
            
        input("\nPress Enter to continue...")
        
    def run (self) :
        while True:
            self.clear_screen()
            print("="*30)
            print("   BARBER SHOP MANAGEMENT v1.0   ")
            print("="*30)
            
            if self.current_user :
                print(f'Login as {self.current_user}')

            print("1. Register")
            print("2. Login")
            print("3. Book Appointment")
            print("4. Exit")
            print("-" * 30)
            
            choice = input("Select an option (1-4): ")
            
            if choice == '1':
                self.register()
            elif choice == '2':
                self.login()
            elif choice == '3':
                self.book_time()
            elif choice == '4':
                break

if __name__ == '__main__':
    app = BarberShop()
    app.run
    
                