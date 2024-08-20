# Define the contacts dictionary to store contact information
contacts = {}

# Function to add a new contact
def add_contact():
    store_name = input("Enter store name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    
    contacts[store_name] = {
        "Phone": phone_number,
        "Email": email,
        "Address": address
    }
    print(f" \nContact '{store_name}' added successfully \n")

# Function to view all contacts
def view_contacts():
    if contacts:
        print("\nContact List:")
        for name, details in contacts.items(): 
            print(f"Name: {name}, Phone: {details['Phone']}")
    else:
        print("\n No contacts found \n")

# Function to search for a contact
def search_contact():
    search_name = input("Enter the name or phone number to search: ")
    found = False
    for name, details in contacts.items():
        if search_name.lower() in name.lower() or search_name in details["Phone"]:
            print(f"\nFound Contact:\nName: {name}\nPhone: {details['Phone']}\nEmail: {details['Email']}\nAddress: {details['Address']}\n")
            found = True
    if not found:
        print("\n Contact not found \n")

# Function to update a contact
def update_contact():
    store_name = input("Enter the name of the contact to update: ")
    if store_name in contacts:
        print("\nCurrent details:")
        print(f"Phone: {contacts[store_name]['Phone']}")
        print(f"Email: {contacts[store_name]['Email']}")
        print(f"Address: {contacts[store_name]['Address']}")
        
        phone_number = input("Enter new phone number (leave blank to keep current): ")
        email = input("Enter new email (leave blank to keep current): ")
        address = input("Enter new address (leave blank to keep current): ")
        
        if phone_number:
            contacts[store_name]['Phone'] = phone_number
        if email:
            contacts[store_name]['Email'] = email
        if address:
            contacts[store_name]['Address'] = address
            
        print(f"\nContact '{store_name}' updated successfully.\n")
    else:
        print("\n Contact not found \n")

# Function to delete a contact
def delete_contact():
    store_name = input("Enter the name of the contact to delete: ")
    if store_name in contacts:
        del contacts[store_name]
        print(f"\nContact '{store_name}' deleted successfully.\n")
    else:
        print("\n Contact not found \n")

# Main function
def main():
    while True:
        print("Contact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("\n Enter your choice: ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("\n Exiting Contact Management System")
            break
        else:
            print("\n Invalid choice. Please select a valid option \n")

# Run the main function
if __name__ == "__main__":
    main()
