# import sqlite3
# conn=sqlite3.connect("data.db")



# conn.execute( ''' 

# Create table student (
#              st_id INT PRIMARY KEY
#              st_name VARCHAR(30)
#              st_email VARCHAR(30) 
#                          )
             
# '''
# )

# conn.close()



# import sqlite3

# # Connect to SQLite (or create it if it doesn't exist)
# conn = sqlite3.connect('students.db')

# # Create a cursor object
# cursor = conn.cursor()

# # Create a table for student data
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS students (
#     student_id INTEGER PRIMARY KEY,
#     first_name TEXT NOT NULL,
#     last_name TEXT NOT NULL,
#     age INTEGER,
#     grade TEXT,
#     major TEXT
# )
# ''')

# # Insert sample data into the table
# sample_students = [
#     ('John', 'Doe', 20, 'Sophomore', 'Computer Science'),
#     ('Jane', 'Smith', 22, 'Senior', 'Biology'),
#     ('Mike', 'Brown', 19, 'Freshman', 'Physics'),
#     ('Emily', 'Davis', 21, 'Junior', 'Mathematics')
# ]

# # Use parameterized queries to insert data
# cursor.executemany('''
# INSERT INTO students (first_name, last_name, age, grade, major)
# VALUES (?, ?, ?, ?, ?)
# ''', sample_students)

# # Commit changes and close the connection
# conn.commit()
# print
# ("Sample data inserted successfully!")

# # Optionally, close the connection
# conn.close()









import sqlite3
import bcrypt

# Connect to the SQLite database (creates the file if it doesn't exist)
conn = sqlite3.connect('admin_credentials.db')
cursor = conn.cursor()

# Create a table for admin users if it doesn't already exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS admins (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
''')

# Insert an admin user (use a strong password)
username = 'het'
password = 'het'
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

try:
    cursor.execute('INSERT INTO admins (username, password) VALUES (?, ?)', (username, hashed_password))
    conn.commit()
    print("Admin user added successfully!")
except sqlite3.IntegrityError:
    print("Admin user already exists.")

conn.close()










# from flask import Flask, render_template, request, redirect, url_for, flash, session
# import sqlite3
# import bcrypt

# app = Flask(__name__)
# app.secret_key = 'your_secret_key'

# # Function to check login credentials
# def check_admin_credentials(username, password):
#     conn = sqlite3.connect('admin_credentials.db')
#     cursor = conn.cursor()

#     cursor.execute('SELECT password FROM admins WHERE username = ?', (username,))
#     result = cursor.fetchone()

#     conn.close()

#     if result:
#         stored_password = result[0]
#         if bcrypt.checkpw(password.encode('utf-8'), stored_password):
#             return True
#     return False

# # Route for the login form
# @app.route('/admin_login', methods=['GET', 'POST'])
# def admin_login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']

#         if check_admin_credentials(username, password):
#             session['admin_logged_in'] = True
#             flash('Login successful!', 'success')
#             return redirect(url_for('admin_dashboard'))
#         else:
#             flash('Invalid username or password.', 'danger')

#     return render_template('login.html')

# # Route for the admin dashboard (requires login)
# @app.route('/admin_dashboard')
# def admin_dashboard():
#     if 'admin_logged_in' in session:
#         return '<h1>Welcome to the Administrator Dashboard!</h1>'
#     else:
#         flash('You need to log in first.', 'warning')
#         return redirect(url_for('admin_login'))

# # Route to log out
# @app.route('/logout')
# def logout():
#     session.pop('admin_logged_in', None)
#     flash('You have been logged out.', 'info')
#     return redirect(url_for('admin_login'))

# if __name__ == '__main__':
#     app.run(debug=True)
