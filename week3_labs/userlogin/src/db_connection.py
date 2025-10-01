import mysql.connector

def connect_db():
    """
    Connect to the MySQL database with the specified parameters.
    Returns a mysql.connector connection object.
    """
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin123",  # IMPORTANT: Replace with your actual MySQL root password
            database="fletapp"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to database: {err}")
        return None
