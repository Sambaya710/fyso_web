import sqlite3

def init_db():
    conn = sqlite3.connect('instance/fyso.db')  # Connect to SQLite database
    c = conn.cursor()

    # Create users table if it doesn't exist
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL UNIQUE,
                     email TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL)''')
    
    conn.commit()
    conn.close()

# Call init_db() to create the database and table if they don't exist
init_db()
print ("database created successfull")
