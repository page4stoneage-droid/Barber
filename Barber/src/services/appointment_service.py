from models.appointment import Appointment

class AppointmentService:
    def __init__(self):
        self.appointments = []
        
    def add_appointment(self, new_appointment):
        for appointment in self.appointments:
            if (
                appointment.barber == new_appointment.barber 
                and appointment.date == new_appointment.date 
                and appointment.time == new_appointment.time
            ):
                print("Error: This barber is already booked at this time!")
                return
        self.appointments.append(new_appointment)
        print("Appointment added successfully!")
    
    def show_appointments(self):
        if not self.appointments:
            print("Take WhatEver you want!")
            return
        for i in self.appointments:
            i.show_info()
            
    def search_appointment(self, appointment_id):
        found = False
        for i in self.appointments:
            if i.id == appointment_id :
                found = True
                i.show_info()
        if not found:
            print("No matches!")   
            
    def cancel_appointment(self, appointment_id):    
        appointment_to_remove = None
        for i in self.appointments:
            if i.id == appointment_id:
                appointment_to_remove = i
                break
                
        if appointment_to_remove:
            self.appointments.remove(appointment_to_remove) 
            print("Appointment canceled successfully!")
        else:
            print("Not Found")