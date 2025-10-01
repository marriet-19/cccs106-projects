# app_logic.py - With improvements
import flet as ft
from database import update_contact_db, delete_contact_db, add_contact_db, get_all_contacts_db

def display_contacts(page, contacts_list_view, db_conn, search_term=None):
    """Fetches and displays all contacts in the ListView."""
    contacts_list_view.controls.clear()
    
    if search_term:
        # Search contacts by name
        cursor = db_conn.cursor()
        cursor.execute(
            "SELECT id, name, phone, email FROM contacts WHERE name LIKE ?", 
            (f"%{search_term}%",)
        )
        contacts = cursor.fetchall()
    else:
        contacts = get_all_contacts_db(db_conn)
    
    if not contacts:
        message = "No contacts found" if search_term else "Your contact list is empty"
        contacts_list_view.controls.append(
            ft.Container(
                content=ft.Text(message, italic=True),
                alignment="center",
                padding=20
            )
        )
    
    for contact in contacts:
        contact_id, name, phone, email = contact
        
        # Card-based UI
        card = ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.ListTile(
                        leading=ft.CircleAvatar(content=ft.Text(name[0].upper() if name else "?")),
                        title=ft.Text(name, weight="bold"),
                        subtitle=ft.Column([
                            ft.Row([
                                ft.Icon("phone", size=16),
                                ft.Text(phone if phone else "No phone number")
                            ]),
                            ft.Row([
                                ft.Icon("email", size=16),
                                ft.Text(email if email else "No email address")
                            ])
                        ])
                    ),
                    ft.Row([
                        ft.TextButton("Edit", on_click=lambda e, c=contact: open_edit_dialog(page, c, db_conn, contacts_list_view)),
                        ft.TextButton("Delete", on_click=lambda e, cid=contact_id, n=name: show_delete_confirmation(page, cid, n, db_conn, contacts_list_view))
                    ], alignment="end")
                ]),
                padding=10
            )
        )
        
        contacts_list_view.controls.append(card)
    page.update()

def add_contact(page, inputs, contacts_list_view, db_conn):
    """Adds a new contact and refreshes the list."""
    name_input, phone_input, email_input = inputs
    add_contact_db(db_conn, name_input.value, phone_input.value, email_input.value)
    
    for field in inputs:
        field.value = ""
    
    page.snack_bar = ft.SnackBar(content=ft.Text("Contact added successfully!"))
    page.snack_bar.open = True
    
    display_contacts(page, contacts_list_view, db_conn)
    page.update()

def show_delete_confirmation(page, contact_id, name, db_conn, contacts_list_view):
    """Shows a confirmation dialog before deleting a contact."""
    def close_dlg(e):
        dialog.open = False
        page.update()
        
    def confirm_delete(e):
        dialog.open = False
        page.update()
        delete_contact_db(db_conn, contact_id)
        display_contacts(page, contacts_list_view, db_conn)
        page.snack_bar = ft.SnackBar(content=ft.Text("Contact deleted successfully!"))
        page.snack_bar.open = True
        page.update()
        
    dialog = ft.AlertDialog(
        title=ft.Text("Confirm Deletion"),
        content=ft.Text(f"Are you sure you want to delete '{name}' from your contacts?"),
        actions=[
            ft.TextButton("Cancel", on_click=close_dlg),
            ft.TextButton("Delete", on_click=confirm_delete)
        ]
    )
    
    page.dialog = dialog
    dialog.open = True
    page.update()

def open_edit_dialog(page, contact, db_conn, contacts_list_view):
    """Opens a dialog to edit a contact's details."""
    contact_id, name, phone, email = contact
    
    edit_name = ft.TextField(label="Name", value=name)
    edit_phone = ft.TextField(label="Phone", value=phone)
    edit_email = ft.TextField(label="Email", value=email)
    
    def close_dlg(e):
        dialog.open = False
        page.update()
        
    def save_changes(e):
        if not edit_name.value:
            edit_name.error_text = "Name cannot be empty"
            page.update()
            return
            
        update_contact_db(db_conn, contact_id, edit_name.value, edit_phone.value, edit_email.value)
        dialog.open = False
        page.update()
        
        display_contacts(page, contacts_list_view, db_conn)
        page.snack_bar = ft.SnackBar(content=ft.Text("Contact updated successfully!"))
        page.snack_bar.open = True
        page.update()
    
    dialog = ft.AlertDialog(
        title=ft.Text("Edit Contact"),
        content=ft.Column([edit_name, edit_phone, edit_email], spacing=10),
        actions=[
            ft.TextButton("Cancel", on_click=close_dlg),
            ft.TextButton("Save", on_click=save_changes)
        ]
    )
    
    page.dialog = dialog
    dialog.open = True
    page.update()