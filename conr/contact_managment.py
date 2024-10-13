contacts = []

while True:
    print("""
          ***Contact Managment***
          1- Add a contact
          2- View contact
          3- Edit a contact
          4- Exit""")
    number_of_contact = input("Please choose a number from 1-4: ")

    if number_of_contact == '1':
        ID = input("Enter the contact ID: ")
        name = input("Please type a name: ")
        
        phone_number = input("Please type a phone number: ")
        while not phone_number.isdigit():
            print("Invalid phone number. Please enter only digits.")
            phone_number = input("Please type a phone number: ")
        
        contact = {"ID": ID, "name": name, "phone number": phone_number}
        contacts.append(contact)
        print(f"{name} was added successfully")
    elif number_of_contact == '2':
        # contact[ID]={"contacts":contacts}
        # print(contacts)
        for contact in contacts:
            print(contact)
    elif number_of_contact == '3':
        editor_ID = input("Please enter the ID of the contact to edit: ")
        for contact in contacts:
            if contact["ID"] == editor_ID:
                contact["name"] = input("Enter a new name: ")
                
                new_phone_number = input("Enter a new phone number: ")
                while not new_phone_number.isdigit():
                    print("Invalid phone number. Please enter only digits.")
                    new_phone_number = input("Enter a new phone number: ")
                
                contact["phone number"] = new_phone_number
                print("Contact updated successfully")
                break
        else:
            print("Contact ID not found")
    elif number_of_contact == '4':
        print("Exiting program...")
        break
    else:
        print("Invalid choice, please choose a number from 1-4.")

        
    #while True:
    # print("""
    #       1- Add a contact
    #       2- View contact
    #       3- Edit a contact
    #       4- Exit""")
    # editor = [
    # input("Please enter an ID to edit: "),
    # input("Enter a new name: "),
    # input("Enter a new number: ")
    # ]
    # number_of_contact= input("please choose a number from 1-4 ")
    # ID= input("Enter the contact ID: ")
    # name= input("please type a name: ")
    # phone_number= input("please type a phone number: ")
    # contact={}
    # contact["ID"]= ID
    # contact["name"]= name
    # contact["phone Number"]= phone_number

    

    # if number_of_contact == '1':
    #     print(f"{name} was added sucessfully")
    # elif number_of_contact == '2':
    #     print(f"{contact} contact managment")
    # elif number_of_contact == '3':
    #     print(editor)
    # else:
    #     print("Exiting programm...")
