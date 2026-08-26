from src.modules.contact import Contact


class ContactBook:
    def __init__(self):        
        self.favorites = []
        self.contacts = {}

        self.tags={}
        
        

    def add_contact(self, name, phone, email):
        if name in self.contacts :
            print("Already Exist !!")
            return
        else :
            contact = Contact(name, phone, email)
            self.contacts[name] = contact
            print("Added successfuly")
    
    def show_contacts (self):
        if not self.contacts :
            print("No contacts found") 
            return
        else :
            for contact in self.contacts.values():
                contact.show_info()
                print(25*'-')
                
    def search_by_name(self,  name):
        if name not in self.contacts :
            print ("Contact Not Found")
            return
        self.contacts[name].show_info()
        
    def search_by_email(self, email):
        for contact in self.contacts.values():
            if contact.email == email:
                contact.show_info()
                return
        print('Contact not found')
        
    def search_by_phone(self, phone):
        for contact in self.contacts.values():
            if contact.phone == phone:
                contact.show_info()
                return
        print ("Contact not found")   
        
        
    def edit(self, name, phone=None , email=None):
        if name not in self.contacts:
            print("Contact Not Found!!")
            return
        contact = self.contacts[name]
        if phone :
            old_phone = contact.phone
            contact.phone = phone
            contact.history.append(f'Phone Changed From {old_phone} to {phone}')
        if email :
            old_email = contact.email
            contact.email = email
            contact.history.append(f'Email Changed From {old_email} to {email}')
        print("Edit Successfuly!")
    
    def delete_contact(self, name) :
        if name in self.contacts:
            contact = self.contacts[name]
            del self.contacts[name]
            print("Delete Successfuly!!")
        else :
            print("Contact Not Found!")
        
    def add_favorite(self, name):
        if name not in self.contacts :
            print("Not found")
            return
        if name in self.favorites :
                print("Already Added")
                return
        contact = self.contacts[name]
        self.favorites.append(name)
        contact.favorite =True
        contact.history.append("Added to favorites")
        print(f"{name} Added to favorite list")

    def show_favorite(self):
        if self.favorites :
            for i in self.favorites:
                print(i)
        else :
            print("You Love No One")
    
    def show_history (self, name) :
        if name not in self.contacts:
            print("Empty")
            return
        
        contact = self.contacts[name]
        
        if not contact.history:        
            print("Empty")
            return
    
        for i in contact.history:
            print(i)
            
    def add_tag (self, name, tag):
            if name not in self.contacts:
                print("Contact not found!!")
                return
            
            contact = self.contacts[name]
            
            if tag not in self.tags: 
                self.tags[tag] = []
            
            if contact in self.tags[tag]:
                print("Already tagged")
                return
            
            self.tags[tag].append(contact)
            contact.history.append(f"Added tag {tag}")
            print("Tag Added") 
    
    def show_tags (self, name):
        if name not in self.contacts:
            print("Contact Not Found!")
            return
        
        contact = self.contacts[name]
        user_tags = []
        
        for tag, contacts in self.tags.items():
            if contact in self.contacts:
                user_tags.append(tag)
        
        if not user_tags:
            print("No tags found for this contact.")
            return
            
        print(f"Tags for {name}:")
        for t in user_tags:
            print(f"- {t}")
    
    def remove_tag(self, name, tag):
        if name not in self.contacts:
                print("Contact not found!!")
                return
            
        if tag not in self.tags:
            print('No Tag Found.')
            return
        contact = self.contacts[name]
        
        if contact not in self.tags[tag]:
            print("No Name Found.")
            return

        
        self.tags[tag].remove(contact)
        if len(self.tags[tag])== 0 :
            del self.tags[tag]
        contact.history.append(f"{name} Removed from {tag} tag!!")
        
        

            