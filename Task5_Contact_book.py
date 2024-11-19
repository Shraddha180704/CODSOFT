import sys
contact_list = []

def display_menu():
    print()
    print("MENU")
    print("1.Add contact")
    print("2.View contact list")
    print("3.Search contact")
    print("4.Update contact")
    print("5.Delete contact")
    print("6.Exit")


    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            add_contact_info()
        elif choice == "2":
            view_contact()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            sys.exit()
        else:
            print("Invalid input")




def add_contact_info():
    global contact_list
    name = input("Please enter name to get added: ")

    while True:
        phone_no = input("Enter phone number: ")
        if phone_no.isdigit():
            if len(phone_no) == 10:
                break
            else:
                print("Enter 10 digit phone number")
        else:
            print("Enter 10 digit number")

    email = input("enter email id: ")
    address = input("Enter address: ")

    contact = {"name" : name,
               "phone number" : phone_no,
               "email" : email,
               "address" : address}

    contact_list.append(contact)
    print("Added successfully")
    display_menu()

def view_contact():
    global contact_list
    if len(contact_list) == 0:
        print("\nContact list is empty")
    else:
        for contact in contact_list:
            print()
            print("Name:", contact["name"])
            print("Phone number:", contact["phone number"])
            print("Email:", contact["email"])
            print("Address:", contact["address"])


    display_menu()

def search_contact():
    global contact_list
    name = input("Enter name to search: ")
    for contact in contact_list:
        if contact["name"] == name:
            print()
            print("Name:", contact["name"])
            print("Phone number:", contact["phone number"])
            print("Email:", contact["email"])
            print("Address:", contact["address"])
            break
    else:
        print("Contact not found")
    display_menu()

def update_contact():
    global contact_list
    name = input("Enter name to be updated: ")
    for contact in contact_list:
        if contact["name"] == name:
            name = input("Please enter name to update: ")

            while True:
                phone_no = input("Enter phone number: ")
                if phone_no.isdigit():
                    if len(phone_no) == 10:
                        break
                    else:
                        print("Enter 10 digit phone number")
                else:
                    print("Enter 10 digit number")
            email = input("enter email id: ")
            address = input("Enter address: ")

            contact["name"] = name
            contact["phone number"] = phone_no
            contact["email"] = email
            contact["address"] = address
            print("\nUpdated successfully")
            break
    else:
        print("\nNot found")

    display_menu()

def delete_contact():
    global contact_list
    name = input("Enter name to delete: ")
    for contact in contact_list:
        if contact["name"] == name:
            contact_list.remove(contact)
            print("\nDeleted successfully")
            break
    else:
        print("\nNo contact found")

    display_menu()

display_menu()






