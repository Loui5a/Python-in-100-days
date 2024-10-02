from tkinter import *


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)
# label:
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label["text"] = "new text"
my_label.config(text="new text")
#my_label.pack()
#my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)

#button:
button = Button(text="Click me", command=button_clicked)
#button.pack()
button.grid(column=1, row=1)
new_button = Button(text="New Button")
new_button.grid(column=2,row=0)
# entry
input = Entry(width=10)
#input.pack()
input.grid(column=3, row=2)

# always placed at the end
window.mainloop()