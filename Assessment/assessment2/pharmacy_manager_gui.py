import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
from db_connection import DatabaseConnection
from models import PharmacyManager

class PharmacyManagerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Pharmacy Manager")
        
        
        self.db = DatabaseConnection()
        self.pharmacy_manager = None 

        
        self.create_main_menu()
    
    def create_main_menu(self):
        self.clear_window()

        tk.Label(self.root, text="Pharmacy Manager System", font=("Arial", 18)).pack(pady=10)
        
        
        tk.Button(self.root, text="Register", command=self.register_window, width=20).pack(pady=5)
        tk.Button(self.root, text="Login", command=self.login_window, width=20).pack(pady=5)
        tk.Button(self.root, text="Add Medicine", command=self.add_medicine_window, width=20).pack(pady=5)
        tk.Button(self.root, text="View Medicines", command=self.view_medicine_window, width=20).pack(pady=5)
        tk.Button(self.root, text="Delete Medicine", command=self.delete_medicine_window, width=20).pack(pady=5)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    
    def register_window(self):
        self.clear_window()

        tk.Label(self.root, text="Register Pharmacy Manager", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.root, text="Username:").pack(pady=5)
        username_entry = tk.Entry(self.root)
        username_entry.pack()
        tk.Label(self.root, text="Password:").pack(pady=5)
        password_entry = tk.Entry(self.root, show="*")
        password_entry.pack()

        def register():
            username = username_entry.get()
            password = password_entry.get()
            if not username or not password:
                messagebox.showwarning("Input Error", "All fields are required!")
                return
            self.pharmacy_manager = PharmacyManager(username, password)
            self.pharmacy_manager.register(self.db)
            messagebox.showinfo("Success", "Registration successful!")
            self.create_main_menu()

        tk.Button(self.root, text="Register", command=register).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.create_main_menu).pack()


    def login_window(self):
        self.clear_window()
        
        tk.Label(self.root, text="Login", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.root, text="Username:").pack(pady=5)
        username_entry = tk.Entry(self.root)
        username_entry.pack()
        
        tk.Label(self.root, text="Password:").pack(pady=5)
        password_entry = tk.Entry(self.root, show="*")
        password_entry.pack()

        def login():
            username = username_entry.get()
            password = password_entry.get()
            if not username or not password:
                messagebox.showwarning("Input Error", "All fields are required!")
                return
            
            self.pharmacy_manager = PharmacyManager(username, password)
            if self.pharmacy_manager.login(self.db):
                messagebox.showinfo("Success", "Login successful!")
    
            else:
                messagebox.showerror("Login Failed", "Invalid username or password.")

        tk.Button(self.root, text="Login", command=login).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.create_main_menu).pack()








    
    def add_medicine_window(self):
        self.clear_window()

        tk.Label(self.root, text="Add Medicine", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.root, text="Medicine Name:").pack(pady=5)
        name_entry = tk.Entry(self.root)
        name_entry.pack()
        tk.Label(self.root, text="Quantity:").pack(pady=5)
        quantity_entry = tk.Entry(self.root)
        quantity_entry.pack()
        tk.Label(self.root, text="Price:").pack(pady=5)
        price_entry = tk.Entry(self.root)
        price_entry.pack()

        def add_medicine():
            name = name_entry.get()
            quantity = quantity_entry.get()
            price = price_entry.get()
            if not name or not quantity or not price:
                messagebox.showwarning("Input Error", "All fields are required!")
                return
            try:
                quantity = int(quantity)
                price = float(price)
                if self.pharmacy_manager is None:
                    raise ValueError("Pharmacy Manager is not logged in.")
                self.pharmacy_manager.add_medicine(self.db, name, quantity, price)
                messagebox.showinfo("Success", "Medicine added successfully!")
            except ValueError as ve:
                
                messagebox.showwarning("Input Error", str(ve))

        tk.Button(self.root, text="Add Medicine", command=add_medicine).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.create_main_menu).pack()

    
    def view_medicine_window(self):
        self.clear_window()

        tk.Label(self.root, text="Medicine List", font=("Arial", 16)).pack(pady=10)
        
        
        medicines = self.pharmacy_manager.view_medicine(self.db)
        
        
        columns = ("sr_no", "name", "quantity", "added_date", "added_by", "price")
        tree = ttk.Treeview(self.root, columns=columns, show="headings")
        tree.heading("sr_no", text="Sr No")
        tree.heading("name", text="Name")
        tree.heading("quantity", text="Quantity")
        tree.heading("added_date", text="Added Date")
        tree.heading("added_by", text="Added By")
        tree.heading("price", text="Price")

    
        for med in medicines:
            tree.insert("", tk.END, values=med)
        
        tree.pack(pady=10, fill=tk.BOTH, expand=True)
        tk.Button(self.root, text="Back", command=self.create_main_menu).pack()

    
    def delete_medicine_window(self):
        self.clear_window()

        tk.Label(self.root, text="Delete Medicine", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.root, text="Enter Medicine Sr No:").pack(pady=5)
        sr_no_entry = tk.Entry(self.root)
        sr_no_entry.pack()

        def delete_medicine():
            sr_no = sr_no_entry.get()
            if not sr_no:
                messagebox.showwarning("Input Error", "Sr No is required!")
                return
            if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this medicine?"):
                try:
                    sr_no = int(sr_no)
                    self.pharmacy_manager.delete_medicine(self.db, sr_no)
                    messagebox.showinfo("Success", "Medicine deleted successfully!")
                except ValueError:
                    messagebox.showwarning("Input Error", "Sr No must be an integer!")

        tk.Button(self.root, text="Delete Medicine", command=delete_medicine).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.create_main_menu).pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = PharmacyManagerGUI(root)
    root.mainloop()