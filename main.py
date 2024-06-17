from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import numpy as np
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def find_password():
  user_website = web_bar.get()
  try:
    with open(file="password_manager.json", mode='r') as data_file:
      password_dictionary = json.load(data_file)
      try:
        user_email = password_dictionary[f"{user_website}"]["email"]
        user_password = password_dictionary[f"{user_website}"]["password"]
        messagebox.showinfo(title=f"{user_website}", message=f" User: {user_email}\n Password: {user_password}")
      except KeyError:
        messagebox.showwarning(title="Something is wrong", message=f"No details for the {user_website} exists")
  except FileNotFoundError:
    messagebox.showwarning(title="Error", message="No data file found")

#Password Generator Project
def generate_password():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  password_list = []
  password_list = [random.choice(letters) for char in range(random.randint(8, 10))]

  password_list += [random.choice(symbols) for char in range(random.randint(2, 4))]

  password_list += [random.choice(numbers) for char in range(random.randint(2, 4))]

  random.shuffle(password_list)

  password = "".join(password_list)
  pass_bar.insert(0, password)
  pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
  website = web_bar.get()
  user = user_bar.get()
  password = pass_bar.get()
  separation = "************************"
  new_data = {website:{
    "email": user,
    "password": password
  }}

  if len(website) == 0 or len(password) == 0:
    messagebox.showwarning(title="You forgot information", message="Please don't leave any field empty")

  else:
    try:
      with open(file="password_manager.json", mode='r') as data_file:
        # Reading old data
        data = json.load(data_file)
        # Updating old data with new data
        data.update(new_data)
    except FileNotFoundError:
      with open(file="password_manager.json", mode='w') as data_file:
        json.dump(new_data, data_file, indent=4)
        
    else:
      with open("password_manager.json", "w") as data_file:
        # saving update data
        json.dump(data, data_file, indent=4)
    finally:
        web_bar.delete(0, END)
        pass_bar.delete(0, END)
    

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

# Adding the image
canvas = Canvas(width=200, height=200)
password_img = PhotoImage(file="logo.png")
canvas.create_image(100, 94, image=password_img)
canvas.grid(row=0, column=1)

# Adding the website section
label_web = Label(text="Website:")
label_web.grid(row=1, column=0)
web_bar = Entry(width=24)
web_bar.grid(row=1, column=1)


# Adding the search bar
search_bar = Button(text="Search", command=find_password, width=13)
search_bar.grid(row=1,column=2)

# Adding the User section
label_user = Label(text="Email/Username:")
label_user.grid(row=2, column=0)
user_bar = Entry(width=42)
user_bar.grid(row=2, column=1, columnspan=2)
user_bar.insert(0, "alberto.gzga@gmail.com")

# Adding the Password section
pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)
pass_bar = Entry(width=24, show="*")
pass_bar.grid(row=3, column=1)

# Generate password buttom
generate_pass = Button(text="Generate Password", command=generate_password)
generate_pass.grid(row=3, column=2)

# Save buttom
save = Button(width=36, text="Save", command=save)
save.grid(row=4, column=1, columnspan=2)

window.mainloop()