import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pickle

# Create the main window
root = tk.Tk()
root.title("Event Management App")
root.geometry("800x400")
root.configure(bg="#000000")  # Set background color to black

# Create style for ttk elements
style = ttk.Style()
style.theme_create(
    "dark",
    settings={
        "TLabel": {
            "configure": {
                "foreground": "#C0C0C0",  # Set label foreground color to silver
                "background": "#000000",  # Set label background color to black
                "font": ("Helvetica", 12),
            }
        },
        "TButton": {
            "configure": {
                "foreground": "#000000",  # Set button foreground color to black
                "background": "#C0C0C0",  # Set button background color to silver
                "font": ("Helvetica", 12, "bold"),
            }
        },
        "TEntry": {
            "configure": {
                "foreground": "#C0C0C0",  # Set entry foreground color to silver
                "background": "#000000",  # Set entry background color to black
                "font": ("Helvetica", 12),
            }
        },
        "TListbox": {
            "configure": {
                "foreground": "#C0C0C0",  # Set listbox foreground color to silver
                "background": "#000000",  # Set listbox background color to black
                "font": ("Helvetica", 12),
            }
        },
    },
)
style.theme_use("dark")

# Function to save data to a pickle file
def save_data(data, filename):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)

# Function to load data from a pickle file
def load_data(filename):
    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []

# Create event information list
event_info = load_data("event_info.pkl")

# Function to save event information
def save_event_info():
    event_name = txt_event_name.get()
    event_date = txt_event_date.get()
    event_location = txt_event_location.get()
    if event_name and event_date and event_location:
        event_id = len(event_info) + 1  # Generate a unique ID
        event_info.append({"ID": event_id, "Event Name": event_name, "Event Date": event_date, "Event Location": event_location})
        save_data(event_info, "event_info.pkl")
        messagebox.showinfo("Success", "Event information saved successfully.")
        clear_fields()
    else:
        messagebox.showwarning("Error", "Please fill in all the fields.")

# Function to clear input fields
def clear_fields():
    txt_event_name.delete(0, tk.END)
    txt_event_date.delete(0, tk.END)
    txt_event_location.delete(0, tk.END)

# Function to open the Add Event Information window
def open_add_event_window():
    global txt_event_name, txt_event_date, txt_event_location  # Declare variables as global
    add_event_window = tk.Toplevel(root)
    add_event_window.title("Add Event Information")
    add_event_window.geometry("400x300")
    add_event_window.configure(bg="#000000")  # Set background color to black
    lbl_event_name = ttk.Label(add_event_window, text="Event Name:", style="TLabel")
    lbl_event_name.pack(pady=10)
    txt_event_name = ttk.Entry(add_event_window, width=30)
    txt_event_name.pack()
    lbl_event_date = ttk.Label(add_event_window, text="Event Date:", style="TLabel")
    lbl_event_date.pack(pady=10)
    txt_event_date = ttk.Entry(add_event_window, width=30)
    txt_event_date.pack()
    lbl_event_location = ttk.Label(add_event_window, text="Event Location:", style="TLabel")
    lbl_event_location.pack(pady=10)
    txt_event_location = ttk.Entry(add_event_window, width=30)
    txt_event_location.pack()
    btn_save_event_info = ttk.Button(add_event_window, text="Save", command=save_event_info, style="TButton")
    btn_save_event_info.pack(pady=10)

# Create Add Event Information Button
btn_add_event_info = ttk.Button(root, text="Add Event Information", command=open_add_event_window, style="TButton")
btn_add_event_info.place(x=20, y=20)

# Function to search event information by ID
def search_event_by_id():
    event_id = txt_search_id.get()
    if event_id:
        for event in event_info:
            if event.get("ID") == int(event_id):  # Convert event ID to integer for comparison
                display_event_info(event)
                return
        messagebox.showinfo("Search Results", f"No event found with ID: {event_id}")
    else:
        messagebox.showwarning("Error", "Please enter an ID to search.")

