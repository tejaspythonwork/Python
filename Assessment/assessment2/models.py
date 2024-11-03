
from db_connection import DatabaseConnection
from datetime import datetime

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    # def register(self):
    #     pass

    # def login(self):
    #     pass

class PharmacyManager(User):
    def register(self, db):
        query = "INSERT INTO managers (username, password) VALUES (%s, %s)"
        db.execute_query(query, (self.username, self.password))

    def add_medicine(self, db, name, quantity, price):
        query = """INSERT INTO medicine (name, quantity, added_date, added_by, price)
                   VALUES (%s, %s, %s, %s, %s)"""
        date_added = datetime.now().strftime('%Y-%m-%d')
        db.execute_query(query, (name, quantity, date_added, self.username, price))

    def view_medicine(self, db):
        query = "SELECT * FROM medicine WHERE added_by = %s"
        return db.execute_query(query, (self.username,))

    def delete_medicine(self, db, sr_no):
        query = "DELETE FROM medicine WHERE sr_no = %s AND added_by = %s"
        db.execute_query(query, (sr_no, self.username))

    def login(self, db):
        query = "SELECT * FROM managers WHERE username = %s AND password = %s"
        result = db.execute_query(query, (self.username, self.password))
        return result is not None and len(result) > 0


class Admin(User):
    def register(self, db):
        query = "INSERT INTO admins (username, password) VALUES (%s, %s)"
        db.execute_query(query, (self.username, self.password))

    def view_managers(self, db):
        query = "SELECT * FROM managers"
        return db.execute_query(query)

    def view_all_medicines(self, db):
        query = "SELECT * FROM medicine"
        return db.execute_query(query)

    def login(self, db):
        query = "SELECT * FROM admins WHERE username = %s AND password = %s"
        result = db.execute_query(query, (self.username, self.password))
        return result is not None and len(result) > 0
