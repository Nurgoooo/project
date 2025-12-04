#kitaphanalar
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image
from database.db import add_user, get_user_by_iin 
import os
import sys
import secrets
import string



ctk.set_appearance_mode("light")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("Тестілеуші программа")
app.geometry("1040x700")


# PDF файлын ашу функциясы
def open_pdf(path):
   os.startfile(path)


# Құпия сөз жасау функциясы
def create_pw(pw_length=4):
    digits = string.digits
    alpha = digits
    pwd = ''
    pw_strong = False

    while not pw_strong:
        pwd =''
        for i in range(pw_length):
            pwd += ''.join(secrets.choice(alpha))

        pw_strong = True
    return pwd


#KYPUASOZ TABU
def kupiasoz_find():
     app.destroy()
     os.system(f'python "C:\\Users\\Asus\\Desktop\\Workspace\\Nurait things\\Python 3.13\\py313\\nur\\projectbay\\findpass.py"')
     
    
# Кіру функциясы
def kiru():
    jsn = login_jsc.get().strip()
    parol = login_pass.get().strip()
    if jsn and parol != "":    
        if len(jsn) == 12 and len(parol) == 4:
            user = get_user_by_iin(jsn)
            if user is None:
                messagebox.showerror("Қате", "Мұндай ЖСН тіркелмеген.")
            elif user[2] != parol:
                messagebox.showerror("Қате", "Құпия сөз дұрыс емес.")
            else:
                aty2 = get_user_by_iin(jsn)[0]
                messagebox.showinfo("Қош келдіңіз", f"Сіз сәтті кірдіңіз {aty2} !")
                app.destroy()
                os.system(f'python "C:\\Users\\Asus\\Desktop\\Workspace\\Nurait things\\Python 3.13\\py313\\nur\\projectbay\\profil.py" {aty2} {jsn} {parol}')

        elif len(jsn) < 12 or len(jsn) > 12 and len(parol) !=4:
                  messagebox.showerror("Қате", "ЖСН 12 саннан тұруы керек және құпия сөз 4 саннан тұруы керек.")
        elif len(parol) !=4 and len(jsn) == 12:
            messagebox.showerror("Қате", "Құпия сөз 4 саннан тұруы керек.")        
        
    else:
        messagebox.showerror("Қате", "Барлық өрістерді толтырыңыз.")

# Тіркелу функциясы
def tirkelu():
        jsn = reg_jsc.get().strip()
        aty = reg_aty.get().strip()
        parol1 = create_pw()
        if jsn and aty != "":
            if len(jsn) == 12:
                  add_user(aty, jsn, parol1)
                  messagebox.showinfo("Тіркелу сәтті өтті", f"Базаға сәтті тіркелдіңіз! \n\n  ЖСН:{reg_jsc.get()} \n   Аты-жөні:{reg_aty.get()}\n   Сіздің құпия сөзіңіз: {parol1} \n\nПарольді есте сақтаңыз!")
            elif len(jsn) < 12 or len(jsn) > 12:
                  messagebox.showerror("Қате", "ЖСН 12 саннан тұруы керек.")
        else:
            messagebox.showerror("Қате", "Барлық өрістерді толтырыңыз.")


#Панель
header = ctk.CTkFrame(app, fg_color="#001882", height=80, corner_radius=3)
header.pack(fill="x")

title = ctk.CTkLabel(
    header,
    text="Testtileushi programma",
    text_color="white",
    font=("Lato Bold", 24, "bold"),
   
)
title.place(relx=0.5, rely=0.5, anchor="center")

logo_path = r"C:\Users\Asus\Desktop\Workspace\Nurait things\Python 3.13\py313\nur\projectbay\materials\xx.png"
logo_image = ctk.CTkImage(
    light_image=Image.open(logo_path),
    dark_image=Image.open(logo_path),
    size=(60, 60)
)
logo_label = ctk.CTkLabel(header, image=logo_image, text="")
logo_label.place(relx=0.93, rely=0.5, anchor="center")
#Panek end



card = ctk.CTkFrame(app, width=460, height=500, corner_radius=15, fg_color="#F2F2F2" , )
card.place(relx=0.27, rely=0.5, anchor="center")
card.pack_propagate(False)

tabs = ctk.CTkTabview(card, width=430, height=500, corner_radius=12, fg_color="#F3F3F3")
tabs.pack(pady=50)

