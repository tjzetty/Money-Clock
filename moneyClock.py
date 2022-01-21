import tkinter
from tkinter import *

ws = Tk()
ws.title('Money Clock')
ws.config(bg='#299617')

rate = 0
counter = 0
flag = False
running = False


def counter_label(lbl):
    def count():
        if running:
            global counter
            global rate
            if flag == False:
                display = "$ --"
            else:
                display = '$ ' + f"{counter:.2f}"

            lbl['text'] = display

            lbl.after(8, count)
            counter += .008 * rate / 3600

    count()


def StartTimer(lbl):
    global running
    global flag
    flag = True
    running = True
    counter_label(lbl)
    start_btn['state'] = 'disabled'
    stop_btn['state'] = 'normal'
    reset_btn['state'] = 'normal'


def StopTimer():
    global running
    start_btn['state'] = 'normal'
    stop_btn['state'] = 'disabled'
    reset_btn['state'] = 'normal'
    running = False


def ResetTimer(lbl):
    global counter
    counter = 0
    if running == False:
        reset_btn['state'] = 'disabled'
        lbl['text'] = '$ 0.00'
    else:
        lbl['text'] = ''


def validate(value):
    if value:
        try:

            return float(value) >= 0
        except ValueError:
            return False
    else:
        return False


def returnEntry(arg=None):
    """Gets the result from Entry and return it to the Label"""
    global rate

    result = entry.get()
    if validate(result):
        rate = float(result)
        label_msg.config(text="$" + f"{rate:.2f}" + "/hr")
        entry.delete(0, END)
    else:
        entry.delete(0, END)
        entry.insert(0, "Must be a number")


lbl = Label(
    ws,
    text="$ 0.00",
    fg="black",
    bg='#299617',
    font="Verdana 40 bold"
)

label_entry = Label(
    ws,
    text="Enter Rate:",
    fg="black",
    bg='#299617',
    font="Verdana 10 bold",
)
label_entry.grid(column=0, row=0, padx=10, pady=30, sticky=tkinter.E)

entry = Entry(
    ws,
    width=20,
    font="Verdana 10 bold",
)
entry.focus()
entry.bind("<Return>", returnEntry)
entry.grid(column=1, row=0, padx=10, pady=30,)

label_msg = Label(
    ws,
    text="$-/hr",
    fg="black",
    bg='#299617',
    font="Verdana 10 bold"
)

lbl.grid(column=1, row=1, padx=10, pady=0, sticky=tkinter.W, columnspan=3)
label_msg.grid(column=1, row=2, padx=25, pady=0, sticky=tkinter.W, columnspan=3)

start_btn = Button(
    ws,
    text='Start',
    width=15,
    command=lambda: StartTimer(lbl)
)
stop_btn = Button(
    ws,
    text='Stop',
    width=15,
    state='disabled',
    command=StopTimer
)

reset_btn = Button(
    ws,
    text='Reset',
    width=15,
    state='disabled',
    command=lambda: ResetTimer(lbl)
)

start_btn.grid(column=0, row=3, padx=10, pady=30, sticky=tkinter.W)
stop_btn.grid(column=1, row=3, padx=10, pady=30, )
reset_btn.grid(column=2, row=3, padx=10, pady=30, sticky=tkinter.E)



ws.mainloop()