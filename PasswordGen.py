import random
import tkinter as tk
import platform

if platform.system() in "Darwin":
    from tkmacosx import Button
else:
    from tkinter import Button

root = tk.Tk()

canvas = tk.Canvas(root, width=550, height=500, relief='raised')
canvas.pack()

entry_password = tk.Entry(root)
title_password = tk.Label(root, text="What is this password for?")
canvas.create_window(120, 100, window=title_password)
canvas.create_window(120, 140, window=entry_password)


def generatePassword():
    password_length = 12
    canvas.delete("password")

    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
               "S", "T", "U", "V", "W", "X", "Y", "Z"]
    special_characters = ["?", ".", "*", "@", "#", "&", "!", "%", "'", "^"]
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    password_letters_list = []
    password = ""
    purpose = entry_password.get()
    entry_password.delete(0, tk.END)
    index = 0

    for i in range(0, password_length // 2):
        password_letters_list += letters[random.randint(0, len(letters) - 1)]
    for i in range(0, password_length + 1):
        rand_int = random.randint(0, 1)

        if i % 2 == 0 and index < len(password_letters_list):
            if index % 2 == 0:
                password_letters_list[index] = password_letters_list[index].lower()
            password += password_letters_list[index]
            index += 1

        elif rand_int == 1:
            random_special_character = special_characters[random.randint(0, len(special_characters) - 1)]
            password += random_special_character

        elif rand_int == 0:
            random_number = numbers[random.randint(0, len(numbers) - 1)]
            password += str(random_number)

    with open("passwords.txt", 'a') as input_password:
        print(purpose)
        input_password.writelines(purpose + " " + password + '\n')
    password_label = tk.Label(root,
                              text="\nThe password has been added,\nenter a new name and click "
                                   "\nthe button again to "
                                   "\ncreate a new password")

    ent = tk.Entry(root, state='readonly', readonlybackground='white', fg='black')
    var = tk.StringVar()
    var.set(password)
    ent.config(textvariable=var, relief='flat')
    ent.pack()
    canvas.create_window(120, 290, window=password_label, tags="password")
    canvas.create_window(120, 250, window=ent, tags="password")


password_button = Button(text="Generate a Password", command=generatePassword, bg="black", fg="white")
password_button.pack()
canvas.create_window(120, 200, window=password_button)

title_finder = tk.Label(root, text="What password do you need?")
title_finder.pack()
canvas.create_window(400, 100, window=title_finder)

finder_entry = tk.Entry(root)
canvas.create_window(400, 140, window=finder_entry)


def findPassword():
    keyword_line = ""
    thankyoutext = "Enter another keyword \nto find a new password"
    keyword = finder_entry.get()
    canvas.delete("discovered_password")

    with open("passwords.txt", 'r') as read_lines:
        for line in read_lines:
            if keyword.lower() in line.lower():
                keyword_line = line

        if keyword_line == "":
            keyword_line = "The password you are looking for does not exist"

    keyword_label = tk.Label(root, text=thankyoutext)
    ent_finder = tk.Entry(root, state='readonly', readonlybackground='white', fg='black')
    var = tk.StringVar()
    var.set(keyword_line)
    ent_finder.config(textvariable=var, relief='flat')
    ent_finder.pack()

    canvas.create_window(400, 250, window=ent_finder, tags="discovered_password")
    canvas.create_window(400, 290, window=keyword_label, tags="discovered_password")
    finder_entry.delete(0, tk.END)


finder_button = Button(text="Find Password", command=findPassword, bg="black", fg="white")
finder_button.pack()
canvas.create_window(400, 200, window=finder_button)
root.mainloop()
