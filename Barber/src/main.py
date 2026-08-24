import os
import getpass
from models.customer import Customer
from models.barber import Barber
from models.appointment import Appointment
from services.customer_service import CustomerService
from services.barber_service import BarberService
from services.appointment_service import AppointmentService

class MainApp:
    def __init__(self):
        # سرویس‌ها
        self.customer_service = CustomerService()
        self.barber_service = BarberService()
        self.appointment_service = AppointmentService()
        
        
        self.users = {}          
        self.current_user = None 
        
        
        self.barber_service.add_barber(Barber(1, "Ali", "Haircut"))
        self.barber_service.add_barber(Barber(2, "Reza", "Beard Trim"))

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def run(self):
        while True:
            self.clear_screen()
            print("="*30)
            print("   BARBER SHOP MAIN MENU   ")
            print("="*30)
            
            
            if self.current_user:
                print(f"Welcome, {self.current_user}!")
            
            print("1. Register")
            print("2. Login")
            print("3. Book Appointment")
            print("4. Show Appointments")
            print("5. Exit")
            print("-" * 30)
            
            choice = input("Select an option (1-5): ")
            
            if choice == '1':
                self.register_menu()
            elif choice == '2':
                self.login_menu()
            elif choice == '3':
                self.book_appointment_menu()
            elif choice == '4':
                self.appointment_service.show_appointments()
                input("\nPress Enter to continue...")
            elif choice == '5':
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")
                input("Press Enter to continue...")

    def register_menu(self):
        self.clear_screen()
        print("--- Register Panel ---")
        username = input("Enter a new username: ")
        if username in self.users:
            print("\n[Error] Username already taken!")
        else:
            password = getpass.getpass("Enter password (min 8 chars): ")
            if len(password) < 8:
                print("\n[Error] Password must be at least 8 characters.")
            else:
                self.users[username] = password
                print("\n[Success] Registration complete! Please login.")
        input("\nPress Enter to continue...")

    def login_menu(self):
        self.clear_screen()
        print("--- Login Panel ---")
        username = input("Username: ")
        password = getpass.getpass("Password: ")
        
        if username in self.users and self.users[username] == password:
            self.current_user = username
            print(f"\n[Success] Welcome back, {username}!")
        else:
            print("\n[Error] Invalid username or password.")
        input("\nPress Enter to continue...")

  
    def book_appointment_menu(self):
        self.clear_screen()
        print("--- Book Appointment ---")
        
        
        if not self.current_user:
            print("[Error] You must login first to book an appointment!")
            input("\nPress Enter to continue...")
            return  

        print("Available Barbers:")
        self.barber_service.show_barbers()
        
        appt_id = input("\n ENter an ID for this appointment : ")
        b_name = input("\nEnter Barber Name: ")
        service_name = input("Enter service name : ")
        date = input("Enter Date (e.g., 2024-08-21): ")
        time = input("Enter Time (e.g., 15:00): ")
        
        new_appointment = Appointment(id =appt_id,customer=self.current_user, barber=b_name,service=service_name ,date=date, time=time)
        self.appointment_service.add_appointment(new_appointment)
        input("\nPress Enter to continue...")

if __name__ == '__main__':
    app = MainApp()
    app.run()