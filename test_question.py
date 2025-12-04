import customtkinter as ctk
from tkinter import messagebox
from database.db2 import add_user ,cleanup_results
from PIL import Image
import json
import random
import time
import os
import sys


ctk.set_appearance_mode("light")
ctk.set_default_color_theme("dark-blue")


#Argumennti alu
aty2 = sys.argv[1]
selected_subject = sys.argv[2]
parol2 = sys.argv[3]
jssn = sys.argv[4]
data = sys.argv[5]
kerek =[]
#score , {minutes:02d}:{seconds:02d} , len(shuffled_questions)


# ------------------- Загружаем JSON -------------------
SUBJECT_FILES = {
    "Тарих": r"C:\Users\Asus\Desktop\Workspace\Nurait things\Python 3.13\py313\nur\projectbay\materials\tarikh.json",
    "Информатика": r"C:\Users\Asus\Desktop\Workspace\Nurait things\Python 3.13\py313\nur\projectbay\materials\infor.json",
    "Математика": r"C:\Users\Asus\Desktop\Workspace\Nurait things\Python 3.13\py313\nur\projectbay\materials\math.json"
}

def start_test_window():
    global selected_subject
    
    if selected_subject not in SUBJECT_FILES:
        print("Алдымен пәнді таңдаңыз!")
        return

    file_name = SUBJECT_FILES[selected_subject]   # мысалы: "tarikh.json"

    # JSON ашу
    with open(file_name, "r", encoding="utf-8") as f:
        questions = json.load(f)

    return questions    

all_questions = start_test_window()
# Выбираем случайно 15 вопросов
random.shuffle(all_questions)
questions = all_questions[:15]

# Перемешиваем выбранные вопросы один раз
shuffled_questions = questions.copy()
random.shuffle(shuffled_questions)

# ------------------- Window -------------------
app = ctk.CTk()
app.title("Тестілеуші программа")
app.geometry("1040x700")

# ------------------- Header -------------------
header = ctk.CTkFrame(app, fg_color="#03287B", height=80, corner_radius=0)
header.pack(fill="x")

header_user = ctk.CTkLabel(
    header,
    text="Уақыт:",
    text_color="white",
    font=("Inter", 16, "bold"),
)
header_user.place(relx=0.08, rely=0.5, anchor="center")

title = ctk.CTkLabel(
    header,
    text="ТЕСТІЛЕУШІ ПРОГРАММА",
    text_color="white",
    font=("Arial", 22, "bold"),
)
title.place(relx=0.5, rely=0.5, anchor="center")

logo_path = r"C:\Users\Asus\Desktop\Workspace\Nurait things\Python 3.13\py313\nur\projectbay\materials\xx.png"
logo_image = ctk.CTkImage(
    light_image=Image.open(logo_path),
    dark_image=Image.open(logo_path),
    size=(70, 70)
)
logo_label = ctk.CTkLabel(header, image=logo_image, text="")
logo_label.place(relx=0.93, rely=0.5, anchor="center")

# ------------------- Глобальные переменные -------------------
user_answers = {}       # выбранные ответы
current = 0
selected_answer = ctk.IntVar(value=-1)
time_left = 30 * 60     # 30 минут
timer_running = True
test_finished = False
start_time = time.time()

# ------------------- Навигатор сверху -------------------
nav_frame = ctk.CTkFrame(app, fg_color="transparent")
nav_frame.pack(pady=(33, 0))
nav_buttons = []

def save_answer():
    if test_finished:
        return
    if selected_answer.get() != -1:
        user_answers[current] = selected_answer.get()
        update_finish_button()
        update_nav_buttons()

def go_to_question(idx):
    global current
    save_answer()
    current = idx
    load_question()

def update_nav_buttons():
    for i, btn in enumerate(nav_buttons):
        if i == current:
            btn.configure(fg_color="#E0E0E0")
        elif i in user_answers:
            btn.configure(fg_color="#C0FFC0")  # зеленый, если ответ есть
        else:
            btn.configure(fg_color="#FFFFFF")

for i in range(len(shuffled_questions)):
    btn = ctk.CTkButton(
        nav_frame,
        text=str(i+1),
        width=60,
        height=35,
        fg_color="#FFFFFF",
        border_color="#B0B0B0",
        border_width=2,
        text_color="#000000",
        font=("Inter", 16),
        hover_color="#E0E0E0",
        command=lambda i=i: go_to_question(i)
    )
    btn.pack(side="left", padx=1)
    nav_buttons.append(btn)

# ---------- Метка вопроса ----------
question_label = ctk.CTkLabel(app, text="", font=("Inter", 25), wraplength=800)
question_label.pack(pady=(38, 0))

# ---------- Контейнер для вариантов ----------
options_frame = ctk.CTkFrame(app, fg_color="transparent")
options_frame.pack(pady=(34, 0))

# ---------- Кнопки "Предыдущий" / "Следующий" / "Закончить" ----------
nav_control_frame = ctk.CTkFrame(app, fg_color="transparent")
nav_control_frame.pack(pady=10)

