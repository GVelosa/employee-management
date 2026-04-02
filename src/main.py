import flet as ft

from components.appbar import appbar_create

from pages.signup import signup_view
from pages.login import login_view
from pages.home import home_view
from pages.register_employees import create_employee_view
from pages.create_job_title import create_job_title_view
from pages.overview import overview_view
from pages.create_departments import create_departments_view
from pages.update_infos import update_page_view
from database.db import init_db
from theme import colors

init_db()

def main(page: ft.Page):
    page.title = "Staff Manager"
    
    def route_change():
        page.views.clear()
        page.views.append(
            ft.View(
                route="/",
                bgcolor=colors.WHITE,
                controls=[
                    login_view(page)
                ],
            )
        )

        if page.route == "/signup":
            page.views.append(
                ft.View(
                    align=ft.Alignment.CENTER,
                    route="/signup",
                    bgcolor=colors.WHITE,
                    controls=[
                        signup_view(page)
                    ],
                )
            )
        if page.route == "/home":
            page.views.append(
                ft.View(
                    appbar=appbar_create(page),
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    route="/home",
                    bgcolor=colors.WHITE,
                    controls=[
                        home_view(page)
                    ],
                )
            )
        if page.route == "/create_employee":
            page.views.append(
                ft.View(
                    appbar= appbar_create(page),
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    route="/create_employee",
                    bgcolor=colors.WHITE,
                    controls=[
                        create_employee_view(page)
                    ],
                )
            )
        if page.route == "/overview":
            page.views.append(
                ft.View(
                    appbar= appbar_create(page),
                    route="/overview",
                    bgcolor=colors.WHITE,
                    controls=[
                        overview_view(page)
                    ],
                )
            )

        if page.route == "/create_departments":
            page.views.append(
                ft.View(
                    appbar= appbar_create(page),
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    route="/create_departments",
                    bgcolor=colors.WHITE,
                    controls=[
                        create_departments_view(page)
                    ],
                )
            )

        if page.route == "/create_job_title":
            page.views.append(
                ft.View(
                    appbar= appbar_create(page),
                    route="/create_job_title",
                    bgcolor=colors.WHITE,
                    controls=[
                        create_job_title_view(page)
                    ],
                )
            )
        if page.route == "/update_infos":
            page.views.append(
                ft.View(
                    appbar= appbar_create(page),
                    route="/create_job_title",
                    bgcolor=colors.WHITE,
                    controls=[
                        update_page_view(page)
                    ],
                )
            )

        page.update()

    async def view_pop(e):
        if e.view is not None:
            print("View pop:", e.view)
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()

if __name__ == "__main__":
    ft.run(main)
