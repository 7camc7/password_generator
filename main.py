from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    p_letters = [choice(letters) for char in range(nr_letters)]
    p_symbols = [choice(symbols) for char in range(nr_symbols)]
    p_numbers = [choice(numbers) for char in range(nr_numbers)]

    password_list = p_letters + p_symbols + p_numbers
    shuffle(password_list)

    password = "".join(password_list)
    entry_password.insert(0, password)
    pyperclip.copy(password) #already in clipboard


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Don't leave fields empty!")
    else:
        is_ok = messagebox.askokcancel(message=f"Details entered for {website}:\n\n {email}\n{password}\n\nOk to save?")
        if is_ok:
            with open("datafile.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
            entry_website.delete(0, END)
            entry_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

label_website = Label(text="Website: ")
label_website.grid(column=0, row=1)

label_email = Label(text="Email/Username: ")
label_email.grid(column=0, row=2)

label_password = Label(text="Password: ")
label_password.grid(column=0, row=3)

entry_website = Entry(width=35)
entry_website.grid(column=1, row=1, columnspan=2)
entry_website.focus()

entry_email = Entry(width=35)
entry_email.grid(column=1, row=2, columnspan=2)
entry_email.insert(0, "claudiachurch00@gmail.com")

entry_password = Entry(width=18)
entry_password.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36,command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
