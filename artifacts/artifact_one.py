"""
Contact & Task Manager Application
A comprehensive management system for contacts, appointments, and tasks.
Provides CRUD operations with validation for all data types.
"""

import re
from datetime import datetime

# ==============================================================================
# DATA STORES
# ==============================================================================
# Global dictionaries to store application data
contacts = {}        # Stores contact information {contact_id: {name, email, phone}}
appointments = {}    # Stores appointments {app_id: {title, date_time, location}}
tasks = {}           # Stores tasks {task_id: {description, due_date}}

# ==============================================================================
# VALIDATION HELPERS
# ==============================================================================
# Functions to validate user input across the application

def validate_email(email):
    """
    Validate email format using regex.
    
    Args:
        email (str): Email address to validate
        
    Returns:
        Match object if valid, None if invalid
    """
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def validate_phone(phone):
    """
    Validate phone number format (must be exactly 10 digits).
    
    Args:
        phone (str): Phone number to validate
        
    Returns:
        Match object if valid, None if invalid
    """
    return re.match(r"\d{10}$", phone)

def validate_date(date_str):
    """
    Validate date and time format (YYYY-MM-DD HH:MM).
    
    Args:
        date_str (str): Date string to validate
        
    Returns:
        bool: True if valid format, False otherwise
    """
    try:
        datetime.strptime(date_str, "%Y-%m-%d %H:%M")
        return True
    except ValueError:
        return False

# ==============================================================================
# CONTACT MANAGEMENT FUNCTIONS
# ==============================================================================

def create_contact(contact_id, name, email, phone):
    """
    Create a new contact with validation.
    
    Args:
        contact_id (str): Unique identifier for the contact
        name (str): Contact's full name
        email (str): Contact's email address
        phone (str): Contact's phone number (10 digits)
        
    Returns:
        str: Success or error message
    """
    if not validate_email(email):
        return "Invalid email format."
    if not validate_phone(phone):
        return "Phone must be 10 digits."
    contacts[contact_id] = {"name": name, "email": email, "phone": phone}
    return f"Contact '{name}' created."

def update_contact(contact_id, name=None, email=None, phone=None):
    """
    Update an existing contact's information.
    
    Args:
        contact_id (str): ID of contact to update
        name (str, optional): New name
        email (str, optional): New email
        phone (str, optional): New phone number
        
    Returns:
        str: Success or error message
    """
    if contact_id not in contacts:
        return "Contact not found."
    if email and not validate_email(email):
        return "Invalid email format."
    if phone and not validate_phone(phone):
        return "Phone must be 10 digits."
    if name: contacts[contact_id]["name"] = name
    if email: contacts[contact_id]["email"] = email
    if phone: contacts[contact_id]["phone"] = phone
    return f"Contact '{contact_id}' updated."

# ==============================================================================
# APPOINTMENT MANAGEMENT FUNCTIONS
# ==============================================================================

def create_appointment(app_id, title, date_time, location):
    """
    Create a new appointment with validation.
    
    Args:
        app_id (str): Unique identifier for the appointment
        title (str): Appointment title/subject
        date_time (str): Date and time (format: YYYY-MM-DD HH:MM)
        location (str): Appointment location
        
    Returns:
        str: Success or error message
    """
    if not validate_date(date_time):
        return "Invalid date format. Use YYYY-MM-DD HH:MM"
    appointments[app_id] = {"title": title, "date_time": date_time, "location": location}
    return f"Appointment '{title}' created."

def update_appointment(app_id, title=None, date_time=None, location=None):
    """
    Update an existing appointment's information.
    
    Args:
        app_id (str): ID of appointment to update
        title (str, optional): New title
        date_time (str, optional): New date and time
        location (str, optional): New location
        
    Returns:
        str: Success or error message
    """
    if app_id not in appointments:
        return "Appointment not found."
    if date_time and not validate_date(date_time):
        return "Invalid date format."
    if title: appointments[app_id]["title"] = title
    if date_time: appointments[app_id]["date_time"] = date_time
    if location: appointments[app_id]["location"] = location
    return f"Appointment '{app_id}' updated."

# ==============================================================================
# TASK MANAGEMENT FUNCTIONS
# ==============================================================================

def create_task(task_id, description, due_date):
    """
    Create a new task with validation.
    
    Args:
        task_id (str): Unique identifier for the task
        description (str): Task description
        due_date (str): Due date and time (format: YYYY-MM-DD HH:MM)
        
    Returns:
        str: Success or error message
    """
    if not validate_date(due_date):
        return "Invalid date format. Use YYYY-MM-DD HH:MM"
    tasks[task_id] = {"description": description, "due_date": due_date}
    return f"Task '{description}' created."