# Function to display event information
def display_event_info(event):
    result_window = tk.Toplevel(root)
    result_window.title("Event Details")
    result_window.geometry("400x300")
    result_window.configure(bg="#000000")  # Set background color to black
    
    # Create a frame to organize labels
    frame = ttk.Frame(result_window, padding=20)
    frame.pack(fill=tk.BOTH, expand=True)

    # Create labels to display event details
    lbl_event_id = ttk.Label(frame, text=f"Event ID: {event['ID']}", style="TLabel")
    lbl_event_id.pack(anchor=tk.W)

    lbl_event_name = ttk.Label(frame, text=f"Event Name: {event['Event Name']}", style="TLabel")
    lbl_event_name.pack(anchor=tk.W)

    lbl_event_date = ttk.Label(frame, text=f"Event Date: {event['Event Date']}", style="TLabel")
    lbl_event_date.pack(anchor=tk.W)

    lbl_event_location = ttk.Label(frame, text=f"Event Location: {event['Event Location']}", style="TLabel")
    lbl_event_location.pack(anchor=tk.W)

    # Button to close the window
    btn_close = ttk.Button(frame, text="Close", command=result_window.destroy, style="TButton")
    btn_close.pack(pady=10)

# Create Search Entry Field and Button
lbl_search_id = ttk.Label(root, text="Search by ID:", style="TLabel")
lbl_search_id.place(x=20, y=60)
txt_search_id = ttk.Entry(root, width=10)
txt_search_id.place(x=120, y=60)

btn_search = ttk.Button(root, text="Search", command=search_event_by_id, style="TButton")
btn_search.place(x=180, y=60)




# Function to save data to a pickle file
def save_data(data, filename):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)

# Function to load data from a pickle file
def load_data(filename):
    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return {}


# Create employees dictionary
employees = load_data("employees.pkl")
if not employees:
    employees = {}

# Function to save employee information
def save_employee_info():
    employee_name = txt_employee_name.get()
    employee_id = txt_employee_id.get()
    if employee_name and employee_id:
        employees[employee_id] = employee_name
        save_data(employees, "employees.pkl")
        messagebox.showinfo("Success", "Employee information saved successfully.")
        display_employees()
        clear_employee_fields()
    else:
        messagebox.showwarning("Error", "Please fill in all the fields.")

# Function to delete employee
def delete_employee():
    employee_id = txt_employee_id.get()
    if employee_id in employees:
        del employees[employee_id]
        save_data(employees, "employees.pkl")
        messagebox.showinfo("Success", "Employee deleted successfully.")
        display_employees()
        clear_employee_fields()
    else:
        messagebox.showwarning("Error", "Employee not found.")

# Function to modify employee
def modify_employee():
    employee_id = txt_employee_id.get()
    employee_name = txt_employee_name.get()
    if employee_id in employees:
        employees[employee_id] = employee_name
        save_data(employees, "employees.pkl")
        messagebox.showinfo("Success", "Employee modified successfully.")
        display_employees()
        clear_employee_fields()
    else:
        messagebox.showwarning("Error", "Employee not found.")

# Function to display employees
def display_employees():
    listbox_employees.delete(0, tk.END)
    for employee_id, employee_name in employees.items():
        listbox_employees.insert(tk.END, f"ID: {employee_id}, Name: {employee_name}")

# Function to clear employee fields
def clear_employee_fields():
    txt_employee_name.delete(0, tk.END)
    txt_employee_id.delete(0, tk.END)

# Create Employee Information Section
lbl_employee_name = ttk.Label(root, text="Employee Name:", style="TLabel")
lbl_employee_name.place(x=20, y=100)
txt_employee_name = ttk.Entry(root, width=30)
txt_employee_name.place(x=150, y=100)

lbl_employee_id = ttk.Label(root, text="Employee ID:", style="TLabel")
lbl_employee_id.place(x=20, y=130)
txt_employee_id = ttk.Entry(root, width=10)
txt_employee_id.place(x=150, y=130)

btn_add_employee = ttk.Button(root, text="Add Employee", command=save_employee_info, style="TButton")
btn_add_employee.place(x=20, y=160)

btn_delete_employee = ttk.Button(root, text="Delete Employee", command=delete_employee, style="TButton")
btn_delete_employee.place(x=190, y=160)

btn_modify_employee = ttk.Button(root, text="Modify Employee", command=modify_employee, style="TButton")
btn_modify_employee.place(x=330, y=160)

