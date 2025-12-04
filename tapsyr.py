#kitaphanalar
from database.db2 import get_user_by_iin
import customtkinter as ctk
from PIL import Image
import os
import sys

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Тестілеуші программа")
app.geometry("1040x700")
app.resizable(False, False)

# Аргументтерді алу
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
#Panel end


#MENU
def profil_otu():
    app.destroy()
    os.system(f'python "C:\\Users\\Asus\\Desktop\\Workspace\\Nurait things\\Python 3.13\\py313\\nur\\projectbay\\profil.py" {aty2} {jssn} {parol2}')

def otinish_beru_otu():
    app.destroy()
    os.system(f'python "C:\\Users\\Asus\\Desktop\\Workspace\\Nurait things\\Python 3.13\\py313\\nur\\projectbay\\otinishberu.py" {aty2} {jssn} {parol2}')


def daindk_otu():
    app.destroy()
    os.system(f'python "C:\\Users\\Asus\\Desktop\\Workspace\\Nurait things\\Python 3.13\\py313\\nur\\projectbay\\daindk.py" {aty2} {jssn} {parol2}')

def shigu_lg():
    app.destroy()
    os.system('python "C:\\Users\\Asus\\Desktop\\Workspace\\Nurait things\\Python 3.13\\py313\\nur\\projectbay\\tirkelu.py"')
#MENU end


# Сол жақ панель
left_panel = ctk.CTkFrame(app, width=250, fg_color="#D9D9D9")
left_panel.pack(side="left", fill="y")

ctk.CTkButton(left_panel, text="Профиль",command=profil_otu, width=180, height=30,
                  fg_color="white", text_color="black").pack(pady=5, padx=30)

ctk.CTkButton(left_panel, text="Өтініш беру",command=otinish_beru_otu, width=180, height=30,
                  fg_color="white", text_color="black").pack(pady=5, padx=30)

ctk.CTkButton(left_panel, text="Тапсырғандарым", width=180, height=30,
                  fg_color="white", text_color="black").pack(pady=5, padx=30)

ctk.CTkButton(left_panel, text="Дайындық",command=daindk_otu, width=180, height=30,
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

ctk.CTkLabel(form, text="тапсырғандарым", font=("Arial", 14)).place(x=20, y=10)

#ӨТІНІШ БЕРУ көк тақтасы
blue_box = ctk.CTkFrame(content, fg_color="#77B9E8",
                        width=750, height=65, corner_radius=10)
blue_box.place(x=20, y=55)

#Көк сызық
line = ctk.CTkFrame(content, fg_color="#4C90FF", width=750, height=3)
line.place(x=20, y=130)

ctk.CTkButton(blue_box, text="ТАПСЫРҒАНДАРЫМ",bg_color="#77B9E8",fg_color="#77B9E8",
             font=("Arial", 22, "bold"), text_color="black").place(x=280, y=18)


def create_block(parent, text, y):
    h = ctk.CTkFrame(parent,fg_color="#FFFFFF",width=750,height=40,corner_radius=3)
    h.place(x=20, y=y)

    lbl = ctk.CTkLabel(h,text=text,font=("Arial", 16),text_color="black")
    lbl.place(x=10, y=5)


results = get_user_by_iin(jssn)
for index, r in enumerate(results):
    name, iin, score, time, wrong = r

    text = f" {name}                Балл: {score}            Қателер: {wrong}              Тапсырған күні: {time}"

    create_block(content, text, 140 + index * 50)




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
