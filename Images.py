import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.geometry("600x800")

#Gallery app
image = Image.open("Image1.jpg") #Loading the image
image = image.resize((150,140))   #Resize the image
image = ImageTk.PhotoImage(image)	# Make into a photoimage object
gallery_image = tk.Label(window, image=image)	# Put image onto a label 
gallery_image.pack(pady=15,side="left")   # Pack the image

gallery_label = tk.Label(window, text= "Photo gallery")
gallery_label.pack(pady=5,side="left")

#Discord app
image1 = Image.open("discord.jpg")
image1 = image1.resize((150,140))
image1 = ImageTk.PhotoImage(image1)
discord_image = tk.Label(window,image=image1)
discord_image.pack(pady=15)

discord_label = tk.Label(window, text= "Discord")
discord_label.pack(pady=5)




















window.mainloop()