listbox_employees = tk.Listbox(root, width=50, height=8, bg="#000000", fg="#C0C0C0", font=("Helvetica", 12))
listbox_employees.place(x=20, y=200)

btn_display_employees = ttk.Button(root, text="Display Employees", command=display_employees, style="TButton")
btn_display_employees.place(x=20, y=350)
# Function to save client information
def save_client_info():
    global client_info
    if 'client_info' not in globals():
        client_info = []
    
    client_name = txt_client_name.get()
    client_email = txt_client_email.get()
    client_phone = txt_client_phone.get()
    
    if client_name and client_email and client_phone:
        client_id = len(client_info) + 1  # Generate a unique ID
        client_info.append({"ID": client_id, "Client Name": client_name, "Email": client_email, "Phone": client_phone})
        save_data(client_info, "client_info.pkl")
        messagebox.showinfo("Success", "Client information saved successfully.")
        clear_client_fields()
    else:
        messagebox.showwarning("Error", "Please fill in all the fields.")

# Function to clear client fields
def clear_client_fields():
    txt_client_name.delete(0, tk.END)
    txt_client_email.delete(0, tk.END)
    txt_client_phone.delete(0, tk.END)

# Function to open the Add Client Information window
def open_add_client_window():
    global txt_client_name, txt_client_email, txt_client_phone  # Declare variables as global
    add_client_window = tk.Toplevel(root)
    add_client_window.title("Add Client Information")
    add_client_window.geometry("400x300")
    add_client_window.configure(bg="#000000")  # Set background color to black
    lbl_client_name = ttk.Label(add_client_window, text="Client Name:", style="TLabel")
    lbl_client_name.pack(pady=10)
    txt_client_name = ttk.Entry(add_client_window, width=30)
    txt_client_name.pack()
    lbl_client_email = ttk.Label(add_client_window, text="Client Email:", style="TLabel")
    lbl_client_email.pack(pady=10)
    txt_client_email = ttk.Entry(add_client_window, width=30)
    txt_client_email.pack()
    lbl_client_phone = ttk.Label(add_client_window, text="Client Phone:", style="TLabel")
    lbl_client_phone.pack(pady=10)
    txt_client_phone = ttk.Entry(add_client_window, width=30)
    txt_client_phone.pack()
    btn_save_client_info = ttk.Button(add_client_window, text="Save", command=save_client_info, style="TButton")
    btn_save_client_info.pack(pady=10)

# Create Add Client Information Button
btn_add_client_info = ttk.Button(root, text="Add Client Information", command=open_add_client_window, style="TButton")
btn_add_client_info.place(x=20, y=380)

# Function to load data from a file
def load_data(filename):
    try:
        with open(filename, "rb") as file:
            data = pickle.load(file)
        return data
    except FileNotFoundError:
        return None

# Function to save data to a file
def save_data(data, filename):
    with open(filename, "wb") as file:
        pickle.dump(data, file)

# Create supplier information list
supplier_info = load_data("supplier_info.pkl")
if supplier_info is None:
    supplier_info = []

# Function to save supplier information
def save_supplier_info():
    global supplier_info
    
    supplier_name = txt_supplier_name.get()
    supplier_email = txt_supplier_email.get()
    supplier_phone = txt_supplier_phone.get()
    
    if supplier_name and supplier_email and supplier_phone:
        supplier_id = len(supplier_info) + 1  # Generate a unique ID
        supplier_info.append({"ID": supplier_id, "Supplier Name": supplier_name, "Email": supplier_email, "Phone": supplier_phone})
        save_data(supplier_info, "supplier_info.pkl")
        messagebox.showinfo("Success", "Supplier information saved successfully.")
        clear_supplier_fields()
    else:
        messagebox.showwarning("Error", "Please fill in all the fields.")

# Function to clear supplier fields
def clear_supplier_fields():
    txt_supplier_name.delete(0, tk.END)
    txt_supplier_email.delete(0, tk.END)
    txt_supplier_phone.delete(0, tk.END)

