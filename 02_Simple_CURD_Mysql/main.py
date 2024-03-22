import mysql.connector
from color import colors,fg,bg

class UserManagement:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host = "127.0.0.1",
                user = "root",
                password = "",
                database = "curd"
            )
            self.cursor = self.conn.cursor()
            print(fg.green+"\n\tConnected to MySQL database successfully..."+colors.reset)
        except mysql.connector.Error as err:
            print(fg.red+f"Error: {err}"+colors.reset)
            exit(1)
    
    def create_user(self,name,email):
        try:
            self.cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
            self.conn.commit()
            print(fg.green+"User created successfully!"+colors.reset)
        except mysql.connector.Error as err:
            print(fg.red+f"Error: {err}"+colors.reset)

        
    def read_users(self):
        try:
            self.cursor.execute("SELECT * FROM users")
            users = self.cursor.fetchall()
            for user in users:
                print(user)
        except mysql.connector.Error as err:
            print(fg.red+f"Error: {err}"+colors.reset)
            
    def update_user(self,user_id,new_name,new_email): # using placeholder %s to prevent sql injection
        try:
            self.cursor.execute("UPDATE users SET name=%s, email=%s WHERE id=%s", (new_name, new_email, user_id))
            self.conn.commit()
            print(fg.green+"User updated successfully!"+colors.reset)
        except mysql.connector.Error as err:
            print(fg.red+f"Error: {err}"+colors.reset)
            
    def delete_user(self, user_id):
        try:
            self.cursor.execute("DELETE FROM users WHERE id=%s", (user_id,))
            self.conn.commit()
            print(fg.green+"User deleted successfully!"+colors.reset)
        except mysql.connector.Error as err:
            print(fg.red+f"Error: {err}"+colors.reset)
            
    def close_connection(self):
        try:
            self.cursor.close()
            self.conn.close()
            print(fg.green+"\n\t\tConnection closed successfully!\n"+colors.reset)
        except mysql.connector.Error as err:
            print(fg.red+f"Error: {err}"+colors.reset)

# Main function 
def main():

    user_management = UserManagement()

    while True:
        print(fg.cyan+"\n\t\t\t\tMenu"+colors.reset)
        print(fg.purple+"\t\t\t1. Create User")
        print("\t\t\t2. Read Users")
        print("\t\t\t3. Update User")
        print("\t\t\t4. Delete User")
        print("\t\t\t5. Exit\n"+colors.reset)
        
        choice = input(fg.yellow+"Enter your choice: "+colors.reset)
        
        if choice == '1':
            name = input(fg.blue+"Enter user's name: "+colors.reset)
            email = input(fg.blue+"Enter user's email: "+colors.reset)
            user_management.create_user(name,email)
        elif choice == '2':
            user_management.read_users()
        elif choice == '3':
            user_id = int(input(fg.blue+"Enter user ID to update: "+colors.reset))
            new_name = input(fg.blue+"Enter new name: "+colors.reset)
            new_email = input(fg.blue+"Enter new email: "+colors.reset)
            user_management.update_user(user_id,new_name,new_email)
        elif choice == '4':
            user_id = int(input(fg.blue+"Enter user ID to delete: "+colors.reset))
            user_management.delete_user(user_id)
        elif choice == '5':
            user_management.close_connection()
            break
        else:
            print(fg.red+"Invalid choice! Please try again."+colors.reset)

if __name__ == "__main__":
    main()
