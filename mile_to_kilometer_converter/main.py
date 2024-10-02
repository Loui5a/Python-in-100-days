from tkinter import *

def button_clicked():
    value = float(miles.get())
    converted_value = round((value * 1.60934), 2)
    label_4.config(text=converted_value)


window = Tk()
window.title("Mile to Km Converter")
#window.minsize(width=300, height=150)
window.config(padx=25, pady=25)

label_1 = Label(text="is equal to")
label_1.config(padx=10, pady=10)
label_1.grid(column=0, row=2)

label_2 = Label(text="Miles")
label_2.config(padx=10, pady=10)
label_2.grid(column=2, row=1)

label_3 = Label(text="Km")
label_3.config(padx=10, pady=10)
label_3.grid(column=2, row=2)

label_4 = Label(text="0")
label_4.config(padx=10, pady=10)
label_4.grid(column=1, row=2)

miles = Entry(width=7)
miles.grid(column=1, row=1)

button = Button(text="Calculate", command=button_clicked)
button.config(padx=10, pady=10)
button.grid(column=1, row=3)
window.mainloop()