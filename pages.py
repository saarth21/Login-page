import tkinter as tk
from PIL import Image, ImageTk

#Functions
def page1():
    page2_Label.pack_forget()
    page1_button.pack_forget()
    page1_Label.pack()
    page2_button.pack()
def page2():
    page1_Label.pack_forget()
    page2_button.pack_forget()
    page2_Label.pack()
    page1_button.pack()

window = tk.Tk()
window.geometry("300x400")
#Page 1
page1_Label=tk.Label(window, text="this is page 1")
image = Image

#Page 2
page2_Label=tk.Label(window, text="This is page 2")


#Buttons for both pages
page1_button=tk.Button(window, text="page 1", command=page1)
page1_button.pack(pady=14)



page2_button=tk.Button(window, text="page 2", command=page2)
page2_button.pack(pady=14)

page1_Label.pack(pady=6)




















window.mainloop()