# Django To-Do List Application
![To-Do List Screenshot](screenshot.png)

## Description
This is a stylish and interactive To-Do List application built with Django, SQLite, HTML, JavaScript, and Bootstrap. It allows users to add, view, and delete tasks with ease.

## Features
- Add new tasks
- View all tasks
- Delete tasks

## Installation
1. Clone this repository: `git clone <repository-url>`
2. Navigate to the project directory: `cd <project-directory>`
3. Install the required packages: `pip install -r requirements.txt`
4. Apply database migrations: `python manage.py migrate`
5. Create a superuser to manage tasks: `python manage.py createsuperuser`
6. Run the server: `python manage.py runserver`

## Usage
- Access the application by navigating to `http://localhost:8000` in your web browser.
- To add a task, click the "Add Task" button, enter your task in the input field, and press "Add."
- To view all tasks, click the "Tasks" button in the navigation bar.
- To delete a task, click the "Delete" button next to the task on the "Tasks" page.

## Customization
You can customize the application further by modifying the HTML templates and CSS styles as needed in the project's `templates` and `static` directories.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is open-source and available under the [MIT License](https://choosealicense.com/licenses/mit/).