def update_task(task_id, description=None, due_date=None):
    """
    Update an existing task's information.
    
    Args:
        task_id (str): ID of task to update
        description (str, optional): New description
        due_date (str, optional): New due date and time
        
    Returns:
        str: Success or error message
    """
    if task_id not in tasks:
        return "Task not found."
    if due_date and not validate_date(due_date):
        return "Invalid date format."
    if description: tasks[task_id]["description"] = description
    if due_date: tasks[task_id]["due_date"] = due_date
    return f"Task '{task_id}' updated."

# ==============================================================================
# DELETE FUNCTIONS
# ==============================================================================

def delete_contact(contact_id):
    """
    Delete a contact from the system.
    
    Args:
        contact_id (str): ID of contact to delete
        
    Returns:
        str: Success or error message
    """
    if contact_id not in contacts:
        return "Contact not found."
    del contacts[contact_id]
    return f"Contact '{contact_id}' deleted."

def delete_appointment(app_id):
    """
    Delete an appointment from the system.
    
    Args:
        app_id (str): ID of appointment to delete
        
    Returns:
        str: Success or error message
    """
    if app_id not in appointments:
        return "Appointment not found."
    del appointments[app_id]
    return f"Appointment '{app_id}' deleted."

def delete_task(task_id):
    """
    Delete a task from the system.
    
    Args:
        task_id (str): ID of task to delete
        
    Returns:
        str: Success or error message
    """
    if task_id not in tasks:
        return "Task not found."
    del tasks[task_id]
    return f"Task '{task_id}' deleted."

# ==============================================================================
# VIEW FUNCTIONS
# ==============================================================================

def view_contacts():
    """
    Display all contacts in a formatted table.
    
    Returns:
        str: Formatted contact list or message if no contacts exist
    """
    if not contacts:
        return "No contacts found."
    result = "=== CONTACTS ===\n"
    for contact_id, info in contacts.items():
        result += f"ID: {contact_id}\n  Name: {info['name']}\n  Email: {info['email']}\n  Phone: {info['phone']}\n"
    return result

def view_appointments():
    """
    Display all appointments in a formatted table.
    
    Returns:
        str: Formatted appointment list or message if no appointments exist
    """
    if not appointments:
        return "No appointments found."
    result = "=== APPOINTMENTS ===\n"
    for app_id, info in appointments.items():
        result += f"ID: {app_id}\n  Title: {info['title']}\n  Date/Time: {info['date_time']}\n  Location: {info['location']}\n"
    return result

def view_tasks():
    """
    Display all tasks in a formatted table.
    
    Returns:
        str: Formatted task list or message if no tasks exist
    """
    if not tasks:
        return "No tasks found."
    result = "=== TASKS ===\n"
    for task_id, info in tasks.items():
        result += f"ID: {task_id}\n  Description: {info['description']}\n  Due Date: {info['due_date']}\n"
    return result

# ==============================================================================
# MENU DISPLAY FUNCTIONS
# ==============================================================================
# These functions display the various menu options to the user

def print_main_menu():
    """Display the main application menu."""
    print("\n" + "="*40)
    print("      CONTACT & TASK MANAGER")
    print("="*40)
    print("1. Contact Management")
    print("2. Appointment Management")
    print("3. Task Management")
    print("4. View All")
    print("5. Exit")
    print("="*40)

def print_contact_menu():
    """Display the contact management submenu."""
    print("\n--- CONTACT MANAGEMENT ---")
    print("1. Create Contact")
    print("2. View All Contacts")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Back to Main Menu")

def print_appointment_menu():
    """Display the appointment management submenu."""
    print("\n--- APPOINTMENT MANAGEMENT ---")
    print("1. Create Appointment")
    print("2. View All Appointments")
    print("3. Update Appointment")
    print("4. Delete Appointment")
    print("5. Back to Main Menu")

def print_task_menu():
    """Display the task management submenu."""
    print("\n--- TASK MANAGEMENT ---")
    print("1. Create Task")
    print("2. View All Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Back to Main Menu")

# ==============================================================================
# MANAGEMENT INTERFACE FUNCTIONS
# ==============================================================================
# These functions handle the interactive loops for each management category

