'''
1. *User interface*:
    - Create a user-friendly command-line interface (CLI) for the contact Management System.
    - Display a welcoming message and provide a menu with the following options

    Welcome to the Contact Management System! 
Menu:
1. Add a new contact
2. Edit an existing contact
3. Delete a contact
4. Search for a contact
5. Display all contacts
6. Export contacts to a text file
7. Import contacts from a text file *BONUS*
8. Quit
2. *Contact Data Storage*:

    - Use nested dictionaries as the main data structure for storing contact information.
    - Each contact should have a unique identifier (a phone number or email address) as the outer directionary key
    - Store contact details within the inner dictionary, including:
        - name
        - phone number
        - Email address
        - Additional information (address, notes).
3. *Menu Actions*:

Implement the following actions in response to menu selections:
    - Adding a new contact
    - Editing an exisiting contact's information (name, phone number, email)
    - Deleting a contact
    - Searcing for a contact and dispalying their details.
    - Displaying a list of all contacts.
    - Exporting contacts to a text file in a structured format
    - Importing contacts from a text file and adding them to the system *Bonus
4. *User Interaction*:

- Utilize input() to enable users to select menu options and provide contact details.
- Implement input validation using regex to ensure correct formatting of contact information.
5 *Error Handling*

Apply error handling using try, except, else, and finally blocks to manage unexpected issue that may araise during execution.
*GitHub Repository*

- Create a GitHub repository for your project.
- Create a clean and interactive README.md file in your GitHub repository.
- Include clear instructions on how to run the application and explanations of its features.

'''

contact_information = [
    {"name": "Carlos Martinez", "email": "carlos.martinez@example.com", "phone": "3051234567"},
    {"name": "Lucia Gomez", "email": "lucia.gomez@example.com", "phone": "7869876543"},
    {"name": "Miguel Rodriguez", "email": "miguel.rodriguez@example.com", "phone": "8187654321"},
    {"name": "Sofia Hernandez", "email": "sofia.hernandez@example.com", "phone": "2133456789"},
    {"name": "John Smith", "email": "john.smith@example.com", "phone": "2025550176"},
    {"name": "Emily Johnson", "email": "emily.johnson@example.com", "phone": "2125550123"},
    {"name": "Michael Brown", "email": "michael.brown@example.com", "phone": "7185550144"},
    {"name": "Ashley Davis", "email": "ashley.davis@example.com", "phone": "3235550198"}
]
import re 

def validate_email(email):
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_regex, email)

def validate_phone(phone):
    phone_regex = r"^\d{10}$"
    return re.match(phone_regex, phone)

def add_contact(contact_information):
    try:
        name = input("Enter the contact name: ")
        email = input("Enter the contact email: ")
        phone_num = input("Enter the contact phone number: ")

        if not validate_email(email):
            raise ValueError("Invalid email entered! Please double check your charecters.")
        
        if not validate_phone(phone_num):
            raise ValueError("Invalid number, make sure it is a 10 digit number.")

        contact_information.append({"name": name, "email": email, "phone": phone_num})

    except ValueError as e:
        print(f"Error: {e}")
        
    else:
        print("Contact added succesfully!")

    finally:
        print("process of adding was complete.")

def edit_contact(contact_information):
    contact_name = input("Enter the name of the contact you want to edit: ")
    found = False

    for contact in contact_information:
        if contact['name'].lower() == contact_name.lower():
            found = True
            print(f"Editing the contact {contact['name']}")

            new_name = input("Enter the new name you wish to use: ")
            if new_name:
                contact['name'] = new_name

            new_email = input("Enter the new email: ")
            if new_email:
                if validate_email(new_email):
                    contact['email'] = new_email
                else:
                    print("Invalid email, no change was made.")    

            new_phone = input("Enter the new phone number: ")
            if new_phone:
                if validate_phone(new_phone):
                    contact['phone'] = new_phone
                else:
                    print("number has to be 10 digits, no change on phone number has been made.")
            
            print(f"Contact '{contact['name']} has been updated.")
            break
    if not found:
        print(f"Contact '{contact_name}' was not found.")


def delete_contact(contact_information):
    contact_removal = input("Enter the name of the contact you wish to remove: ")
    found = False

    for contact in contact_information:
        if contact['name'].lower() == contact_removal.lower():
            contact_information.remove(contact)
            print(f"The contact '{contact_removal}' has been removed. ")
            found = True
            break
    if not found:
        print(f"The contact '{contact_removal}' is not in your contacts.")


def search_for_contact(contact_information):
    find_contact = input("Enter the name of the person you want to find: ")
    found = False

    for contact in contact_information:
        if contact['name'].lower() == find_contact.lower():
            print(f"Name: {contact['name']}, Email: {contact['email']}, Phone: {contact['phone']}")
            found = True
            break
    if not found:
        print(f"the contact '{find_contact}' was not found in your contacts.")


def display_all_contacts():
    if contact_information:
        for contact in contact_information:
            print(f"Name: {contact['name']}, Email: {contact['email']}, Phone: {contact['phone']} ")
    else:
        print("No contacts found")

def export_contacts(contact_information):
    try:
        with open('additional_contacts.txt', 'w') as file:
            for contact in contact_information:
                file.write(f"{contact['name']},{contact['email']},{contact['phone']}\n")
        print("Contacts exported successfully to 'additional_contacts.txt'.")
    
    except Exception as e:
        print(f"An error occurred while exporting contacts: {e}")


def import_contacts(contact_information):
    try:
        with open('additional_contacts.txt', 'r') as file:
            for line in file:  
                parts = line.strip().split(',')
                if len(parts) == 3:
                    name = parts[0]
                    email = parts[1]
                    phone = parts[2]
                    contact_information.append({'name': name, 'email': email, 'phone': phone})
            print("Contacts imported successfully from 'additional_contacts.txt'.")
        
    except FileNotFoundError:
        print("The file 'additional_contacts.txt' was not found.")
    except Exception as e:
        print(f"An error occurred while importing contacts: {e}")



def menu():
    while True:
        
        print("\nWelcome to the Contact Management App\nMenu")
        print("\n1: Add new contact\n2: Edit a contact\n3: Delete contact\n4: Search for a contact\n5: Display all contacts\n6: Export contacts to a text file\n7: Import contacts from text file\n8: Exit")
        choice = input("Please select an option: ")

        if choice == '1':
            add_contact(contact_information)
        
        elif choice == '2':
            edit_contact(contact_information)

        elif choice == '3':
            delete_contact(contact_information)

        elif choice == '4':
            search_for_contact(contact_information)
        
        elif choice == '5':
            display_all_contacts()

        elif choice == '6':
            export_contacts(contact_information)
        
        elif choice == '7':
            import_contacts(contact_information)

        elif choice == '8':
            print("Exiting the program.")
            break

        else:
            print("Please enter a valid choice.")
        
if __name__=='__main__':
    menu()