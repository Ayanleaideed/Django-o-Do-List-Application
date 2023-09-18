//<!-- JavaScript to handle the delete button clicks -->

  // Get all delete buttons by class name
  const deleteButtons = document.querySelectorAll('.delete-button');

  // Add a click event listener to each delete button
  deleteButtons.forEach(button => {
    button.addEventListener('click', () => {
      const taskToDelete = button.getAttribute('data-task');

      // Set the deleteTask input field to the task name
      const deleteTaskInput = document.getElementById('deleteTaskInput');
      deleteTaskInput.value = taskToDelete;

      // Submit the delete task form
      const deleteTaskForm = document.getElementById('deleteTaskForm');
      deleteTaskForm.submit();
    });
  });
  // Get all Done buttons by class name
  const doneButtons = document.querySelectorAll('.Done-button');

  // Add a click event listener to each Done button
  doneButtons.forEach(button => {
    button.addEventListener('click', () => {
      // Get the parent element of the button (the table cell)
      const parentElement = button.parentElement;

      // Get the previous sibling of the parent (the task cell)
      const taskCell = parentElement.previousElementSibling;

      // Check if the task is already done
      if (taskCell.style.color === 'red') {
        // If the task is done, undo it
        taskCell.style.color = '';
        taskCell.style.textDecoration = '';
        button.innerText = "Done";
      } else {
        // If the task is not done, do it
        taskCell.style.color = 'red';
        taskCell.style.textDecoration = 'line-through';
        button.innerText = "Undone";
      }
    });
  });
