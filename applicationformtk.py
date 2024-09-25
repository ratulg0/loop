import tkinter as tk
from tkinter import *
a = tk.Tk()

a.title('pack method')
a.geometry('300x200')

name = tk.StringVar()
phone = tk.StringVar()
email = tk.StringVar()
city = tk.StringVar()
course = tk.StringVar()

Name = Label(a, text= 'Name').place(x=30, y=10)
e1= Entry(a, textvariable=name).place(x=100, y=10)

Phone = Label(a, text='Phone').place(x=30, y=40)
e2= Entry(a, textvariable= phone).place(x=100, y=40)

Email = Label(a, text='Email').place(x=30, y=70)
e3= Entry(a, textvariable=email).place(x=100, y=70)

City = Label(a, text='City').place(x=30, y=100)
e4= Entry(a, textvariable=city).place(x=100, y=100)

Course = Label(a, text='Course').place(x=30, y=130)
e5= Entry(a, textvariable=course).place(x=100, y=130)

def submit():
    print(f"Name: {name.get()}")
    print(f"Phone Number: {phone.get()}")
    print(f"Email: {email.get()}")
    print(f"City: {city.get()}")
    print(f"Applied Course: {course.get()}")

b= Button(a, text='Submit', command = submit).place(x=100, y=160)

a.mainloop()


import tkinter as tk
from tkinter import messagebox

# Function to validate the login
def validate_login():
   user_id = uname_e.get()
   password = pword_e.get()

   # You can add your own validation logic here
   if user_id == "darkfire" and password == "asd":
      messagebox.showinfo("Login Successful", "Welcome, Admin!")
      print(user_id, password)
   else:
      messagebox.showerror("Login Failed", "Invalid username or password")

# Create the main window
a = tk.Tk()
a.title("Login Form")
a.geometry('200x200')
# Create and place the username label and entry
uname_l = tk.Label(a, text="User id:")
uname_l.pack()
uname_e = tk.Entry(a)
uname_e.pack()
# Create and place the password label and entry
pword_l = tk.Label(a, text="Password:")
pword_l.pack()
pword_e = tk.Entry(a, show="*")  # Show asterisks for password
pword_e.pack()
# Create and place the login button
login_b = tk.Button(a, text="Login", command=validate_login)
login_b.pack()
# Start the Tkinter event loop
a.mainloop()

