
# Import Libraries
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
reps = 0
# ---------------------------- TIMER RESET ------------------------------- # 



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
        if reps%2 == 0:
            count_down(WORK_MIN*60)
        elif reps%7 == 0:
            count_down(LONG_BREAK_MIN*60)
        else:
            count_down(SHORT_BREAK_MIN*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    minutes = count // 60
    seconds = count % 60
    canvas.itemconfig(timer_text, text = f"{'{:02d}'.format(minutes)}:{'{:02d}'.format(seconds)}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        global reps
        reps += 1
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady = 50, bg = YELLOW)

# Label: "Timer"
label_01 = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg = GREEN, bg = YELLOW)
label_01.config(padx=0, pady=5)
label_01.grid(column=1, row=0)

# Button: "Start"
button_start = Button(text = "Start", highlightthickness=0, command=start_timer)
button_start.grid(column=0, row=2)
button_start.config(padx=5, pady=5)

# Button: "Reset"
button_reset = Button(text = "Reset", highlightthickness=0)
button_reset.grid(column=2, row=2)
button_reset.config(padx=5, pady=5)

# Label: check mark
check_mark = "✔"
label_02 = Label(text=check_mark, font=(FONT_NAME, 35, "bold"), fg = GREEN, bg = YELLOW)
label_02.config(padx=0, pady=5)
label_02.grid(column=1, row=3)

# Pomodoro canvas
canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness=0)
pomodoro_image = PhotoImage(file = "tomato.png")
canvas.create_image(100, 112, image = pomodoro_image)
timer_text = canvas.create_text(100, 130, text = "00:00", fill = "white", font = (FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


window.mainloop()