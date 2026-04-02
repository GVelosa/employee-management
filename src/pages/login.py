import flet as ft

from components.genericButton import genericButton 
from components.genericTextField import genericTextField
from components.info_fields import info_fields

from database.operations import consute_user

def login_view(page: ft.Page):
    users_account = consute_user()
    async def login_call():
        for conta in users_account:
            id, username, user_email, password = conta
            if username == user_login.value or user_email == user_login.value:
                if password == user_pass.value:
                    await page.push_route("/home")
                    break

        user_pass.value = ""
        confirm_text.value = "Wrong Login Informations!"
        page.update()
        

    async def to_signup(e):
        await page.push_route("/signup")

    

    user_login = genericTextField("Enter Username/Email")
    user_pass = genericTextField("Password", "", True, True)
    login_button = genericButton("Login", login_call)
    signup_button = genericButton("Don't have an acconut?", to_signup)
    confirm_text = ft.Text(value="", color=ft.Colors.RED)
    buttons = ft.Row(
                    alignment = ft.MainAxisAlignment.CENTER, 
                    controls=[
                        login_button, signup_button
                    ]
                )
    
    login_page = info_fields([
                user_login, user_pass, buttons, confirm_text
            ]
        , 1)
    
    return login_page