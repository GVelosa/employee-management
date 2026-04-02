import flet as ft

from components.genericButton import genericButton 
from components.genericTextField import genericTextField
from components.info_fields import info_fields

from database.operations import create_user

from theme import colors

def signup_view(page: ft.Page):
    async def to_login(e):
        await page.push_route("/")

    
    def user_create(e):
        name = user_name.value
        email = user_email.value
        password = user_pass.value

        if not all([
            user_name.value,
            user_email.value,
            user_pass.value,
            confirm_pass.value
        ]):
            confirm_text.value = "Missing information!"
            return
        if user_pass.value != confirm_pass.value:
            confirm_text.value = "Passwords do not match!"
            return
        if "@" not in user_email.value:
            confirm_text.value = "Invalid email!"
            return
        
        create_user(name, email, password)
        confirm_text.value = "Account Created! You Can Now Login!"
        confirm_text.color=colors.ACCEPTED
        user_name.value = ""
        user_email.value = ""
        user_pass.value = ""
        confirm_pass.value = ""
        page.update()

    user_name = genericTextField("Enter Username")
    user_email = genericTextField("Enter Email",)
    user_pass = genericTextField("Create Password", "", True, True)
    confirm_pass = genericTextField("Confirm Password", "", True, True)
    signup_button = genericButton("SignUp", user_create)
    login_button = genericButton("Alredy has an acconut?", to_login)
    confirm_text = ft.Text(value="", color=colors.DENIED)
    buttons_row = ft.Row(
                    alignment = ft.MainAxisAlignment.CENTER,
                    controls=[
                        signup_button, login_button
                    ]
                )

    signup_page = info_fields([
                    user_name, user_email, user_pass, confirm_pass, buttons_row, confirm_text
                ], 1
        )
    
    
    return signup_page