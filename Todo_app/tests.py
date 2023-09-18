from django.test import TestCase
import sqlite3

# from todo import views

# connecting to the database
connection = sqlite3.connect("database.db", check_same_thread=False)
# make a sql object
cursor = connection.cursor()
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS Tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT)
    """
)

has_run_once = False


def populate():
    global has_run_once
    personal_todo_list = [
        "Buy groceries",
        "Schedule a dentist appointment",
        "Pay rent",
        "Go for a 30-minute jog",
        "Read a chapter of your book",
        "Call mom",
        "Clean the kitchen",
        "Plan a weekend trip",
        "Organize closet",
        "Watch the new episode of your favorite TV show",
    ]

    work_todo_list = [
        "Finish the quarterly report",
        "Send follow-up emails to clients",
        "Attend the team meeting at 2 PM",
        "Update the project timeline",
        "Review and approve expense reports",
        "Prepare presentation for the board meeting",
        "Research industry trends",
        "Complete the design mockup",
        "Submit the weekly progress report",
        "Collaborate with colleagues on the new project proposal",
    ]

    if not has_run_once:
        for items in personal_todo_list:
            sql = "INSERT INTO Tasks (task) VALUES (?)"
            cursor.execute(sql, (items,))
            connection.commit()
        for items in work_todo_list:
            sql = "INSERT INTO Tasks (task) VALUES (?)"
            cursor.execute(sql, (items,))
            connection.commit()
        has_run_once = True


def run_once(func):
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            func(*args, **kwargs)
            wrapper.has_run = True

    wrapper.has_run = False
    return wrapper


@run_once
def my_function():
    populate()


# test function to add task to the database
my_function()
