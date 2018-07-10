#!/usr/bin/env python3
import csv
FILENAME = "contacts.csv"
'''
Daniel Diaz Santiago
COP2002.002
Module 7 Homework
'''

def main():
    print("Contact Manager\n")
    menu()

def menu():
    contacts = _read()
    
    print("COMMAND MENU")
    print("list - Display all contacts")
    print("view - View a contact")
    print("add - Add a contact")
    print("del - Delete a contact")
    print("exit - Exit program\n")

    while True:
        cmd = str(input("Command: "))

        if cmd.lower() == "list":
            list(contacts)
        elif cmd.lower() == "view":
            view(contacts)
        elif cmd.lower() == "add":
            add(contacts)
        elif cmd.lower() == "del":
            delete(contacts)
        elif cmd.lower() == "exit":
            print("Bye!")
            return False
        else:
            print("\n\"" + cmd + "\" not found.")

## Read data from "contacts.csv"
def _read():
    contacts = []
    with open(FILENAME, newline = "") as f:
        reader = csv.reader(f)

        for i in reader:
            contacts.append(i)
    return contacts

## Write data into "contacts.csv"
def _write(contacts):
    with open(FILENAME, "w", newline = "") as f:
        write = csv.writer(f)
        write.writerows(contacts)

## List all contact names in "contacts.csv"
def list(contacts):
    contacts = _read()
    for i in range(len(contacts)):
        cont = contacts[i]
        print(str(i+1) + ". " + cont[0])
    print()

## View X contact
def view(contacts):
    name = str(input("Contact name: "))
    j = 0
    print(contacts[1][0])
    while j < len(contacts):
        if name.lower() == contacts[j][0].lower():
            print("\nName: " + contacts[j][0] + "\nEmail: " + contacts[j][1] + "\nPhone: " + contacts[j][2])
            break
        elif name.lower() != contacts[j][0].lower():
            j += 1
        else:
            print("Contact \"" + name + "\" not found.")
            break
    print()

## Add a contact to "contacts.csv"
def add(contacts):
    contact = []
    
    name = str(input("Name: "))
    email = str(input("Email: "))
    phone = str(input("Phone: "))

    ## Append to contact variable
    contact.append(name)
    contact.append(email)
    contact.append(phone)

    ## Append contact variable to contacts variable
    contacts.append(contact)
    
    # Write data to "contacts.csv"
    _write(contacts)
    print(name + " was added.\n")

## Delete contact from "contacts.csv"
def delete(contacts):
    num = int(input("Number: "))
    index = num - 1

    print("Contact \"" + str(contacts[index][0]) + "\" was deleted\n")
    new_contacts = contacts.pop(index)
    
    # Write data to "contacts.csv"
    _write(contacts)

if __name__== "__main__":
    main()
