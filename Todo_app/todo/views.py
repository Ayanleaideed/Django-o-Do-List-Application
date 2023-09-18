from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
import sqlite3

# connecting to the database
connection = sqlite3.connect("database.db", check_same_thread=False)
# make a sql object
cursor = connection.cursor()
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS Tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT)
    """
)


# Create your views here.
def index(request):
    if request.method == "POST":
        cursor.execute("DELETE FROM Tasks")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='Tasks'")
    cursor.execute("UPDATE SQLITE_SEQUENCE SET seq = 0 WHERE name='Tasks'")
    connection.commit()
    cursor.execute("VACUUM")
    # Retrieve tasks from the database
    cursor.execute("SELECT * FROM Tasks")
    tasks = cursor.fetchall()

    # Convert the cursor result to a list of tasks
    tasks = [task[1] for task in tasks]

    return render(request, "todo/index.html", {"tasks": tasks})


# add task method
def add(request):
    if request.method == "POST":
        new_task = request.POST.get("newTask")
        if new_task:
            sql = "INSERT INTO Tasks (task) VALUES (?)"
            cursor.execute(sql, (new_task,))
            connection.commit()
            return HttpResponseRedirect(reverse("index"))
    return render(request, "todo/add.html")


def delete(request):
    if request.method == "POST":
        delete_task = request.POST.get("deleteTask")
        if delete_task:  # Check if a value is provided
            if delete_task.isdigit():  # Check if it's a valid integer (ID)
                sql_id = "DELETE FROM Tasks WHERE id = ?"
                cursor.execute(sql_id, (delete_task,))
                connection.commit()
            else:  # Assume it's a task name
                sql = "DELETE FROM Tasks WHERE task = ?"
                cursor.execute(sql, (delete_task,))
                connection.commit()

        cursor.execute("DELETE FROM sqlite_sequence WHERE name='Tasks'")
        cursor.execute("UPDATE SQLITE_SEQUENCE SET seq = 0 WHERE name='Tasks'")
        connection.commit()
        cursor.execute("VACUUM")

        return HttpResponseRedirect(reverse("index"))

    return render(request, "todo/delete.html")
