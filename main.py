import tkinter as tk
import tkinter.font as font
from tkinter import simpledialog
from in_out import in_out
from RTD import rtd 
# import os
# import camera
# import model
from app import App
# from classifier import classifier
from motion import noise
from rect_noise import rect_noise
from record import record
from PIL import Image, ImageTk


window = tk.Toplevel()
window.title("Smart cctv")
window.iconphoto(False, ImageTk.PhotoImage(file='mn.png'))
window.geometry('1060x760')
window.minsize(900,700)
window.configure(bg='#577399')


frame1 = tk.Frame(window)
frame1.configure(bg='#577399')

# class Main:
#     def __init__(self):
#         frame1 = tk.frame(window)

label_title = tk.Label(frame1, text="Smart cctv Camera")
label_font = font.Font(size=35, weight='bold',family='Helvetica')
label_title['font'] = label_font
label_title.grid(pady=(10,10), column=2)


icon = Image.open('icons/spy.png')
icon = icon.resize((150,150), Image.ANTIALIAS)
icon = ImageTk.PhotoImage(icon)
label_icon = tk.Label(frame1, image=icon)
label_icon.grid(row=1, pady=(5,10), column=2)

btn1_image = Image.open('icons/incognito.png')
btn1_image = btn1_image.resize((50,50), Image.ANTIALIAS)
btn1_image = ImageTk.PhotoImage(btn1_image)

btn2_image = Image.open('icons/rectangle-of-cutted-line-geometrical-shape.png')
btn2_image = btn2_image.resize((50,50), Image.ANTIALIAS)
btn2_image = ImageTk.PhotoImage(btn2_image)

btn5_image = Image.open('icons/exit.png')
btn5_image = btn5_image.resize((50,50), Image.ANTIALIAS)
btn5_image = ImageTk.PhotoImage(btn5_image)

btn3_image = Image.open('icons/noise.png')
btn3_image = btn3_image.resize((50,50), Image.ANTIALIAS)
btn3_image = ImageTk.PhotoImage(btn3_image)

# add
btn7_image = Image.open('icons/1.png')
btn7_image = btn7_image.resize((50,50), Image.ANTIALIAS)
btn7_image = ImageTk.PhotoImage(btn7_image)

btn6_image = Image.open('icons/security-camera.png')
btn6_image = btn6_image.resize((50,50), Image.ANTIALIAS)
btn6_image = ImageTk.PhotoImage(btn6_image)

btn4_image = Image.open('icons/recording.png')
btn4_image = btn4_image.resize((50,50), Image.ANTIALIAS)
btn4_image = ImageTk.PhotoImage(btn4_image)

# --------------- Button -------------------#
btn_font = font.Font(size=25)
btn1 = tk.Button(frame1, text='Classifier', height=90, width=200, fg='green', bg="#f7f7ff", command=App, image=btn1_image, compound='left', borderwidth=3, relief="raised", padx=5, pady=10)
btn1['font'] = btn_font
# tk.Button(frame1, text="raised border", borderwidth=3, relief="raised", padx=5, pady=10).pack(padx=5, pady=10)
btn1.grid(row=3, pady=(20,10))

btn2 = tk.Button(frame1, text='Rectangle', height=90, width=200, fg='orange',bg="#f7f7ff", command=rect_noise, compound='left', image=btn2_image,  borderwidth=3, relief="raised", padx=5, pady=10)
btn2['font'] = btn_font
btn2.grid(row=3, pady=(20,10), column=3, padx=(20,5))

btn_font = font.Font(size=25)
btn3 = tk.Button(frame1, text='Noise', height=90, width=200, fg='green', bg="#f7f7ff", command=noise, image=btn3_image, compound='left',  borderwidth=3, relief="raised", padx=5, pady=10)
btn3['font'] = btn_font
btn3.grid(row=5,  pady=(20,10))

#add
btn_font = font.Font(size=25)
btn7 = tk.Button(frame1, text='RTD', height=90, width=200, fg='green', bg="#f7f7ff", command=rtd, image=btn7_image, compound='left',  borderwidth=3, relief="raised", padx=5, pady=10)
btn7['font'] = btn_font
btn7.grid(row=5, column=2, pady=(20,10))

btn4 = tk.Button(frame1, text='Record', height=90, width=200, fg='orange', bg="#f7f7ff", command=record, image=btn4_image, compound='left',  borderwidth=3, relief="raised", padx=5, pady=10)
btn4['font'] = btn_font
btn4.grid(row=5, pady=(20,10), column=3)


btn6 = tk.Button(frame1, text='In Out', height=90, width=200, fg='green', bg="#f7f7ff", command=in_out, image=btn6_image, compound='left',  borderwidth=3, relief="raised", padx=5, pady=10)
btn6['font'] = btn_font
# btn6.grid(row=4, pady=(20,10), column=2)
btn6.grid(row=3, pady=(20,10), column=2)

btn5 = tk.Button(frame1, height=90, width=200, fg='red', bg="#f7f7ff", command=window.quit, image=btn5_image,  borderwidth=3, relief="raised", padx=5, pady=10)
btn5['font'] = btn_font
btn5.grid(row=6, pady=(20,10), column=2)

frame1.pack()
window.mainloop()





