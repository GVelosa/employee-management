import flet as ft

from theme import colors

def genericTextField(label, hint = None, password = False, can_reveal = False):
    
    return ft.TextField(
        label=label,
        hint_text=hint,
        password=password, 
        can_reveal_password=can_reveal,
        border_color=colors.RAFTSMAN,
        focused_border_color=colors.RAFTSMAN,
        border_radius=10,
        border_width=2,
        focused_border_width=3,
        text_style=ft.TextStyle(color=colors.WHITE, size=18),
        label_style=ft.TextStyle(color=colors.WHITE),
    )