import flet as ft

from theme import colors

def content_card(name, description, on_click):

    return ft.Card(
        bgcolor=colors.PERKIN_MAUVE,
        content=ft.GestureDetector(
            on_tap=on_click,
            mouse_cursor = ft.MouseCursor.CLICK,
            content=ft.Container(
                width=300,
                padding=16,
                content=ft.Column(
                    controls=[
                            # ft.Icon(ft.Icons.ABC, size=45), 
                            # ft.Divider(),
                            ft.Text(value=name, color=colors.WHITE, weight=ft.FontWeight.BOLD, size=18),
                            ft.Text(value=description, weight=ft.FontWeight.BOLD, color=colors.GREY, size=14),
                            ]   
                        )
                )
            )
        )
        