# Function to open the Add Supplier Information window
def open_add_supplier_window():
    global txt_supplier_name, txt_supplier_email, txt_supplier_phone  # Declare variables as global
    add_supplier_window = tk.Toplevel(root)
    add_supplier_window.title("Add Supplier Information")
    add_supplier_window.geometry("400x300")
    add_supplier_window.configure(bg="#000000")  # Set background color to black
    lbl_supplier_name = ttk.Label(add_supplier_window, text="Supplier Name:", style="TLabel")
    lbl_supplier_name.pack(pady=10)
    txt_supplier_name = ttk.Entry(add_supplier_window, width=30)
    txt_supplier_name.pack()
    lbl_supplier_email = ttk.Label(add_supplier_window, text="Supplier Email:", style="TLabel")
    lbl_supplier_email.pack(pady=10)
    txt_supplier_email = ttk.Entry(add_supplier_window, width=30)
    txt_supplier_email.pack()
    lbl_supplier_phone = ttk.Label(add_supplier_window, text="Supplier Phone:", style="TLabel")
    lbl_supplier_phone.pack(pady=10)
    txt_supplier_phone = ttk.Entry(add_supplier_window, width=30)
    txt_supplier_phone.pack()
    btn_save_supplier_info = ttk.Button(add_supplier_window, text="Save", command=save_supplier_info, style="TButton")
    btn_save_supplier_info.pack(pady=10)

# Create Add Supplier Information Button
btn_add_supplier_info = ttk.Button(root, text="Add Supplier Information", command=open_add_supplier_window, style="TButton")
btn_add_supplier_info.place(x=20, y=420)

# Function to search supplier information by ID
def search_supplier_by_id():
    supplier_id = txt_search_supplier_id.get()
    if supplier_id:
        for supplier in supplier_info:
            if supplier.get("ID") == int(supplier_id):  # Convert supplier ID to integer for comparison
                display_supplier_info(supplier)
                return
        messagebox.showinfo("Search Results", f"No supplier found with ID: {supplier_id}")
    else:
        messagebox.showwarning("Error", "Please enter an ID to search.")

# Function to display supplier information
def display_supplier_info(supplier):
    result_window = tk.Toplevel(root)
    result_window.title("Supplier Details")
    result_window.geometry("400x300")
    result_window.configure(bg="#000000")  # Set background color to black
    
    # Create a frame to organize labels
    frame = ttk.Frame(result_window, padding=20)
    frame.pack(fill=tk.BOTH, expand=True)

    # Create labels to display supplier details
    lbl_supplier_id = ttk.Label(frame, text=f"Supplier ID: {supplier['ID']}", style="TLabel")
    lbl_supplier_id.pack(anchor=tk.W)

    lbl_supplier_name = ttk.Label(frame, text=f"Supplier Name: {supplier['Supplier Name']}", style="TLabel")
    lbl_supplier_name.pack(anchor=tk.W)

    lbl_supplier_email = ttk.Label(frame, text=f"Supplier Email: {supplier['Email']}", style="TLabel")
    lbl_supplier_email.pack(anchor=tk.W)

    lbl_supplier_phone = ttk.Label(frame, text=f"Supplier Phone: {supplier['Phone']}", style="TLabel")
    lbl_supplier_phone.pack(anchor=tk.W)

    # Button to close the window
    btn_close = ttk.Button(frame, text="Close", command=result_window.destroy, style="TButton")
    btn_close.pack(pady=10)

# Create Search Entry Field and Button for Supplier
lbl_search_supplier_id = ttk.Label(root, text="Search by Supplier ID:", style="TLabel")
lbl_search_supplier_id.place(x=20, y=460)
txt_search_supplier_id = ttk.Entry(root, width=10)
txt_search_supplier_id.place(x=160, y=460)

btn_search_supplier = ttk.Button(root, text="Search Supplier", command=search_supplier_by_id, style="TButton")
btn_search_supplier.place(x=260, y=460)



# Create guest information list
guest_info = load_data("guest_info.pkl")

# Function to save guest information
def save_guest_info():
    global guest_info
    if guest_info is None:
        guest_info = []
    
    guest_name = txt_guest_name.get()
    guest_email = txt_guest_email.get()
    guest_phone = txt_guest_phone.get()
    
    if guest_name and guest_email and guest_phone:
        guest_id = len(guest_info) + 1  # Generate a unique ID
        guest_info.append({"ID": guest_id, "Guest Name": guest_name, "Email": guest_email, "Phone": guest_phone})
        save_data(guest_info, "guest_info.pkl")
        messagebox.showinfo("Success", "Guest information saved successfully.")
        clear_guest_fields()
    else:
        messagebox.showwarning("Error", "Please fill in all the fields.")

