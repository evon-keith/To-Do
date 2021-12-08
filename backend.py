from sqlite3 import *
import sqlite3
from tkinter.constants import TRUE


def create_database():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('''create table if not exists tasklist (taskname varchar(50))''')
    connection.commit()
    connection.close

def insert_tasks(task):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO tasklist VALUES ('{0}')".format(task))
    connection.commit()
    connection.close()


def view():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    listoftasks=[]
    for row in cursor.execute('SELECT * FROM tasklist'):
        listoftasks.append(row[0])
    connection.commit()
    connection.close()
    return listoftasks


def delete(task):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM tasklist WHERE taskname = "{0}"'.format(task))
    connection.commit()
    connection.close()


create_database()

