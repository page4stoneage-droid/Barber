from src.services.contact_book import ContactBook

if __name__ == '__main__' : 
    contactbook = ContactBook()
    

    while True:
        print("-----menu-----")
        print('1.Add Contact , 2.Show Contacts')
        print('3.Search by name , 4.Search by phone')
        print('5.Search by email , 6.Edit Contact')
        print("7.Delete Contacts , 8.Add Favorite")
        print("9.Show Favorites , 10.Add Tag")
        print("11.Remove Tag , 12.Show Tag")
        print("13.Show History , 14.Exit")
        choice = input("1-14")

        if choice == '1':
            name = input ("Enter name : ")
            phone = (input ('Enter phone number :'))
            email = input("Enter your email : ")
            contactbook.add_contact(name,phone,email)
        
        elif choice == '2' :
            contactbook.show_contacts()
        
        elif choice == '3':
            name = input("Write name : ")
            contactbook.search_by_name(name)

        elif choice == '4':
            phone = (input ("Write phone number : "))
            contactbook.search_by_phone(phone)
        
        elif choice == '5' :
            email = input ("Write email : ")
            contactbook.search_by_email(email)
        
        elif choice == '6' :
            name = input("\nEnter name of the contact to edit: ")
            phone = input("Enter new/updated phone number or press Enter to keep unchanged: ")
            email = input("Enter new/updated email or press Enter to keep unchanged: ")
            contactbook.edit(name, phone , email )
    
        elif choice == '7':
            name = input("Write name : ")
            contactbook.delete_contact(name)            
    
        elif choice == '8' :
            name = input("Write Name : ")    
            contactbook.add_favorite(name)

        elif choice == '9':
            contactbook.show_favorite()

        elif choice == '10' :
            name = input("Write name : ")
            tag = input("Write Tag : ")
            contactbook.add_tag(name,tag)
        
        elif choice == '11':
            name = input("Wirte name : ")
            tag = input('Write tag : ')
            contactbook.remove_tag(name,tag)
        
        elif choice == '12':
            name = input("Write name : ")
            contactbook.show_tags(name)
        
        elif choice == '13' :
            name = input("Write name : ")
            contactbook.show_history(name)
        
        elif choice == '14':
            break
    
        else : 
            print("Not Found")

