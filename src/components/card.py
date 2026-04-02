import flet as ft

def content_card(name, description, on_click):

    return ft.Card(
        content=ft.GestureDetector(
            on_tap=on_click,
            mouse_cursor = ft.MouseCursor.CLICK,
            content=ft.Container(
                padding=16,
                content=ft.Column(
                    controls=[
                        ft.Icon(ft.Icons.ABC, size=45), 
                        ft.Divider(),
                                ft.Text(value=name, color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD, size=18),
                                ft.Text(value=description, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE_70, size=14),
                            ]   
                        )
                )
            )
        )
        
