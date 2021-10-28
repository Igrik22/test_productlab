import sqlite3 as sq


def start_db():
    global base, cur
    base = sq.connect('../bot/wildberries.db')
    cur = base.cursor()
    if base:
        print('successful connection ')
    base.execute('CREATE TABLE IF NOT EXISTS test(title BLOB, brand BLOB)')
    base.commit()


def sql_add_brand_and_title(title, brand):
    cur.execute('INSERT INTO test VALUES (?, ?)', (title, brand,))
    base.commit()























