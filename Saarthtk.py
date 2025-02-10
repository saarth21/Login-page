import tkinter as tk
from tkinter import messagebox
def login():
	username = username_entry.get()
	password = password_entry.get()
	if username == "admin" and password == "password":
		messagebox.showinfo("Welcome back online admin", "Login successful")
	else:
		if(username != "admin" and password == "password"):
			messagebox.showinfo("Incorrect username", "Try agian, incorrect username")
		elif(username == "admin" and password != "password"):
			messagebox.showinfo("Incorrect password", "try agian, incorrect password")
		else:
			messagebox.showinfo("Incorrect username AND password", "try agian, both invaild")
	


#Create windows
windows = tk.Tk()
windows.title("Login page")
windows.geometry("400x300")


#Username/Password entry
username_label = tk.Label(windows,text="Username: ")
username_label.pack(pady=5)

username_entry = tk.Entry(windows)
username_entry.pack(pady=5)

#Password

password_label = tk.Label(windows,text="Password: ")
password_label.pack(pady=9)

password_entry = tk.Entry(windows)
password_entry.pack(pady=5)

login_button = tk.Button(windows, text= "login", command=login)
login_button.pack(pady=5)







windows.mainloop()
