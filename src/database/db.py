import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "database.db")

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    conection = get_connection()
    cursor = conection.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS users
                   (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   username TEXT NOT NULL,
                   user_email TEXT UNIQUE NOT NULL,
                   user_password TEXT NOT NULL)""")
                    #Password has to be a hash (bcrypt)
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS job_titles
                   (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   title TEXT UNIQUE NOT NULL)""")
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS departments
                   (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   title TEXT UNIQUE NOT NULL,
                   manager_id INTEGER,
                   FOREIGN KEY (manager_id) REFERENCES employees(id))""")
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS employees
                   (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   employee_code INTEGER UNIQUE NOT NULL,
                   job_title_id INTEGER NOT NULL,
                   department_id INTEGER NOT NULL,
                   is_manager INTEGER NOT NULL CHECK (is_manager IN (0, 1)),
                   manager_id INTEGER,
                   salary DECIMAL(19, 4) NOT NULL,
                   hire_date TEXT NOT NULL,
                   performance_score REAL,
                   status TEXT DEFAULT 'active',
                   employment_type TEXT NOT NULL,
                   created_at TEXT,
                   FOREIGN KEY (manager_id) REFERENCES employees(id),
                   FOREIGN KEY (department_id) REFERENCES departments(id), 
                   FOREIGN KEY (job_title_id) REFERENCES job_titles(id))""")
    
    conection.commit()