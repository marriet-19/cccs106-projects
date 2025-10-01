# main.py - With improvements
import flet as ft
from database import init_db
from app_logic import display_contacts, add_contact

def main(page):
    page.title = "Contact Book"
    page.window_width = 400
    page.window_height = 600
    page.padding = 20
    
    # Initialize database
    db_conn = init_db()
    
    # Dark mode toggle
    def toggle_theme(e):
        if page.theme_mode == "light":
            page.theme_mode = "dark"
            theme_button.icon = "light_mode"
        else:
            page.theme_mode = "light"
            theme_button.icon = "dark_mode"
        page.update()
    
    theme_button = ft.IconButton(
        icon="dark_mode",
        tooltip="Toggle theme",
        on_click=toggle_theme
    )
    
    # Search functionality
    def do_search(e):
        display_contacts(page, contacts_list_view, db_conn, search_term=search_field.value)
    
    search_field = ft.TextField(
        label="Search contacts",
        width=250,
        on_change=do_search
    )

    # Contact form
    name_input = ft.TextField(label="Name", width=350)
    phone_input = ft.TextField(label="Phone", width=350)
    email_input = ft.TextField(label="Email", width=350)
    
    inputs = (name_input, phone_input, email_input)
    contacts_list_view = ft.ListView(expand=True, spacing=10)

    # Form validation
    def validate_and_add(e):
        if not name_input.value:
            name_input.error_text = "Name cannot be empty"
            page.update()
            return
        name_input.error_text = None
        add_contact(page, inputs, contacts_list_view, db_conn)
    
    add_button = ft.ElevatedButton(
        text="Add Contact",
        on_click=validate_and_add
    )

    # Layout
    page.add(
        # Header with theme toggle
        ft.Row([
            ft.Text("Contact Book", size=30, weight="bold"),
            theme_button
        ], alignment="spaceBetween"),
        
        # Input form
        ft.Container(
            content=ft.Column([
                ft.Text("Enter Contact Details:"),
                name_input,
                phone_input,
                email_input,
                add_button,
            ]),
            padding=10,
            border_radius=10,
            border=ft.border.all(1, "blue"),
            margin=ft.margin.symmetric(vertical=10)
        ),
        
        # Search and contacts list
        ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Text("Contacts:", size=18, weight="bold"),
                    search_field
                ], alignment="spaceBetween"),
                contacts_list_view
            ]),
            padding=10,
            border_radius=10,
            border=ft.border.all(1, "blue"),
            expand=True
        )
    )

    display_contacts(page, contacts_list_view, db_conn)

if __name__ == "__main__":
    ft.app(target=main)