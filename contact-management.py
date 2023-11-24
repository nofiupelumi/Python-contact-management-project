import time

# initialize a contact db 
contacts = {}

while True:
    print("\n*Welcome To my Contact Management System App*\n")
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. Delete Contact")
    print("4. View Contacts")
    print("5. Search Contact by Phone Number")
    print("6. Search Contact by Name")
    print("7. Sort Contacts by Name") # added a new option for sorting contacts by name
    print("8. Sort Contacts by Phone Number") # added a new option for sorting contacts by phone number
    print("9. Quit\n")

    # get user choice
    user_choice = int(input("Enter a number to perform an operation: "))

    if user_choice == 9:
        print("Sad to see you leave. Thanks and Goodbye!!!")
        break
    elif user_choice == 1:
        name = input("Enter contact name: ").title().strip()
        phone_num = input("Enter phone number: ").replace(' ','')
        # check if the phone number is valid and has 11 digits
        if phone_num.isdigit() and len(phone_num) == 11:
            # pair the value with the key
            contacts[name] = phone_num
            print(f'{name} contact has been added successfully!!!')
        else:
            print("Invalid phone number. Please enter a valid 11-digit number.")
    elif user_choice == 2:
        name = input("Enter contact name to update: ").title().strip()
        # check if name exist before performing update 
        if name in contacts:
            new_phone_num = input("Enter new phone number: ").replace(' ','')
            # check if the new phone number is valid and has 11 digits
            if new_phone_num.isdigit() and len(new_phone_num) == 11:
                # update new phone number with the name
                contacts[name] = new_phone_num
                time.sleep(5)
                print(f'{name} contact has been updated successfully!!!')
            else:
                print("Invalid phone number. Please enter a valid 11-digit number.")
        else:
            print('Oops! That name doesn\'t exist!!!')
    elif user_choice == 3:
        # check if name exist before performing delete operation
        name = input("Enter contact name to delete: ").title().strip()
        if name in contacts:
            # delete key from dict
            del contacts[name]
            print(f'{name} contact has been deleted successfully!!!')
        else:
            print('Oops! Contact not found!!!')
    elif user_choice == 4:
        print("Displaying contacts ...\n")
        # delay for about 5 seconds
        time.sleep(5)
         # Use enumerate to show contacts with numbers
        for index, (name, phone_num) in enumerate(contacts.items(), 1):
            print(f"{index}. {name} -> {phone_num}")
    elif user_choice == 5:
        # added a new functionality for searching contact by phone number
        phone_num = input("Enter phone number to search: ").replace(' ','')
        # check if the phone number is valid and has 11 digits
        if phone_num.isdigit() and len(phone_num) == 11:
            # use list comprehension to find the matching names for the phone number
            matching_names = [name for name, num in contacts.items() if num == phone_num]
            # check if there are any matching names
            if matching_names:
                print(f'The following name have the phone number {phone_num}:')
                for name in matching_names:
                    print(name)
            else:
                print(f'No contact found with the phone number {phone_num}.')
        else:
            print("Invalid phone number. Please enter a valid 11-digit number.")
    elif user_choice == 6:
        # Search by name
        search_name = input("Enter the name to search: ").title().strip()
        matching_contacts = {name: phone_num for name, phone_num in contacts.items() if search_name in name}
        if matching_contacts:
            for name, phone_num in matching_contacts.items():
                print(f'{name} -> {phone_num}')
        else:print(f'No contacts found with the name "{search_name}".')
    elif user_choice == 7:
        # added a new functionality for sorting contacts by name
        print("Sorting contacts by name ...\n")
        # delay for about 5 seconds
        time.sleep(5)
        # use the sorted function to sort the keys of the contacts dictionary
        sorted_names = sorted(contacts.keys())
        # loop through the sorted names and print them with their values
        for name in sorted_names:
            print(f'{name} -> {contacts[name]}')
    elif user_choice == 8:
        # added a new functionality for sorting contacts by phone number
        print("Sorting contacts by phone number ...\n")
        # delay for about 5 seconds
        time.sleep(5)
        # use the sorted function to sort the values of the contacts dictionary
        sorted_phone_nums = sorted(contacts.values())
        # loop through the sorted phone numbers and print them with their keys
        for phone_num in sorted_phone_nums:
            # use list comprehension to find the matching names for the phone number
            matching_names = [name for name, num in contacts.items() if num == phone_num]
            # print the phone number with the matching names
            print(f'{phone_num} -> {", ".join(matching_names)}')
    else:
        print('Invalid Input!!! Please, make sure you enter a number between 1 - 9. Thanks')