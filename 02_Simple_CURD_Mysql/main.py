import mysql.connector
from color import colors,fg,bg

class UserManagement:
    def __init__(self,host,user,password,database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conn = self.connect()
        self.cursor = self.conn.cursor()
        
    def connect(self):
        return mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database
        )
    
    def create_user(self,name,email):
        self.cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
        self.conn.commit()
        print("User created successfully!")
        
    def read_users(self):
        self.cursor.execute("SELECT * FROM users")
        users = self.cursor.fetchall()
        for user in users:
            print(user)
            
    def update_user(self,user_id,new_name,new_email): # using placeholder %s to prevent sql injection
        self.cursor.execute("UPDATE users SET name=%s, email=%s WHERE id=%s", (new_name, new_email, user_id))
        self.conn.commit()
        print("User updated successfully!")
        
    def delete_user(self, user_id):
        self.cursor.execute("DELETE FROM users WHERE id=%s", (user_id,))
        self.conn.commit()
        print("User deleted successfully!")
        
    def close_connection(self):
        self.cursor.close()
        self.conn.close()
        
        
def main():
    host = "127.0.0.1"
    user = "root"
    password = ""
    database = "curd"
    
    user_management = UserManagement(host, user, password, database)
    
    while True:
        print("\n1. Create User")
        print("2. Read Users")
        print("3. Update User")
        print("4. Delete User")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter user's name: ")
            email = input("Enter user's email: ")
            user_management.create_user(name,email)
        elif choice == '2':
            user_management.read_users()
        elif choice == '3':
            user_id = int(input("Enter user ID to update: "))
            new_name = input("Enter new name: ")
            new_email = input("Enter new email: ")
            user_management.update_user(user_id,new_name,new_email)
        elif choice == '4':
            user_id = int(input("Enter user ID to delete: "))
            user_management.delete_user(user_id)
        elif choice == '5':
            user_management.close_connection()
            break
        else:
            print("Invalud choice! Please try again.")

if __name__ == "__main__":
    main()
