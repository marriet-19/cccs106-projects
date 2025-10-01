# User Login Application

A simple user login application using the Flet framework and MySQL database for authentication.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- MySQL Server
- Required Python packages (install using `pip install -r requirements.txt`):
  - Flet
  - MySQL Connector for Python

## Database Setup

1. Create a MySQL database named `fletapp`:
   ```sql
   CREATE DATABASE fletapp;
   ```

2. Create a users table:
   ```sql
   USE fletapp;
   CREATE TABLE users (
       id INT AUTO_INCREMENT PRIMARY KEY,
       username VARCHAR(255) NOT NULL UNIQUE,
       password VARCHAR(255) NOT NULL
   );
   ```

3. Insert sample user data:
   ```sql
   INSERT INTO users (username, password) VALUES ('testuser', 'password123');
   ```

## Configuration

Update the database connection parameters in `src/db_connection.py` if necessary:
- host: "localhost"
- user: "root"
- password: "admin123" (replace with your actual MySQL root password)
- database: "fletapp"

## Running the Application

1. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

2. Run the application:
   ```
   cd src
   flet run main.py
   ```

## Expected Output

- A small, frameless window with an amber background
- "User Login" title, fields for username and password, and a "Login" button
- Different dialogs based on login success, failure, or errors

### Test Credentials
- Username: testuser
- Password: password123
