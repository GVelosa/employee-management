import flet as ft

from components.genericButton import genericButton 
from components.genericTextField import genericTextField
from components.info_fields import info_fields

from database.operations import create_department, consult_manager

def create_departments_view(page: ft.Page):
    managers_infos = consult_manager()
    
    def manager_options():
        if managers_infos:
            return [ft.DropdownOption(key=id, text=managers) for managers, id in managers_infos]
        else:
            return None

    def on_click():
        create_department(title.value, manager.value)

    title = genericTextField(label="Dapartment Name")
    manager = ft.Dropdown(label="Department Manager", options=manager_options())
    create_button = genericButton("Create New Department", on_click=on_click)

    create_departments = info_fields([
                title, manager, create_button
            ], 2
        )

    return create_departments