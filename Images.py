import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.geometry("600x800")

#Display Image
image = Image.open("Image1.jpg")
image =image.resize((250,228))
image = ImageTk.PhotoImage(image)
image_label = tk.Label(window, image=image)
image_label.pack(pady=15)



























window.mainloop()