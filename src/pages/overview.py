import flet as ft

from components.genericButton import genericButton 

def overview_view(page: ft.Page):
    
    async def to_home(e):
        await page.push_route("/home")

    overview_page = ft.Column(
        controls=[
            ft.Text("Página de Overview"),
            ft.Button("Home", on_click=to_home)
        ]
    )
    
    return overview_page