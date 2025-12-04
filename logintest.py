#kitaphanalar
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image
from database.db import get_user_by_iin 
import os
import sys

# PDF файлын ашу функциясы
def open_pdf(path):
    if sys.platform.startswith("win"):     
        os.startfile(path)

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("Тестілеуші программа")
app.geometry("1040x700")

#Argumennti alu
aty2 = sys.argv[1]
jssn = sys.argv[2]
parol2 = sys.argv[3]
data = sys.argv[4]



#PANEL
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
#PANEL END



#NEGIZGI
card = ctk.CTkFrame(app, width=460, height=500, corner_radius=15, fg_color="#F2F2F2" , )
card.place(relx=0.50, rely=0.5, anchor="center")
card.pack_propagate(False)

tabs = ctk.CTkTabview(card, width=430, height=500, corner_radius=12, fg_color="#D8D8D8")
tabs.pack(pady=50)

login_tab = tabs.add("Кіру")

jsc = ctk.CTkLabel(login_tab, text="Тестке кіру үшін пәнді таңдаңыз \nжәне құпиясөз енгізіңіз", text_color="black", font=("Arial", 14))
jsc.pack(pady=5)

selected_subject = ""

def subject_changed(value):
    global selected_subject
    selected_subject = value  # пән таңдалды 

pan = ctk.CTkOptionMenu(
    login_tab, 
    values=["","Тарих","Информатика","Математика"],
    command=subject_changed ,
    width=300 , 
    height=35)
pan.pack(pady=10)

login_pass = ctk.CTkEntry(login_tab, placeholder_text="Құпиясөз", width=300, height=42, show="*" , corner_radius=7)
login_pass.pack(pady=5)

#TESTKE KIRU
def check():
    user1 = login_pass.get().strip()
    if selected_subject and user1 != "" :      
        if user1 == "" or len(user1) !=4:
            messagebox.showwarning("Error","Құпия сөз 4 саннан тұруы керек")  
        elif len(user1) == 4:
            if user1 != parol2:
                messagebox.showerror("Қате", "Құпия сөз дұрыс емес.")
            else:
                messagebox.showinfo("Қош келдіңіз", f"Сәттілік {aty2} !")
                app.destroy()
                os.system(f'python "C:\\Users\\Asus\\Desktop\\Workspace\\Nurait things\\Python 3.13\\py313\\nur\\projectbay\\test_question.py" {aty2} {selected_subject} {parol2} {jssn} {data}')

    else:
        messagebox.showerror("Қате", "Барлық өрістерді толтырыңыз.")


login_btn = ctk.CTkButton(login_tab, text="Кіру", width=280,command=check, height=40, fg_color="#3366FF",font=("Arial", 14, "bold"),text_color="#F3F3F3",corner_radius=5 )
login_btn.pack(pady=15)

def paol():
    app.destroy()
    os.system("C:\\Users\\Asus\\Desktop\\Workspace\\Nurait things\\Python 3.13\\py313\\nur\\projectbay\\findpass.py")

footer7 = ctk.CTkButton(
    login_tab, 
    text="Құпия сөзді ұмыттыңыз ба?",
    fg_color="transparent",
    text_color="gray", font=("Arial", 12, "underline"),
    hover_color="#D0D0FF",
    command=paol
    
)
footer7.pack(pady=5)

footer1 = ctk.CTkButton(
    login_tab, 
    text="Тестке кіру нұсқаулығы",
    fg_color="transparent",
    text_color="gray", font=("Arial", 12, "underline"),
    hover_color="#D0D0FF",
    command=lambda: open_pdf(r"C:\Users\Asus\Desktop\Workspace\Nurait things\Python 3.13\py313\nur\projectbay\materials\testkekiru.pdf") 
)
footer1.pack(pady=5)


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
