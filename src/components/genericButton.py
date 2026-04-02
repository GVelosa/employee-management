import flet as ft

from theme import colors

def genericButton(name, on_click):
    return ft.Button(
        content=name,
        on_click=on_click,
        style=ft.ButtonStyle(
        color=colors.WHITE,
        bgcolor=colors.RAFTSMAN,          
        elevation=10,               
        overlay_color=colors.DIVA_VIOLET,   
    )
    )