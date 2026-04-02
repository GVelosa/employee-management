import sqlite3

from database.db import get_connection

conection = get_connection()
cursor = conection.cursor()

def create_user(username, user_email, user_pass):
    cursor.execute("""INSERT INTO users
                   (username, user_email, user_password) VALUES
                   (?,?,?)""", (username, user_email, user_pass))

    conection.commit()

def consute_user():
    cursor.execute("""SELECT * FROM users""")
    users_account = cursor.fetchall()
    return users_account

def consult_manager():
    cursor.execute("""SELECT name, manager_id FROM employees
                   WHERE is_manager == 1""")
    managers_ids = cursor.fetchall()
    return managers_ids

def create_department(title, manager_id=None):
    cursor.execute("""INSERT INTO departments
                   (title, manager_id) VALUES
                   (?,?)""", (title, manager_id))
    conection.commit()
    
def consult_department():
    cursor.execute("""SELECT id, title FROM departments""")
    department_ids = cursor.fetchall()
    return department_ids

def create_jobs_title(title):
    cursor.execute("""INSERT INTO job_titles
                   (title) VALUES
                   (?)""", (title,))
    conection.commit()
    
def consult_job_title():
    cursor.execute("""SELECT * FROM job_titles""")
    job_title_ids = cursor.fetchall()
    return job_title_ids

def create_employee(name, employee_code, job_title_id, department_id, is_manager, manager_id, salary, hire_date, performance_score, employment_type, created_at):
    cursor.execute("""INSERT INTO employees
                   (name, employee_code, job_title_id, department_id, is_manager, manager_id, salary, hire_date, performance_score, employment_type, created_at) VALUES
                   (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (name, employee_code, job_title_id, department_id, is_manager, manager_id, salary, hire_date, performance_score, employment_type, created_at))
    conection.commit()