import pymysql

class DatabaseConnection:
    def __init__(self):

        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            password=""
        )
        self.cursor = self.connection.cursor()
        
    def create_database(self):
        
        try:
            self.cursor.execute("CREATE DATABASE IF NOT EXISTS pharmacy_db")
            print("Database 'pharmacy_db' created or already exists.")
            self.cursor.execute("USE pharmacy_db")
        except pymysql.MySQLError as e:
            print("Error creating database:", e)
    
    def create_tables(self):
        
        medicine_table = """
        CREATE TABLE IF NOT EXISTS medicine (
            sr_no INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            quantity INT NOT NULL,
            added_date DATE NOT NULL,
            added_by VARCHAR(255) NOT NULL,
            price DECIMAL(10, 2) NOT NULL
        )
        """
        
        admin_table = """
        CREATE TABLE IF NOT EXISTS admins (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL
        )
        """
        
        pharmacy_manager_table = """
        CREATE TABLE IF NOT EXISTS managers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL
        )
        """
        

        try:
            self.cursor.execute(medicine_table)
            print("Table 'medicine' created or already exists.")
            
            self.cursor.execute(admin_table)
            print("Table 'admin' created or already exists.")
            
            self.cursor.execute(pharmacy_manager_table)
            print("Table 'pharmacy_manager' created or already exists.")
            

            self.connection.commit()
        except pymysql.MySQLError as e:
            print("Error creating tables:", e)
            self.connection.rollback()
    
    def close_connection(self):

        self.cursor.close()
        self.connection.close()


    def execute_query(self, query, values=None):
        """
        Executes a query and commits the transaction.
        """
        self.connection.select_db("pharmacy_db")
        try:
            self.cursor.execute(query, values)
            self.connection.commit()
            return self.cursor.fetchall()
        except pymysql.MySQLError as e:
            print("Database error:", e)
            self.connection.rollback()
            return None


if __name__ == "__main__":
    db_setup = DatabaseConnection()
    
    
    db_setup.create_database()
    
    
    db_setup.create_tables()
    
    
    db_setup.close_connection()
    print("Database setup completed successfully.")