# Function to clear guest fields
def clear_guest_fields():
    txt_guest_name.delete(0, tk.END)
    txt_guest_email.delete(0, tk.END)
    txt_guest_phone.delete(0, tk.END)

# Function to open the Add Guest Information window
def open_add_guest_window():
    global txt_guest_name, txt_guest_email, txt_guest_phone  # Declare variables as global
    add_guest_window = tk.Toplevel(root)
    add_guest_window.title("Add Guest Information")
    add_guest_window.geometry("400x300")
    add_guest_window.configure(bg="#000000")  # Set background color to black
    lbl_guest_name = ttk.Label(add_guest_window, text="Guest Name:", style="TLabel")
    lbl_guest_name.pack(pady=10)
    txt_guest_name = ttk.Entry(add_guest_window, width=30)
    txt_guest_name.pack()
    lbl_guest_email = ttk.Label(add_guest_window, text="Guest Email:", style="TLabel")
    lbl_guest_email.pack(pady=10)
    txt_guest_email = ttk.Entry(add_guest_window, width=30)
    txt_guest_email.pack()
    lbl_guest_phone = ttk.Label(add_guest_window, text="Guest Phone:", style="TLabel")
    lbl_guest_phone.pack(pady=10)
    txt_guest_phone = ttk.Entry(add_guest_window, width=30)
    txt_guest_phone.pack()
    btn_save_guest_info = ttk.Button(add_guest_window, text="Save", command=save_guest_info, style="TButton")
    btn_save_guest_info.pack(pady=10)

# Create Add Guest Information Button
btn_add_guest_info = ttk.Button(root, text="Add Guest Information", command=open_add_guest_window, style="TButton")
btn_add_guest_info.place(x=20, y=510)

# Function to search guest information by ID
def search_guest_by_id():
    guest_id = txt_search_guest_id.get()
    if guest_id:
        for guest in guest_info:
            if guest.get("ID") == int(guest_id):  # Convert guest ID to integer for comparison
                display_guest_info(guest)
                return
        messagebox.showinfo("Search Results", f"No guest found with ID: {guest_id}")
    else:
        messagebox.showwarning("Error", "Please enter an ID to search.")

# Function to display guest information
def display_guest_info(guest):
    result_window = tk.Toplevel(root)
    result_window.title("Guest Details")
    result_window.geometry("400x300")
    result_window.configure(bg="#000000")  # Set background color to black
    
    # Create a frame to organize labels
    frame = ttk.Frame(result_window, padding=20)
    frame.pack(fill=tk.BOTH, expand=True)

    # Create labels to display guest details
    lbl_guest_id = ttk.Label(frame, text=f"Guest ID: {guest['ID']}", style="TLabel")
    lbl_guest_id.pack(anchor=tk.W)

    lbl_guest_name = ttk.Label(frame, text=f"Guest Name: {guest['Guest Name']}", style="TLabel")
    lbl_guest_name.pack(anchor=tk.W)

    lbl_guest_email = ttk.Label(frame, text=f"Guest Email: {guest['Email']}", style="TLabel")
    lbl_guest_email.pack(anchor=tk.W)

    lbl_guest_phone = ttk.Label(frame, text=f"Guest Phone: {guest['Phone']}", style="TLabel")
    lbl_guest_phone.pack(anchor=tk.W)

    # Button to close the window
    btn_close = ttk.Button(frame, text="Close", command=result_window.destroy, style="TButton")
    btn_close.pack(pady=10)

# Create Search Entry Field and Button for Guest
lbl_search_guest_id = ttk.Label(root, text="Search by Guest ID:", style="TLabel")
lbl_search_guest_id.place(x=20, y=540)
txt_search_guest_id = ttk.Entry(root, width=10)
txt_search_guest_id.place(x=160, y=540)

btn_search_guest = ttk.Button(root, text="Search Guest", command=search_guest_by_id, style="TButton")
btn_search_guest.place(x=260, y=540)

# Start the main event loop
root.mainloop()