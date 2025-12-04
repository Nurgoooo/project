import customtkinter as ctk
from datetime import datetime
from PIL import Image
import sys
import os

aty2 = sys.argv[1]
score = int(sys.argv[2])
data = sys.argv[3]
wrong_count = int(sys.argv[4])
time_str = sys.argv[5]


BG_MAIN   = "#f4f6fb"
BG_HEADER = "#3f5efb"
BG_CARD   = "#f0f2f7"
BTN_COLOR = "#3f5efb"
FONT_MAIN = ("Arial", 14)
FONT_BIG  = ("Arial", 28, "bold")

# =========================== MAIN WINDOW =======================
root = ctk.CTk()
root.title("Тест нәтижесі")
root.geometry("1040x700")
root.configure(fg_color=BG_MAIN)

# =========================== HEADER ===========================
#Panel
header = ctk.CTkFrame(root, fg_color="#03287B", height=75, corner_radius=3)
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
#Panek end

# ======================= MAIN CONTAINER ========================
container = ctk.CTkFrame(root, fg_color=BG_MAIN, corner_radius=0)
container.pack(fill="both", expand=True, padx=20, pady=(0,20))

# ======================= TOP SECTION ===========================
top_frame = ctk.CTkFrame(container, fg_color="white", corner_radius=12)
top_frame.pack(pady=10, fill="x", padx=10)
top_frame.grid_columnconfigure(0, weight=1)
top_frame.grid_columnconfigure(1, weight=0)

# Аты жөні
name_label = ctk.CTkLabel(top_frame, text="Аты жөні", text_color="#333", font=FONT_MAIN, fg_color="transparent")
name_label.grid(row=0, column=0, sticky="w", padx=20, pady=(18, 0))

name_box = ctk.CTkLabel(top_frame, text=f"{aty2}", font=FONT_MAIN, fg_color="#FFFFFF",text_color="#000000", corner_radius=8, width=420, anchor="w", padx=12)
name_box.grid(row=1, column=0, padx=20, pady=8, sticky="w")

# Тапсыру күні
date_label = ctk.CTkLabel(top_frame, text="Тапсыру күні", text_color="#333", font=FONT_MAIN, fg_color="transparent")
date_label.grid(row=2, column=0, sticky="w", padx=20)

date_box = ctk.CTkLabel(top_frame, text=datetime.now().strftime("%d.%m.%Y"), fg_color="#FFFFFF",text_color="#000000", corner_radius=8, width=420, anchor="w", padx=12)
date_box.grid(row=3, column=0, padx=20, pady=8, sticky="w")

# Балл және %
score_frame = ctk.CTkFrame(top_frame, fg_color="transparent")
score_frame.grid(row=0, column=1, rowspan=4, padx=30, pady=10)

score_box = ctk.CTkLabel(score_frame, text=f"{score}", font=FONT_BIG, fg_color="#FFFFFF",text_color="#000000", corner_radius=12, width=160, height=90, anchor="center")
score_box.grid(row=0, column=0, padx=8)

percent_box = ctk.CTkLabel(score_frame, text=f"{round(score / 15 * 100, 1)}", font=FONT_BIG, fg_color="#FFFFFF",text_color="#000000", corner_radius=12, width=160, height=90, anchor="center")
percent_box.grid(row=0, column=1, padx=8)

# ======================= STATS SECTION ===========================
stats_frame = ctk.CTkFrame(container, fg_color="transparent")
stats_frame.pack(pady=10, fill="x", padx=10)

def make_stat(parent, title_text, value_text):
    box = ctk.CTkFrame(parent, fg_color=BG_CARD, corner_radius=12, width=220, height=120)
    box.pack_propagate(False)
    lbl_title = ctk.CTkLabel(box, text=title_text, font=FONT_MAIN, text_color="#333")
    lbl_title.pack(pady=(12,4))
    lbl_value = ctk.CTkLabel(box, text=value_text, font=FONT_BIG, text_color="#111")
    lbl_value.pack()
    return box

stats_row = ctk.CTkFrame(stats_frame, fg_color="transparent")
stats_row.pack()

total_box = make_stat(stats_row, "барлығы", f"{score+wrong_count}")
total_box.pack(side="left", padx=18)

mistake_box = make_stat(stats_row, "қате", f"{wrong_count}")
mistake_box.pack(side="left", padx=18)

time_box = make_stat(stats_row, "тапсыру уақыты", f"{time_str}")
time_box.pack(side="left", padx=18)

def bastybet():
    root.destroy()
    os.system('python "C:\\Users\\Asus\\Desktop\\Workspace\\Nurait things\\Python 3.13\\py313\\nur\\projectbay\\tirkelu.py"')


    
# ======================= BUTTONS ===========================
btn_frame = ctk.CTkFrame(container, fg_color="transparent")
btn_frame.pack(pady=20)

btn_home = ctk.CTkButton(btn_frame, text="Басты бетке",command=bastybet, width=180, height=44, fg_color=BTN_COLOR, hover_color="#3350e6", text_color="white", corner_radius=12)
btn_home.pack(side="left", padx=14)

btn_exit = ctk.CTkButton(btn_frame, text="Шығу", width=180, height=44, fg_color=BTN_COLOR, hover_color="#3350e6", text_color="white", corner_radius=12, command=root.quit)
btn_exit.pack(side="left", padx=14)

root.mainloop()