💈 Barber Shop Management System (CLI)
A robust, Object-Oriented Command-Line Interface (CLI) application for managing a barber shop. This project is built using a Layered Architecture, separating data models from business logic (services) to ensure maintainability and scalability.

✨ Features
Secure Authentication: User registration and login system with hidden password input (getpass) and minimum length validation.
Session Management: Users must be logged in to book an appointment.
Appointment Booking: Prevents double-booking (no two customers can book the same barber at the same date and time).
Layered Architecture: Clear separation between Models (entities) and Services (business logic).
CRUD Operations: Add, show, search, and delete customers, barbers, services, and appointments.
Clean UI: Clear screen functionality for a neat CLI experience.
🏗️ Architecture & Project Structure
The project follows an MVC-like pattern without the View (CLI acts as the view):

📁 Barber├── 📁 models/          # Data entities (Classes)│   ├── customer.py     # Customer class (id, name, phone)│   ├── barber.py       # Barber class (id, name, speciality)│   ├── service.py      # Service class (name, price, duration)│   └── appointment.py  # Appointment class (id, customer, barber, service, date, time, status)│├── 📁 services/        # Business logic (Managers)│   ├── customer_service.py│   ├── barber_service.py│   ├── service_manager.py│   └── appointment_service.py  # Includes double-booking validation│└── main.py             # Main application entry point (Menu, Auth, and UI)
🛠️ Tech Stack
Language: Python 3.x
Modules Used: os, getpass (Standard Python Libraries - No external installation required!)
🚀 How to Run
Make sure you have Python 3+ installed on your system.
Clone this repository:
bash

git clone https://github.com/page4stoneage-droid/Barber.git
Navigate to the project folder:
bash

cd Barber
Run the main application:
bash

python main.py
📋 Usage Guide
1.Register (Option 1): Create a new account. Password must be at least 8 characters.
2.Login (Option 2): Authenticate using your credentials.
3.Book Appointment (Option 3): View available barbers, select one, and choose your desired date and time. The system will automatically reject 4.4.double-bookings.
5.Show Appointments (Option 4): View a list of all currently booked appointments.
6.Exit (Option 5): Close the application safely.