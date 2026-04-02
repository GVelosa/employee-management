import flet as ft

from theme import colors

def appbar_create(page):
    async def to_home(e):
        await page.push_route("/home")

    home = ft.IconButton(icon=ft.Icons.HOME, icon_size=40, on_click=to_home)

    if page.route == "/home":
        lead = None
    else:
        lead = home

    appbar = ft.AppBar(
        leading=lead,
        title= page.route,
        automatically_imply_leading=False,
        center_title = True,
        color=colors.WHITE,
        bgcolor=colors.TANZINE,
    )
    return appbar