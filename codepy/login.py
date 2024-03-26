import tkinter as tk
from database import connect_to_database

def login():
    username = entry_username.get()
    password = entry_password.get()
    
    try:

        db_connection = connect_to_database()
        
        cursor = db_connection.cursor()
        
        sql_query = "SELECT * FROM accounts WHERE username = %s AND password = %s"
        cursor.execute(sql_query, (username, password))
        
        result = cursor.fetchone()
        
        if result:
            login_status_label.config(text="Đăng nhập thành công")
        else:
            login_status_label.config(text="Đăng nhập thất bại")
        cursor.close()
        db_connection.close()
        
    except mysql.connector.Error as error:
        print("Lỗi khi thực hiện truy vấn SQL:", error)

def register():
    
    username = entry_username.get()
    password = entry_password.get()
    email = entry_email.get()
    
    try:
        db_connection = connect_to_database()
        
        cursor = db_connection.cursor()
        
        create_table_accounts(cursor)
        
        sql_query = "INSERT INTO accounts (username, password, email) VALUES (%s, %s, %s)"
        cursor.execute(sql_query, (username, password, email))
        
        db_connection.commit()
        
        cursor.close()
        db_connection.close()
        
        print("Đăng ký tài khoản thành công và lưu vào cơ sở dữ liệu")
        
    except mysql.connector.Error as error:
        print("Lỗi khi thực hiện truy vấn SQL:", error)

root = tk.Tk()
root.title("Đăng nhập")
root.geometry("500x500")


label_username = tk.Label(root, text="Username:", font=("Arial", 14))
label_username.pack()
entry_username = tk.Entry(root, font=("Arial", 12))
entry_username.pack()

label_password = tk.Label(root, text="Password:", font=("Arial", 14))
label_password.pack()
entry_password = tk.Entry(root, show="*", font=("Arial", 12))
entry_password.pack()

button_login = tk.Button(root, text="Đăng nhập", command=login, font=("Arial", 14))
button_login.pack()

button_register = tk.Button(root, text="Đăng ký", command=register, font=("Arial", 14))
button_register.pack()

login_status_label = tk.Label(root, text="", font=("Arial", 14))
login_status_label.pack()

root.mainloop()