def prev_question():
    global current
    save_answer()
    if current > 0:
        current -= 1
        load_question()

def next_question():
    global current
    save_answer()
    if current < len(shuffled_questions) - 1:
        current += 1
        load_question()

prev_btn = ctk.CTkButton(
    nav_control_frame, 
    text="<-   Алдыңғы", 
    command=prev_question, 
    width=166, 
    height=43, 
    fg_color="#3366FF", 
    corner_radius=5,
    text_color="#ffffff",
    font=("Inter", 16),
    hover_color="#254FCC"
)
prev_btn.pack(side="left", padx=20, pady=(25,0))

next_btn = ctk.CTkButton(
    nav_control_frame, 
    text="Келесі   ->", 
    command=next_question, 
    width=166, 
    height=43, 
    fg_color="#3366FF", 
    corner_radius=5,
    text_color="#ffffff",
    font=("Inter", 16),
    hover_color="#254FCC"
)
next_btn.pack(side="left", padx=20, pady=(25,0))

finish_btn = ctk.CTkButton(
    nav_control_frame, 
    text="Аяқтау", 
    command=lambda: finish_test(), 
    width=166, 
    height=43, 
    state="disabled", 
    fg_color="#888888",
    corner_radius=5,
    font=("Inter", 16)
)
finish_btn.pack(side="left", padx=20, pady=(25,0))

def update_finish_button():
    if len(user_answers) == len(shuffled_questions):
        finish_btn.configure(state="normal", fg_color="#FF0000")
    else:
        finish_btn.configure(state="disabled", fg_color="#888888")

# ---------- Загрузка вопроса ----------
def load_question():
    q = shuffled_questions[current]
    question_label.configure(text=q["question"])

    # очищаем старые варианты
    for widget in options_frame.winfo_children():
        widget.destroy()

    # перемешиваем варианты только один раз
    if q.get("shuffled") is None:
        q["shuffled"] = q["options"].copy()
        random.shuffle(q["shuffled"])

    # создаём радиокнопки
    for i, option in enumerate(q["shuffled"]):
        btn_frame = ctk.CTkFrame(
            options_frame,
            fg_color="#FFFFFF",
            corner_radius=5,
            border_color="#B0B0B0",
            border_width=2
        )
        btn_frame.pack(pady=10, fill="x", padx=20)

        rb = ctk.CTkRadioButton(
            btn_frame,
            variable=selected_answer,
            value=i,
            text="    " + option,
            width=530,
            height=50,
            font=("Inter", 18),
            state="disabled" if test_finished else "normal"
        )
        rb.pack(padx=20, pady=5, anchor="w")

    # восстанавливаем выбор пользователя
    if current in user_answers:
        selected_answer.set(user_answers[current])
    else:
        selected_answer.set(-1)

    update_finish_button()
    update_nav_buttons()

# ---------- Таймер ----------
timer_label = ctk.CTkLabel(
    header,
    text="30:00",
    text_color="white",
    font=("Inter", 20, "bold")
)
timer_label.place(relx=0.15, rely=0.5, anchor="center")

def start_timer():
    global time_left, timer_running
    if not timer_running:
        return

    mins = time_left // 60
    secs = time_left % 60
    timer_label.configure(text=f"{mins:02d}:{secs:02d}")

    if time_left > 0:
        time_left -= 1
        app.after(1000, start_timer)
    else:
        timer_label.configure(text="Время вышло!")
        finish_test()

# ---------- Завершение теста ----------
def finish_test():
    global timer_running, test_finished
    timer_running = False
    test_finished = True

    save_answer()

    if len(user_answers) < len(shuffled_questions):
        messagebox.showwarning(title="Ошибка", message="Ответьте на все вопросы перед завершением!")
        timer_running = True
        test_finished = False
        return

    score = 0
    for i, q in enumerate(shuffled_questions):
        if user_answers.get(i) == q["shuffled"].index(q["answer"]):
            score += 1
         

    end_time = time.time()
    total_seconds = int(end_time - start_time)
    minutes = total_seconds // 60
    seconds = total_seconds % 60

    app.destroy()
    os.system(
    f'python "C:\\Users\\Asus\\Desktop\\Workspace\\Nurait things\\Python 3.13\\py313\\nur\\projectbay\\result.py" '
    f'"{aty2}" "{score}" "{data}" "{len(shuffled_questions)-score}" "{minutes:02d}:{seconds:02d}"'
)
    add_user(aty2, jssn, score,data,f"{len(shuffled_questions)-score}")
    cleanup_results(jssn)


   
    next_btn.configure(state="disabled")
    prev_btn.configure(state="disabled")
    finish_btn.configure(state="disabled")
    for btn in nav_buttons:
        btn.configure(state="disabled")
    for widget in options_frame.winfo_children():
        for child in widget.winfo_children():
            child.configure(state="disabled")




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
load_question()
update_nav_buttons()
start_timer()

app.mainloop()

