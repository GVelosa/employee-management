import flet as ft

from theme import colors

def info_fields(content, style_type = 1, side = None):
        
    if style_type == 1:
        match side:
            case "left":
                aligment = ft.CrossAxisAlignment.START
            case "right":
                aligment = ft.CrossAxisAlignment.END
            case "center":
                aligment = ft.CrossAxisAlignment.CENTER
            case _:
                aligment = None

        return ft.Column(
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=aligment,
            controls=[
                ft.Card(
                    expand=True,
                    width=750,
                    bgcolor=colors.TANZINE,
                    elevation=45,
                    content=ft.Container(
                        padding=20,
                        content=ft.Column(
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                            controls=content
                        )
                    )
                )
            ]
        )
    elif style_type == 2:
        return ft.Column(
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Card(
                    width=float("inf"),
                    bgcolor = colors.TANZINE,
                    elevation=45,
                    content=ft.Container(
                        padding=20,
                        content=ft.Column(
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                            controls=content
                        )
                    )
                )
    ]
)