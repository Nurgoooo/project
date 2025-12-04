#kitaphanalar
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image
from datetime import datetime
import os
import sys

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Тестілеуші программа")
app.geometry("1040x700")
app.resizable(False, False)

#Argumennti alu
aty2 = sys.argv[1]
jssn = sys.argv[2]
parol2 = sys.argv[3]


#Panel
header = ctk.CTkFrame(app, fg_color="#03287B", height=75, corner_radius=3)
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

#MENU
def profil_otu():
    app.destroy()
    os.system(f'python "C:\\Users\\Asus\\Desktop\\Workspace\\Nurait things\\Python 3.13\\py313\\nur\\projectbay\\profil.py" {aty2} {jssn} {parol2}')

def daindk_otu():
    app.destroy()
    os.system(f'python "C:\\Users\\Asus\\Desktop\\Workspace\\Nurait things\\Python 3.13\\py313\\nur\\projectbay\\daindk.py" {aty2} {jssn} {parol2}')

def tapsyrgan_otu():
    app.destroy()
    os.system(f'python "C:\\Users\\Asus\\Desktop\\Workspace\\Nurait things\\Python 3.13\\py313\\nur\\projectbay\\tapsyr.py" {aty2} {jssn} {parol2}')

def shigu_lg():
    app.destroy()
    os.system('python "C:\\Users\\Asus\\Desktop\\Workspace\\Nurait things\\Python 3.13\\py313\\nur\\projectbay\\tirkelu.py"')
#MENU end

# Сол жақ панель
left_panel = ctk.CTkFrame(app, width=250, fg_color="#D9D9D9")
left_panel.pack(side="left", fill="y")

ctk.CTkButton(left_panel, text="Профиль",command=profil_otu, width=180, height=30,
                  fg_color="white", text_color="black").pack(pady=5, padx=30)

ctk.CTkButton(left_panel, text="Өтініш беру", width=180, height=30,
                  fg_color="white", text_color="black").pack(pady=5, padx=30)

ctk.CTkButton(left_panel, text="Тапсырғандарым",command=tapsyrgan_otu, width=180, height=30,
                  fg_color="white", text_color="black").pack(pady=5, padx=30)

ctk.CTkButton(left_panel, text="Дайындық", width=180, height=30,command=daindk_otu,
                  fg_color="white", text_color="black").pack(pady=5, padx=30)

ctk.CTkButton(left_panel, text="Шығу",command=shigu_lg, width=180, height=30,
                  fg_color="white", text_color="black").pack(pady=5, padx=30)

ctk.CTkButton(left_panel, text="Көмек", width=180, height=30,
              fg_color="white", text_color="black").pack(side="bottom", pady=20)



# Негізгі контент аймағы
content = ctk.CTkFrame(app, fg_color="#F2F2F2", width=790, height=620)
content.place(x=250, y=80)

#Сұр форма
form = ctk.CTkFrame(content, fg_color="#E5E5E5",
                    width=800, height=600, corner_radius=10)
form.place(x=10, y=10)
ctk.CTkLabel(form, text="өтініш беру", font=("Arial", 14)).place(x=20, y=10)

# Цитата
quote = ctk.CTkFrame(content, fg_color="white", corner_radius=10,
                     width=750, height=110)
quote.place(x=20, y=50)

quote_text = (
    "«Қай істің болмасын өнуіне үш шарт бар: ең әуелі – ниет керек,\n"
    "одан соң – күш керек, одан соң – тәртіп керек.»"
)
ctk.CTkLabel(quote, text=quote_text, font=("Arial", 15),
             text_color="black").place(x=60, y=25)

ctk.CTkLabel(quote, text="Абай Құнанбайұлы",
             font=("Arial", 12), text_color="black").place(x=500, y=70)

#Көк сызық 
line = ctk.CTkFrame(content, fg_color="#4C90FF", width=750, height=2)
line.place(x=20, y=170)

#ӨТІНІШ БЕРУ
blue_box = ctk.CTkFrame(content, fg_color="#77B9E8",
                        width=750, height=65, corner_radius=10)
blue_box.place(x=20, y=190)

ctk.CTkLabel(blue_box, text="ӨТІНІШ БЕРУ",
             font=("Arial", 22, "bold"), text_color="black").place(x=280, y=18)

#Сұр форма
form = ctk.CTkFrame(content, fg_color="#E9E9E9",
                    width=750, height=300, corner_radius=10)
form.place(x=20, y=270)

info_text = (
    "Берілгенді мұқият, ұқыпты толтыруыңыз сұралады\n\n"
    "Әзірше тест тапсыру мүмкіндігі Ақтөбе қаласында ғана бар\n\n"
    "Тапсыру күнін мұқият толтырыңыз, себебі “Тапсырғандарым”\n"
    "бөліміне толтырған күніңіз жазылады"
)
ctk.CTkLabel(form, text=info_text, font=("Arial", 13),
             justify="left").place(x=30, y=50)

#Енгізу өрістері
city = ctk.CTkOptionMenu(form, values=["Ақтөбе"], width=250)
city.place(x=470, y=40)

name_entry = ctk.CTkLabel(form, text=f"Аты жөні: {aty2}", font=("Arial", 12) , width=250 , height=30,corner_radius=10,
              justify = "left",  fg_color="white", text_color="black")
name_entry.place(x=470, y=90)

def check_date():
    date_text = date_entry.get()
    try:
        datetime.strptime(date_text, "%d.%m.%Y")
        messagebox.showinfo("Дұрыс","Формат дұрыс ✔" )
        app.destroy()
        os.system(f'python "C:\\Users\\Asus\\Desktop\\Workspace\\Nurait things\\Python 3.13\\py313\\nur\\projectbay\\logintest.py" {aty2} {jssn} {parol2} {date_text}')
    except:
        messagebox.showerror("Error","Формат қате! ДД.ММ.ГГГГ")

date_entry = ctk.CTkEntry(form, placeholder_text="тапсыру күні (ДД.ММ.ГГГГ)", width=250)
date_entry.place(x=470, y=140)

submit = ctk.CTkButton(form, text="Өтініш жіберу",command=check_date,
                       fg_color="#3F5DD9", text_color="white",
                       width=220, height=35)
submit.place(x=270, y=230)



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
#ЗАпуск программы
app.mainloop()
