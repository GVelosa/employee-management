import flet as ft

def genericButton(name, on_click):
    return ft.Button(
        content=name, on_click=on_click
    )