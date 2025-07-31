from tkinter import *
import requests
from PIL import Image, ImageTK
from io import BytesIO



window = Tk()
window.title('Dogz pics')
window.geometry('360x420')

label = Label()
label.pack(pady=10)

button = Button(text='DownloadIMG', command=show_image)
button.pack(pady=10)

window.mainloop()
