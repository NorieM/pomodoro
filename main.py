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
CHECKMARK = '✓'
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    title.config(text='Timer')
    canvas.itemconfig(timer_text, text='00:00')
    check_marks.config(text='')
    window.after_cancel(timer)
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():

    global reps
    reps += 1

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        title.config(text="Break", fg=RED)
    elif reps % 2 == 1:
        count_down(WORK_MIN * 60)
        title.config(text="Work", fg=GREEN)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        title.config(text="Break", fg=PINK)
        check_marks.config(text=CHECKMARK * int(reps / 2))


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    minutes = int(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f'0{seconds}'

    canvas.itemconfig(timer_text, text=f'{minutes}:{seconds}')
    if count > 0:
        global  timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=100, bg=RED)
tomato = PhotoImage(file='tomato.png')
window.iconphoto(False, tomato)

window.after(1000, )

title = Label(text='Timer', font=(FONT_NAME, 50, 'normal'), bg=RED, fg=GREEN)
title.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=RED, highlightthickness=0)
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text='00:00', fill='black', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

btn_start = Button(text='Start', bg=RED, command=start_timer)
btn_start.grid(row=2, column=0)

btn_reset = Button(text='Reset', bg=RED, command=reset_timer)
btn_reset.grid(row=2, column=2)

check_marks = Label(bg=RED, fg=GREEN)

check_marks.grid(row=3, column=1)

window.mainloop()
