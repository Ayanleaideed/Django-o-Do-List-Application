import sqlite3

# Connect to the SQLite database
connection = sqlite3.connect("database.db")

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Select the highest ID value from the "Tasks" table
cursor.execute("SELECT MAX(id) FROM Tasks")
highest_id = cursor.fetchone()[0]

# Delete the row with the highest ID value
cursor.execute(f"DELETE FROM Tasks WHERE id = {highest_id}")

# Commit the changes to the database
connection.commit()

# Close the cursor and the database connection
cursor.close()
connection.close()
