#kitaphanalar
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image
from database.db import get_user_by_iin ,get_password_by_iin
import os
import sys


ctk.set_appearance_mode("light")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("Тестілеуші программа")
app.geometry("1040x700")

#Panel
header = ctk.CTkFrame(app, fg_color="#03287B", height=80, corner_radius=3)
header.pack(fill="x")

title = ctk.CTkLabel(
    header,
    text="ТЕСТІЛЕУШІ ПРОГРАММА",
    text_color="white",
    font=("Arial", 22, "bold"),
   
)
title.place(relx=0.5, rely=0.5, anchor="center")

logo_path = r"C:\Users\Asus\Desktop\Workspace\Nurait things\Python 3.13\py313\nur\projectbay\materials\zhlogo1.png"
logo_image = ctk.CTkImage(
    light_image=Image.open(logo_path),
    dark_image=Image.open(logo_path),
    size=(60, 60)
)
logo_label = ctk.CTkLabel(header, image=logo_image, text="")
logo_label.place(relx=0.93, rely=0.5, anchor="center")
#Panel end

card = ctk.CTkFrame(app, width=460, height=500, corner_radius=15, fg_color="#F2F2F2" , )
card.place(relx=0.50, rely=0.5, anchor="center")
card.pack_propagate(False)

tabs = ctk.CTkTabview(card, width=430, height=500, corner_radius=12, fg_color="#D8D8D8")
tabs.pack(pady=50)

def oralu():
    app.destroy()
    os.system('python "C:\\Users\\Asus\\Desktop\\Workspace\\Nurait things\\Python 3.13\\py313\\nur\\projectbay\\tirkelu.py"')

def passs():
    iin = jsn_k.get()
    kupia = get_password_by_iin(iin)
    if len(iin) == 12 :
        messagebox.showinfo("SOS",f"{iin} - жсн бойынша пароль:{kupia}")
    else:
        messagebox.showerror("Қате", "ЖСН базада жоқ немесе \n талаптарға сай жазылмады \n (Талап:ЖСН 12 саннан тұруы керек)")

login_tab = tabs.add("Құпиясөз")

jsc = ctk.CTkLabel(login_tab, text="Құпиясөзді базадан іздеу үшін \nБазаға тіркелу кезіндегі енгізген \nЖСН-ды енгізіңіз", text_color="black", font=("Arial", 14))
jsc.pack(pady=5)

jsn_k = ctk.CTkEntry(login_tab, placeholder_text="ЖСН", width=300, height=42,  corner_radius=7)
jsn_k.pack(pady=5)

login_btn = ctk.CTkButton(login_tab, text="Табу",command=passs, width=280, height=40, fg_color="#3366FF",font=("Arial", 14, "bold"),text_color="#F3F3F3",corner_radius=5 )
login_btn.pack(pady=7)

login_btn = ctk.CTkButton(login_tab, text="Оралу",command=oralu, width=280, height=40, fg_color="#3366FF",font=("Arial", 14, "bold"),text_color="#F3F3F3",corner_radius=5 )
login_btn.pack(pady=5)

footer3 = ctk.CTkLabel(login_tab, text="©1-топша", text_color="black", font=("Arial", 12, "underline"))
footer3.pack(pady=5)


#ortaga shygaratyn
def center():
    app.update_idletasks()
    w = app.winfo_width()
    h = app.winfo_height()
    sw = app.winfo_screenwidth()
    sh = app.winfo_screenheight()
    x = (sw - w) // 2
    y = (sh - h) // 2
    app.geometry(f"{w}x{h}+{x}+{y}")
app.after(10, center)
app.mainloop()
