from curses import curs_set
from email.mime import base
import sqlite3 as sq
from components import bot

# Creation | Conection  to Database 
def sql_startup():
    global base, cur
    base = sq.connect("Database")
    cur = base.cursor()
    if base:
        print("Conection to database successful")

    base.execute("CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT)")
    base.execute("CREATE TABLE IF NOT EXISTS admins(name TEXT PRIMARY KEY, id TEXT PRIMARY KEY, duties TEXT)")