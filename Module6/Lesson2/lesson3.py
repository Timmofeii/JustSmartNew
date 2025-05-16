import sqlite3
from prettytable import PrettyTable

conn = sqlite3.connect("my_database.db")
cursor = conn.cursor()
# users = [
#     ("Alice", 25),
#     ("Bob", 42),
#     ("Charlie", 18),
#     ("Diana", 33),
#     ("Ethan", 67),
#     ("Fiona", 24),
#     ("George", 55),
#     ("Hannah", 39),
#     ("Isaac", 22),
#     ("Julia", 70),
#     ("Kevin", 29),
#     ("Liam", 45),
#     ("Mia", 58),
#     ("Noah", 16),
#     ("Olivia", 30)
# ]
#
# cursor.executemany('''
#     INSERT INTO users (name, age)
#     VALUES (?, ?)
# ''', users)
# conn.commit()

# cursor.execute("SElECT*FROM users")
# print(cursor.fetchall())
#
# cursor.execute('''
# UPDATE users
# SET age = 18
# WHERE age < 18
# ''')
#
# cursor.execute("SElECT*FROM users")
# print(cursor.fetchall())
# cursor.execute('''
# UPDATE users
# SET name = "Ms." || name
# where name like 'M%'
# ''')
# cursor.execute("SElECT*FROM users")
# print(cursor.fetchall())
#
cursor.execute('''
DELETE from users
WHERE age > 60

''')


# def show_table(table):
#     for row in table:
#         line = ' | '.join(map(str, row))
#         print(line)


def show_table_pretty():
    headers = [desc[0] for desc in cursor.description]
    table = cursor.fetchall()

    x = PrettyTable()
    x.field_names = headers
    for row in table:
        x.add_row(row)
    print(x)


# Задаем заголовки колонок
cursor.execute("SELECT * FROM users")
columns = [desc[0] for desc in cursor.description]
rows = cursor.fetchall()

# Красивый вывод
show_table_pretty()
name, age = 'Tima', 28
users = {name: age}
for name in users:
    if users[name] < 25:
        users[name] = 18
cursor.execute('''
UPDATE users 
SET age =  18
WHERE age < 18
''')

# cursor.execute('''
# UPDATE character
# SET health_points = health_points-((5*4)+20)
# ''')

cursor.execute("SELECT * FROM character")

# cursor.execute('''
# UPDATE character
# SET health_points = health_points ''')

cursor.execute("SELECT * FROM users")

columns = [desc[0] for desc in cursor.description]
rows = cursor.fetchall()
show_table_pretty()

conn.close()

