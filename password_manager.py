import tkinter as tk
from tkinter import Canvas, PhotoImage, Entry, Button
from tkinter.ttk import Label
from tkinter import messagebox
import random
import pyperclip


def add():

    web_input = website_entry.get()
    user_input = username_entry.get()
    pass_input = password_entry.get()

    if len(web_input) == 0 or len(user_input) == 0 or len(pass_input) == 0:
        messagebox.showinfo(title= "Caution!", message= "Please do not leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title = "Attention" , message= f"Are you sure you want to enter these details: \n"
                                                                      f"Username: {user_input} \nPassword: {pass_input}")

        if is_ok:
            with open("data.txt", "a+") as file:
                file.write(f"{web_input} | {user_input} | {pass_input} \n")

            website_entry.delete(0, tk.END)
            username_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)

def gen_password():
    alphnum_list = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
        '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+',
        '[', ']', '{', '}', ';', ':', ',', '.', '<', '>', '?', '/']

    gen_list = [alphnum_list[random.randint(0,88)] for i in range(random.randint(11,13))]

    password = ''
    for k in gen_list:
        password+=k

    password_entry.insert(0, password)
    pyperclip.copy(password)

window = tk.Tk()
window.title("PASS-MANAGER")
window.minsize(width= 250, height= 250)
window.configure(padx= 70, pady= 70)
#window.configure(bg = "white")

canvas = Canvas(width = 230, height = 230, highlightthickness=0)
#canvas.configure(bg = "white")
lock_image = PhotoImage(file= "download.png")
canvas.create_image(115,115, image = lock_image)
canvas.grid(row = 0, column = 1)

website_label = Label(text = "Website: ")
website_label.grid(row = 1 , column = 0)
website_entry = Entry(width = 40)
website_entry.focus()
website_entry.grid(row = 1 , column = 1, columnspan = 2)

username_label = Label(text = "Email / Username: ")
username_label.grid(row = 2 , column = 0)
username_entry = Entry(width = 40)
username_entry.grid(row = 2 , column = 1, columnspan = 2)

password_label = Label(text = "Password ")
password_label.grid(row = 3 , column = 0)
password_entry = Entry(width = 24)
password_entry.grid(row = 3 , column = 1)

genpass = Button(text = "Generate Password", width= 12, command= gen_password)
genpass.grid(row = 3 , column = 2)

add = Button(text = "Add", width= 38, command= add)
add.grid(row = 4, column = 1, columnspan = 2)








window.mainloop()

