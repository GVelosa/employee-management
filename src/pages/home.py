import flet as ft

from components.card import content_card

def home_view(page: ft.Page):

    async def to_register(e):
        await page.push_route("/create_employee")

    async def to_overview(e):
        await page.push_route("/overview")

    async def to_create_departments(e):
        await page.push_route("/create_departments")

    async def to_create_job_title(e):
        await page.push_route("/create_job_title")

    home_page = ft.Container(
        content=ft.Column(controls=[ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                content_card("Register","Register a new employee", to_register),
                content_card("Overview","Overview of all registered employees", to_overview),
            ]
        ),
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                content_card("Create Departments","Create a New Department", to_create_departments),
                content_card("Create Job Title","Create a New Job Title", to_create_job_title),
            ]
        )]
    ))
    return home_page