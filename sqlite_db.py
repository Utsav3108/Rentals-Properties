import sqlite3 
  
# filename to form database 
file = "Sqlite3.db"
  
try: 
    conn = sqlite3.connect(file) 
    print("Database Sqlite3.db formed.") 
    
    cursor = conn.cursor()
    
    # Create table
    cursor.execute('''CREATE TABLE IF NOT EXISTS user
                      (id INTEGER PRIMARY KEY,
                       name TEXT NOT NULL,
                       age INTEGER NOT NULL)''')
    
    # Insert data
    cursor.execute("INSERT INTO user (name, age) VALUES ('Alice', 30)")
    cursor.execute("INSERT INTO user (name, age) VALUES ('Bob', 25)")
    cursor.execute("INSERT INTO user (name, age) VALUES ('Charlie', 35)")
    
    # Commit the changes
    conn.commit()
    
except Exception as e: 
    print(f"An error occurred: {e}")
finally:
    conn.close()