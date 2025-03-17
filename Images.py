import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.geometry("600x800")

#Display Image
image = Image.open("Image1.jpg") #Loading the image
image =image.resize((250,228))   #Resize the image
image = ImageTk.PhotoImage(image)	# Make into a photoimage object
image_label = tk.Label(window, image=image)	# Put image onto a label 
image_label.pack(pady=15)   # Pack the image



























window.mainloop()