# Contact Book Application

This is a simple contact management application built with Python and Flet.

## Project Overview

The Contact Book Application allows users to:
- Add contacts with name, phone, and email information
- View all contacts in a list
- Edit existing contacts
- Delete contacts

## Project Structure

```
contact_book_app/
├── assets/            # Folder for application assets
├── database.py        # Database interaction layer (SQLite)
├── app_logic.py       # Application logic connecting UI and database
└── main.py            # Main UI components and application entry point
```

## Setup Instructions

### Prerequisites

- Python 3.6 or higher
- Flet library

### Installation

1. Install Python from [python.org](https://python.org) if not already installed.

2. Install the required packages:
   ```
   pip install flet
   ```

## Running the Application

Navigate to the contact_book_app directory and run the application:

```bash
cd contact_book_app
```

Choose one of these commands based on your testing needs:

- For Windows desktop testing:
  ```
  flet run
  ```

- For mobile testing:
  ```
  flet run --android
  ```

- For web testing:
  ```
  flet run --android
  ```

## Application Features

- **Add Contacts**: Enter name, phone, and email details to add a new contact
- **View Contacts**: All contacts are displayed in a scrollable list
- **Edit Contacts**: Modify contact information through an edit dialog
- **Delete Contacts**: Remove contacts from the database

## Additional Learning Tasks

Here are some challenges to enhance the application:

1. **Input Validation**:
   - Prevent empty name submissions
   - Add error messages for invalid inputs

2. **Delete Confirmation**:
   - Show a confirmation dialog before deleting a contact

3. **Search Functionality**:
   - Add a search field to filter contacts by name

4. **Dark Mode Toggle**:
   - Implement a light/dark theme switch using `page.theme_mode`

5. **UI Enhancement**:
   - Replace ListTiles with Cards for a more modern look
   - Add icons for phone and email information
