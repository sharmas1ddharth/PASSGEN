import sqlite3
import pyperclip as clip


def view_password(website):
    conn = sqlite3.connect('PASSWORDS.db')
    cursor = conn.cursor()
    command = f"""SELECT * FROM PASSWORD  where Website == '{website}';
                     """
    cursor.execute(command)
    result = cursor.fetchall()
    website_name = result[0][0]
    username = result[0][1]
    password = result[0][2]
    notes = result[0][3]
    print(f"""website = {website_name}\nUsername = {username}\nPassword = {password}\nNotes = {notes}

The password have been copied to the clipboard""")
    clip.copy(password)
    conn.commit()
    conn.close()


website_name_input = input()
view_password(website_name_input)
