import sqlite3

connection = sqlite3.connect('base.db')
cursor = connection.cursor()

def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')

def get_all_products():
    cursor.execute('SELECT  title, description, price FROM Products')
    products = cursor.fetchall()
    return products

initiate_db()

for i in range(1, 5):
    cursor.execute("INSERT INTO Products(title, description, price) VALUES(?,?,?)",
                   (f'Продукт{i}', f'Описание{i}', f'{i*100}'))


connection.commit()
#connection.close()