#PHOTO
lr_path = r"C:\Users\Asus\Desktop\Workspace\Nurait things\Python 3.13\py313\nur\projectbay\materials\loginph.png"
lr_image = ctk.CTkImage(
    light_image=Image.open(lr_path),
    dark_image=Image.open(lr_path),
    size=(520, 520)
)
lr_label = ctk.CTkLabel(app, image=lr_image, text="")
lr_label.place(relx=0.75, rely=0.50, anchor="center")

#Log in\Sign up
login_tab = tabs.add("Кіру")
register_tab = tabs.add("Тіркелу")

jsc = ctk.CTkLabel(login_tab, text="Кіру үшін ЖСН мен құпиясөзді \nенгізіңіз", text_color="black", font=("Arial", 14))
jsc.pack(pady=5)

login_jsc = ctk.CTkEntry(login_tab, placeholder_text="ЖСН", width=300, height=42, corner_radius=7)
login_jsc.pack(pady=10)

login_pass = ctk.CTkEntry(login_tab, placeholder_text="Құпиясөз", width=300, height=42, show="*" , corner_radius=7)
login_pass.pack(pady=5)

login_btn = ctk.CTkButton(login_tab, text="Кіру",command=kiru, width=300, height=40, fg_color="#3366FF",font=("Arial", 14, "bold"),text_color="#F3F3F3",corner_radius=5 ,border_color="#FFFFFF", border_width=2)
login_btn.pack(pady=15)

#KIRU zattary
footer7 = ctk.CTkButton(
    login_tab, 
    text="Құпия сөзді ұмыттыңыз ба?",
    command=kupiasoz_find,
    fg_color="transparent",
    text_color="gray", font=("Arial", 12, "underline"),
    hover_color="#D0D0FF",
    
)
footer7.pack(pady=5)

footer1 = ctk.CTkButton(
    login_tab, 
    text="Кіру/тіркелу нұсқаулығы",
    fg_color="transparent",
    text_color="gray", font=("Arial", 12, "underline"),
    hover_color="#D0D0FF",
    command=lambda: open_pdf(r"C:\Users\Asus\Desktop\Workspace\Nurait things\Python 3.13\py313\nur\projectbay\materials\kirutirkelu.pdf") 
)
footer1.pack(pady=5)

footer3 = ctk.CTkLabel(login_tab, text="©1-топша", text_color="black", font=("Arial", 12, "underline"))
footer3.pack(pady=5)

#Tirkelu zattary
jsc1 = ctk.CTkLabel(register_tab, text="Тіркелу үшін ЖСН мен Аты-жөніңізді \nенгізіңіз", text_color="black", font=("Arial", 14))
jsc1.pack(pady=5)

reg_jsc = ctk.CTkEntry(register_tab, placeholder_text="ЖСН", width=300, height=42)
reg_jsc.pack(pady=10)

reg_aty = ctk.CTkEntry(register_tab, placeholder_text="Аты-жөні", width=300, height=42)
reg_aty.pack(pady=5)

reg_btn = ctk.CTkButton(register_tab, text="Тіркелу",command=tirkelu, width=300, height=40, fg_color="#3366FF",font=("Arial", 14, "bold"),text_color="#F3F3F3",corner_radius=5 ,border_color="#FFFFFF", border_width=2)
reg_btn.pack(pady=15)

footer2 = ctk.CTkButton(
    register_tab, 
    text="Кіру/тіркелу нұсқаулығы",
    fg_color="transparent",
    text_color="gray", font=("Arial", 12, "underline"),
    hover_color="#D0D0FF",
    command=lambda: open_pdf(r"C:\Users\Asus\Desktop\Workspace\Nurait things\Python 3.13\py313\nur\projectbay\materials\kirutirkelu.pdf") 
)
footer2.pack(pady=5)

footer4 = ctk.CTkLabel(register_tab, text="©1-топша", text_color="black", font=("Arial", 12, "underline"))
footer4.pack(pady=5)

# ---------- Центрирование окна ----------
def center_window(width, height):
    app.geometry(f"{width}x{height}")
    app.update_idletasks()
    sw = app.winfo_screenwidth()
    sh = app.winfo_screenheight()
    x = (sw - width) // 2
    y = (sh - height) // 2
    app.geometry(f"{width}x{height}+{x}+{y}")

# ---------- Старт ----------
center_window(1040, 700)

app.mainloop()
