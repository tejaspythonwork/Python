import tkinter as tk
from admin_gui import AdminGUI  
from pharmacy_manager_gui import PharmacyManagerGUI 



root = tk.Tk()
root.title("Pharmacy System")
root.geometry("300x200")  


def show_admin_data():
    
    admin_window = tk.Toplevel(root)
    admin_window.title("Admin Panel")
    admin_window.geometry("400x300")

    
    AdminGUI(admin_window)

def show_pharmacy_manager_data():
    
    pharmacy_window = tk.Toplevel(root)
    pharmacy_window.title("Pharmacy Manager Data")
    tk.Label(pharmacy_window, text="Pharmacy Manager-specific data displayed here.").pack(pady=20)
    PharmacyManagerGUI(pharmacy_window)


admin_button = tk.Button(root, text="Admin", width=15, height=2, command=show_admin_data)
admin_button.pack(pady=20)


pharmacy_manager_button = tk.Button(root, text="Pharmacy Manager", width=15, height=2, command=show_pharmacy_manager_data)
pharmacy_manager_button.pack(pady=10)


root.mainloop()
