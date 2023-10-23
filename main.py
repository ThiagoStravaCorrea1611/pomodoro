
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady = 50, bg = YELLOW)

# Label: "Timer"
label_01 = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg = GREEN, bg = YELLOW)
label_01.config(padx=0, pady=5)
label_01.grid(column=1, row=0)

check_mark = "✔"


canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness=0)
pomodoro_image = PhotoImage(file = "tomato.png")
canvas.create_image(100, 112, image = pomodoro_image)
canvas.create_text(100, 130, text = "00:00", fill = "white", font = (FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


window.mainloop()