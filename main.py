import os
import sqlite3
import random

files = os.listdir(os.getcwd())

website = input("Website: ")
username = input("Username: ")
password_len = input("Password len: ")
notes = input("Notes: ")


def create_database():
    conn = sqlite3.connect('PASSWORDS.db')

    command = """ CREATE TABLE IF NOT EXISTS PASSWORD (
                    Website VARCHAR(255),
                    Username VARCHAR(255),
                    Password VARCHAR(255),
                    Note VARCHAR(255)
                    );
                 """
    conn.execute(command)

    conn.close()


def insert_data(website_, username_, password_, note_):
    conn = sqlite3.connect('PASSWORDS.db')
    cursor = conn.cursor()
    command = (f"""
                    insert into PASSWORD (Website, Username, Password, Note) 
                    VALUES ('{website_}', '{username_}', '{password_}', '{note_}');
                """)
    count = cursor.execute(command)
    conn.commit()

    cursor.close()


def get_password(password_length):
    temp = []

    UPPERCASE = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']
    LOWERCASE = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u',
                 'v', 'w', 'x', 'y', 'z']
    DIGITS = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    SYMBOLS = ['@', '#', '$', '%', '=', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']

    COMBINED_LIST = UPPERCASE + LOWERCASE + DIGITS + SYMBOLS

    temp.append(random.choice(UPPERCASE))
    temp.append(random.choice(LOWERCASE))
    temp.append(random.choice(DIGITS))
    temp.append(random.choice(SYMBOLS))

    while len(temp) != password_length:
        temp.append(random.choice(COMBINED_LIST))

    random.shuffle(temp)
    generated_password = ''.join(temp)
    return generated_password


create_database()
password = get_password(int(password_len))
insert_data(website, username, password, notes)
print("done")
