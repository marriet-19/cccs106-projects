import flet as ft
import mysql.connector
from db_connection import connect_db

async def main(page: ft.Page):
    # Configure page properties
    page.window.center()  # Corrected method
    page.window.frameless = True
    page.title = "User Login"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window.height = 350
    page.window.width = 400
    page.bgcolor = "amber"

    # Create UI controls
    title = ft.Text(
        "User Login",
        text_align=ft.TextAlign.CENTER,
        size=20,
        weight=ft.FontWeight.BOLD,
        font_family="Arial"
    )

    username = ft.TextField(
        label="User name",
        hint_text="Enter your user name",
        helper_text="This is your unique identifier",
        width=300,
        autofocus=True,
        prefix_icon="person",
        bgcolor="light blue"
    )

    password = ft.TextField(
        label="Password",
        hint_text="Enter your password",
        helper_text="This is your secret key",
        width=300,
        password=True,
        can_reveal_password=True,
        prefix_icon="password",
        bgcolor="light blue"
    )

    async def login_click(e):
        # Define dialog close handlers
        def close_dialog(e):
            e.control.open = False
            page.update()
        
        # Create dialogs for feedback
        success_dialog = ft.AlertDialog(
            title=ft.Text("Login Successful"),
            content=ft.Text(f"Welcome, {username.value}!", text_align=ft.TextAlign.CENTER),
            actions=[ft.TextButton("OK", on_click=close_dialog)],
            actions_alignment=ft.MainAxisAlignment.CENTER,
            icon=ft.Icon("check_circle", color="green")
        )

        failure_dialog = ft.AlertDialog(
            title=ft.Text("Login Failed"),
            content=ft.Text("Invalid username or password", text_align=ft.TextAlign.CENTER),
            actions=[ft.TextButton("OK", on_click=close_dialog)],
            actions_alignment=ft.MainAxisAlignment.CENTER,
            icon=ft.Icon("error", color="red")
        )

        invalid_input_dialog = ft.AlertDialog(
            title=ft.Text("Input Error"),
            content=ft.Text("Please enter username and password", text_align=ft.TextAlign.CENTER),
            actions=[ft.TextButton("OK", on_click=close_dialog)],
            actions_alignment=ft.MainAxisAlignment.CENTER,
            icon=ft.Icon("info", color="blue")
        )

        database_error_dialog = ft.AlertDialog(
            title=ft.Text("Database Error"),
            content=ft.Text("An error occurred while connecting to the database", text_align=ft.TextAlign.CENTER),
            actions=[ft.TextButton("OK", on_click=close_dialog)],
            actions_alignment=ft.MainAxisAlignment.CENTER,
            icon=ft.Icon("error", color="red")
        )

        # Validation and Database Logic
        if not username.value or not password.value:
            page.dialog = invalid_input_dialog
            invalid_input_dialog.open = True
            await page.update_async()
            return

        try:
            # Establish database connection
            connection = connect_db()
            if not connection:
                page.dialog = database_error_dialog
                database_error_dialog.open = True
                await page.update_async()
                return

            # Create cursor and execute query
            cursor = connection.cursor()
            
            # Use parameterized query to prevent SQL injection
            query = "SELECT * FROM users WHERE username = %s AND password = %s"
            cursor.execute(query, (username.value, password.value))
            
            # Fetch result
            result = cursor.fetchone()
            
            # Close database connection
            cursor.close()
            connection.close()
            
            # Show appropriate dialog based on result
            if result:
                page.dialog = success_dialog
                success_dialog.open = True
            else:
                page.dialog = failure_dialog
                failure_dialog.open = True
                
            await page.update_async()
            
        except mysql.connector.Error:
            page.dialog = database_error_dialog
            database_error_dialog.open = True
            await page.update_async()

    # Create login button
    login_button = ft.ElevatedButton(
        text="Login",
        on_click=login_click,
        width=100,
        icon="login"
    )

    # Arrange controls and add to page
    page.add(
        ft.Container(
            content=ft.Column(
                [
                    title,
                    ft.Container(height=20),
                    username,
                    password,
                    ft.Container(
                        content=login_button,
                        alignment=ft.alignment.center_right,
                        padding=ft.padding.only(top=10)
                    )
                ],
                spacing=10,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            padding=ft.padding.all(20)
        )
    )

# Start the Flet app
ft.app(target=main)