#
# import tkinter as tk
#
# phonebook = {"Tima": 2536489903, "Daniel": 2534490245}
#
#
# str_name_contact = "Contact's name"
# str_number_contact = "Contact's phone number"
# str_enter_name = "Enter name"
# str_button_back = "Main menu"
# WIDTH_Entry = 40
#
#
# def show_contacts_frame():
#     frame_contacts = tk.Frame(root)
#     frame_contacts.grid(row=0, column=0)
#     scrollbar = tk.Listbox(frame_contacts, selectmode=tk.SINGLE)
#
#     for contact in phonebook:
#         scrollbar.insert(tk.END, contact)
#     scrollbar.grid(row=0, column=0)
#     button_back = tk.Button(frame_contacts, text="Back", bg='red',
#                             command=lambda: switch_frame(frame_contacts, frame_main))
#     button_back.grid(row=0, column=1)
#
#
# def on_entry_click(event, txt):
#     entry = event.widget
#     if entry.get() == txt:
#         entry.delete(0, tk.END)
#         entry.config(fg="black")
#
#
# def exit_entry(event, txt):
#     entry = event.widget
#     if len(entry.get()) < 1:
#         entry.delete(0, tk.END)
#         entry.insert(0, txt)
#
#
# def custom_entry(frame, text, width=40):
#     entry = tk.Entry(frame, width=width)
#     entry.insert(0, text)
#     entry.bind('<FocusIn>', lambda event: on_entry_click(event, text))
#     entry.bind('<FocusOut>', lambda event: exit_entry(event, text))
#
#     return entry
#
#
# def get_data():
#     number = numberEntry.get()
#     name = nameEntry.get()
#     if len(name) > 3 and len(number) > 8:
#         phonebook[name] = number
#         numberEntry.delete(0, tk.END)
#         nameEntry.delete(0, tk.END)
#         switch_frame(frame_save_contact, frame_main)
#
#
# def switch_frame(close_frame, open_frame):
#     close_frame.grid_remove()
#     open_frame.grid()
#
#
# def remove_contact():
#     name = entry_delete_contact.get()
#     if name in phonebook:
#         phonebook.pop(name)
#         entry_delete_contact.delete(0, tk.END)
#     entry_delete_contact.config(fg="red")
#
#
# def show_contact(label):
#     name = entry_find_contact.get()
#     if name in phonebook:
#         number = phonebook[name]
#         label.config(text=number)
#
#
# root = tk.Tk()
# root.geometry("400x300")
#
# # *****************************frameMain*********************
# frame_main = tk.Frame(root)
# frame_find_contact = tk.Frame(root)
# frame_delete_contact = tk.Frame(root)
# frame_save_contact = tk.Frame(root)
# frame_main.grid(row=0, column=0)
#
# label = tk.Label(frame_main, text="click button to command", pady=5, padx=5)
# label.grid(row=0, column=0, columnspan=2)
#
# button_add_contact = tk.Button(frame_main, text="Add contact",
#                                command=lambda: switch_frame(frame_main, frame_save_contact))
# button_add_contact.grid(row=2, column=0, sticky="w", pady=5)
#
# button_find_contact = tk.Button(frame_main, text="Find contact",
#                                 command=lambda: switch_frame(frame_main, frame_find_contact))
# button_find_contact.grid(row=3, column=0, sticky="w", pady=5)
#
# button_to_frame_delete_contact = tk.Button(frame_main, text="Delete contact",
#                                            command=lambda: switch_frame(frame_main, frame_delete_contact))
# button_to_frame_delete_contact.grid(row=4, column=0, sticky="w", pady=5)
#
# button_to_frame_show_contacts = tk.Button(frame_main, text="Show contacts",
#                                           command=lambda: show_contacts_frame())
# button_to_frame_show_contacts.grid(row=5, column=0, sticky='w', pady=5)
# # *************************frameFindContacts**************************
#
# entry_find_contact = custom_entry(frame_find_contact, str_enter_name)
# entry_find_contact.grid(row=0, column=0)
#
# button_show_number = tk.Button(frame_find_contact, text='Find', bg='green',
#                                command=lambda: show_contact(label_show_number))
# button_show_number.grid(row=0, column=1)
#
# label_show_number = tk.Label(frame_find_contact)
# label_show_number.grid(row=1, column=0, sticky="w")
#
# button_back = tk.Button(frame_find_contact, text=str_button_back,
#                         command=lambda: switch_frame(frame_find_contact, frame_main))
# button_back.grid(row=2, column=0, sticky=tk.W)
#
# frame_find_contact.grid(row=0, column=0)
# frame_find_contact.grid_remove()
# # *****************************frameDeleteContact*********************
#
# entry_delete_contact = custom_entry(frame_delete_contact, "Contact`s name for del")
# entry_delete_contact.grid(row=0, column=0)
#
# button_back = tk.Button(frame_delete_contact, text=str_button_back,
#                         command=lambda: switch_frame(frame_delete_contact, frame_main))
#
# button_enter = tk.Button(frame_delete_contact, text='Delete contact', bg='red',
#                          command=remove_contact)
#
# button_enter.grid(row=0, column=1)
# button_back.grid(row=1, columnspan=2)
# frame_delete_contact.grid(row=0, column=0)
# frame_delete_contact.grid_remove()
#
# # *****************************frameSaveContact*********************
#
# frame_save_contact.grid(row=0, column=0)
#
# nameEntry = custom_entry(frame_save_contact, str_name_contact, WIDTH_Entry)
# nameEntry.grid(row=1, column=0, pady=5)
#
# numberEntry = custom_entry(frame_save_contact, str_number_contact, WIDTH_Entry)
# numberEntry.grid(row=2, column=0, pady=5)
#
# button_enter = tk.Button(frame_save_contact, text="enter", bg='green', command=get_data)
# button_enter.grid(row=3, column=0, columnspan=1, padx=5, pady=5)
#
# frame_save_contact.grid_remove()  # закрыли меню для сохранения контакта
#
# root.mainloop()
