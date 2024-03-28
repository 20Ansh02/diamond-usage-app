import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('diamonds.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''CREATE TABLE IF NOT EXISTS diamonds
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                size REAL,
                status TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS necklace_designs
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                size REAL,
                quantity INTEGER)''')

# Insert sample data into diamonds table
sample_diamonds = [
    (0.5, 'new'),
    (0.75, 'returned'),
    (1.0, 'new'),
    (1.25, 'new'),
    (1.5, 'returned')
]

cursor.executemany('INSERT INTO diamonds (size, status) VALUES (?, ?)', sample_diamonds)

# Insert sample data into necklace_designs table
sample_necklace_designs = [
    ('Simple Necklace', 0.5, 1),
    ('Simple Necklace', 1.0, 2),
    ('Fancy Necklace', 0.75, 3),
    ('Fancy Necklace', 1.0, 1)
]

cursor.executemany('INSERT INTO necklace_designs (name, size, quantity) VALUES (?, ?, ?)', sample_necklace_designs)

# Commit changes and close connection
conn.commit()
conn.close()
