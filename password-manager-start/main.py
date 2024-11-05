from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_button_click():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    my_password = "".join(password_list)
    entry_password.insert(0, my_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_button_click():
    website_value = entry_website.get()
    email_value = entry_email.get()
    password_value = entry_password.get()
    new_data = {
        website_value: {
            "email": email_value,
            "password": password_value,
        }
    }

    if len(website_value) == 0 or len(password_value) == 0:
        messagebox.showinfo(title="Entries Missing", message="Please fill out all entries")
    else:
        try:
            with open("MyPasswords.json", "r") as file:
            #reading old data:
                data = json.load(file)
        except FileNotFoundError:
            with open("MyPasswords.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            #updating old data with new data:
            data.update(new_data)

            with open("MyPasswords.json", "w") as file:
                # saving updated data:
                json.dump(data, file, indent=4)
        finally:
            entry_website.delete(0, END)
            entry_password.delete(0, END)

# ---------------------------- SEARCH SETUP ------------------------------- #

def search_button_click():
    website_value = entry_website.get()
    try:
        with open("MyPasswords.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        if website_value in data:
            email_value = data[website_value]["email"]
            password_value = data[website_value]["password"]
            messagebox.showinfo(title="Website", message=f"Email: {email_value} \nPassword: {password_value}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website_value} exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# label:
label_website = Label(text="Website:")
label_website.grid(column=0, row=1)
label_email = Label(text="Email/Username:")
label_email.grid(column=0, row=2)
label_password = Label(text="Password:")
label_password.grid(column=0, row=3)

# Entry:
entry_website = Entry(width=35)
entry_website.grid(column=1, columnspan=2, row=1, sticky="EW")
entry_website.focus()
entry_email = Entry(width=35)
entry_email.grid(column=1, columnspan=2, row=2, sticky="EW")
entry_email.insert(0, "MyEmail@mail.com")
entry_password = Entry(width=15)
entry_password.grid(column=1, row=3, sticky="EW")

# Button:
password_button = Button(text="Generate Password", width=15, command=password_button_click)
password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, command=add_button_click)
add_button.grid(column=1, columnspan=2, row=4, sticky="EW")
search_button = Button(text="Search", width=15, command=search_button_click)
search_button.grid(column=2, row=1, sticky="EW")
window.mainloop()