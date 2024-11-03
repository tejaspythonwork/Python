import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from db_connection import DatabaseConnection
from models import Admin

class AdminGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin Panel")
        
        
        self.db = DatabaseConnection()
        self.admin = None  

        
        self.create_main_menu()

    def create_main_menu(self):
        self.clear_window()

        tk.Label(self.root, text="Admin Panel", font=("Arial", 18)).pack(pady=10)

        
        tk.Button(self.root, text="Register Admin", command=self.register_window, width=20).pack(pady=5)
        tk.Button(self.root,text= 'Login Admin',command=self.show_login_window,width=20,).pack(pady=5)
        tk.Button(self.root, text="View All Managers", command=self.view_managers_window, width=20).pack(pady=5)
        tk.Button(self.root, text="View All Medicines", command=self.view_medicines_window, width=20).pack(pady=5)


    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()


        
    # Register Admin window
    def register_window(self):
        self.clear_window()

        tk.Label(self.root, text="Register New Admin", font=("Arial", 16)).pack(pady=10)
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
            self.admin = Admin(username, password)
            self.admin.register(self.db)
            messagebox.showinfo("Success", "Admin registered successfully!")
            self.create_main_menu()

        tk.Button(self.root, text="Register", command=register).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.create_main_menu).pack()

    
    def show_login_window(self):
        self.clear_window()

        tk.Label(self.root, text="Admin Login", font=("Arial", 18)).pack(pady=10)
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
                messagebox.showwarning("Input Error", "Please enter both username and password.")
                return

        
            admin = Admin(username, password)
            if admin.login(self.db):  
                self.admin = admin  
                messagebox.showinfo("Login Successful", "Welcome to the Admin Panel!")
                self.create_main_menu()  
            else:
                messagebox.showerror("Login Failed", "Invalid username or password.")

        tk.Button(self.root, text="Login", command=login).pack(pady=10)

    
    
    
    
    
    def view_managers_window(self):
        self.clear_window()

        tk.Label(self.root, text="List of All Pharmacy Managers", font=("Arial", 16)).pack(pady=10)

        
        managers = self.admin.view_managers(self.db)

        
        columns = ("id", "username", "password")
        tree = ttk.Treeview(self.root, columns=columns, show="headings")
        tree.heading("id", text="ID")
        tree.heading("username", text="Username")
        tree.heading("password", text="Password")

        
        for manager in managers:
            tree.insert("", tk.END, values=manager)
        
        tree.pack(pady=10, fill=tk.BOTH, expand=True)
        tk.Button(self.root, text="Back", command=self.create_main_menu).pack()

    
    def view_medicines_window(self):
        self.clear_window()

        tk.Label(self.root, text="List of All Medicines", font=("Arial", 16)).pack(pady=10)

        
        medicines = self.admin.view_all_medicines(self.db)

        
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

if __name__ == "__main__":
    root = tk.Tk()
    app = AdminGUI(root)
    root.mainloop()
