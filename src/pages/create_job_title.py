import flet as ft

from components.genericButton import genericButton 
from components.genericTextField import genericTextField
from components.info_fields import info_fields

from database.operations import create_jobs_title

def create_job_title_view(page: ft.Page):
    
    def create():
        create_jobs_title(title.value)

    title = genericTextField(label="Job Title")
    create_button = genericButton("Create New Job Title", on_click=create)
    create_job_title = info_fields([
            title, create_button
        ], 2
    )
    return create_job_title