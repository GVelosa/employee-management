import flet as ft
import random
from datetime import datetime

from components.genericButton import genericButton 
from components.genericTextField import genericTextField
from components.info_fields import info_fields

from database.operations import consult_job_title,create_employee, consult_department

jobs_titles = consult_job_title()
departmet = consult_department()

def create_employee_view(page: ft.Page):

    def job_title_options():
        if jobs_titles:
            return [ft.DropdownOption(key=id, text=title) for id, title in jobs_titles]
        else:
            return None
        
    def department_options():
        if departmet:
            return [ft.DropdownOption(key=id, text=title) for id, title in departmet]
        else:
            return None

    def create():
        employee_code = random.randint(10000, 99999)
        manager_id = random.randint(100, 999)
        create_employee(
            employee_name.value,
            employee_code,
            int(job_title_id.value),
            int(department_id.value),
            is_manager.value,
            manager_id if is_manager.value else None,
            float(salary.value),
            datetime.now().isoformat(),
            float(performance_score.value) if performance_score.value else None,
            employment_type.value,
            datetime.now().isoformat()
        )

    employee_name = genericTextField(label="Name")
    # employee_code = genericTextField(label="Employee Code")
    job_title_id = ft.Dropdown(label="Job Title", options=job_title_options())
    department_id = ft.Dropdown(label="Department", options=department_options())
    is_manager = ft.Switch(label="Is Manager?")
    # manager_id = genericTextField(label="Manager ID (optional)")
    salary = genericTextField(label="Salary")
    # hire_date = genericTextField(label="Hire Date (YYYY-MM-DD)")
    performance_score = genericTextField(label="Performance Score (optional)")
    # status = genericTextField(label="Employee Status")
    employment_type = genericTextField(label="Employment Type")

    create_button = genericButton("Create Employee", on_click=create)

    create_employee_view = info_fields([
            employee_name,
            job_title_id,
            department_id,
            is_manager,
            salary,
            # hire_date,
            performance_score,
            # status,
            employment_type,
            create_button
        ], 1
    )

    return create_employee_view