def contact_management():
    """
    Handle contact management operations.
    Provides an interactive loop for creating, viewing, updating, and deleting contacts.
    """
    while True:
        print_contact_menu()
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            # Create a new contact
            try:
                contact_id = input("Enter contact ID: ").strip()
                name = input("Enter name: ").strip()
                email = input("Enter email: ").strip()
                phone = input("Enter phone (10 digits): ").strip()
                print(create_contact(contact_id, name, email, phone))
            except Exception as e:
                print(f"Error: {e}")
                
        elif choice == "2":
            # View all contacts
            print(view_contacts())
            
        elif choice == "3":
            # Update an existing contact
            try:
                contact_id = input("Enter contact ID to update: ").strip()
                if contact_id not in contacts:
                    print("Contact not found.")
                    continue
                name = input("Enter new name (press Enter to skip): ").strip() or None
                email = input("Enter new email (press Enter to skip): ").strip() or None
                phone = input("Enter new phone (press Enter to skip): ").strip() or None
                print(update_contact(contact_id, name, email, phone))
            except Exception as e:
                print(f"Error: {e}")
                
        elif choice == "4":
            # Delete a contact
            try:
                contact_id = input("Enter contact ID to delete: ").strip()
                print(delete_contact(contact_id))
            except Exception as e:
                print(f"Error: {e}")
                
        elif choice == "5":
            # Return to main menu
            break
        else:
            print("Invalid choice. Please try again.")

def appointment_management():
    """
    Handle appointment management operations.
    Provides an interactive loop for creating, viewing, updating, and deleting appointments.
    """
    while True:
        print_appointment_menu()
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            # Create a new appointment
            try:
                app_id = input("Enter appointment ID: ").strip()
                title = input("Enter title: ").strip()
                date_time = input("Enter date and time (YYYY-MM-DD HH:MM): ").strip()
                location = input("Enter location: ").strip()
                print(create_appointment(app_id, title, date_time, location))
            except Exception as e:
                print(f"Error: {e}")
                
        elif choice == "2":
            # View all appointments
            print(view_appointments())
            
        elif choice == "3":
            # Update an existing appointment
            try:
                app_id = input("Enter appointment ID to update: ").strip()
                if app_id not in appointments:
                    print("Appointment not found.")
                    continue
                title = input("Enter new title (press Enter to skip): ").strip() or None
                date_time = input("Enter new date/time (press Enter to skip): ").strip() or None
                location = input("Enter new location (press Enter to skip): ").strip() or None
                print(update_appointment(app_id, title, date_time, location))
            except Exception as e:
                print(f"Error: {e}")
                
        elif choice == "4":
            # Delete an appointment
            try:
                app_id = input("Enter appointment ID to delete: ").strip()
                print(delete_appointment(app_id))
            except Exception as e:
                print(f"Error: {e}")
                
        elif choice == "5":
            # Return to main menu
            break
        else:
            print("Invalid choice. Please try again.")

def task_management():
    """
    Handle task management operations.
    Provides an interactive loop for creating, viewing, updating, and deleting tasks.
    """
    while True:
        print_task_menu()
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            # Create a new task
            try:
                task_id = input("Enter task ID: ").strip()
                description = input("Enter description: ").strip()
                due_date = input("Enter due date (YYYY-MM-DD HH:MM): ").strip()
                print(create_task(task_id, description, due_date))
            except Exception as e:
                print(f"Error: {e}")
                
        elif choice == "2":
            # View all tasks
            print(view_tasks())
            
        elif choice == "3":
            # Update an existing task
            try:
                task_id = input("Enter task ID to update: ").strip()
                if task_id not in tasks:
                    print("Task not found.")
                    continue
                description = input("Enter new description (press Enter to skip): ").strip() or None
                due_date = input("Enter new due date (press Enter to skip): ").strip() or None
                print(update_task(task_id, description, due_date))
            except Exception as e:
                print(f"Error: {e}")
                
        elif choice == "4":
            # Delete a task
            try:
                task_id = input("Enter task ID to delete: ").strip()
                print(delete_task(task_id))
            except Exception as e:
                print(f"Error: {e}")
                
        elif choice == "5":
            # Return to main menu
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    """
    Main application entry point.
    Displays the main menu and routes user choices to appropriate management functions.
    """
    print("\nWelcome to Contact & Task Manager!")
    
    while True:
        print_main_menu()
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            # Navigate to contact management
            contact_management()
        elif choice == "2":
            # Navigate to appointment management
            appointment_management()
        elif choice == "3":
            # Navigate to task management
            task_management()
        elif choice == "4":
            # Display all data from all categories
            print(view_contacts())
            print(view_appointments())
            print(view_tasks())
        elif choice == "5":
            # Exit the application
            print("\nThank you for using Contact & Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# ==============================================================================
# APPLICATION ENTRY POINT
# ==============================================================================

if __name__ == "__main__":
    main()
