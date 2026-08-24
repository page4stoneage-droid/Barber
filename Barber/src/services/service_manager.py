from models.service import Service

class ServiceManager:
    def __init__(self):
        self.services = []
    
    def add_service(self, service):
        if service not in self.services:
            self.services.append(service)
        else:
            print("Service already exists")
    
    def show_services(self):
        if not self.services:
            print("No services found")
            return
        for service in self.services:
            service.show_info()
            
    def search_services(self, service):
        found = False
        for i in self.services:
            if i == service :
                service.show_info()
                found = True
        if not found :
            print("Not Found!")
    
    def delete_service (self, service):
        if service in self.services:
            self.services.remove(service)
            print("Deleted")
        else :
           print("Not Found")