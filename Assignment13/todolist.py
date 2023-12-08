"""
### Implementation:

1. **To-Do List Operations**:
    - **Add Task**:
        - Allow users to add tasks to the to-do list.
        - Prompt users to input the task they want to add.
        - Display a confirmation message upon successful addition.
    - **Remove Task**:
        - Permit users to remove tasks by their index in the list.
        - Users input the index of the task they want to remove.
        - Validate the index and remove the specified task.
        - Provide appropriate messages for successful or invalid removal attempts.
    - **View List**:
        - Display the current list of tasks with their corresponding indices.
        - Inform users if the list is empty.
    - **Exit Program**:
        - Allow users to exit the program.
2. **Menu Interface**:
    - Create an interactive menu to facilitate user operations.
    - Continuously prompt users to select an option until they choose to exit.
3. **Error Handling**:
    - Validate user inputs for indices to prevent errors.
    - Handle cases where users enter invalid indices or attempt to remove tasks from an empty list.
"""
organizer = [] # List to store tasks

def add_task():
    task = input("Add new task: ")
    organizer.append(task)
    print("New task added successfully! \n\n")
    
def remove_task(index):
    if len(organizer) == 0:
        print("Any task does not found in the to-do list")
        return
    
    index = int(input("Enter the index of the task you want to remove: "))
    if index < 0 or index >= len(organizer):
        print(f"Invalid index {index}.")
        return
    
    organizer.pop(index)
    print("Selected task removed from the to-do list!")

def view_list():
    if len(organizer) == 0:
        print("No task in the list")
        return
    else:
        print("To-do list includes: ") 
        for index, task in enumerate(organizer):
            print(f"{index}: {task}")

while True:
    type = input(("Wellcome to the TO-DO LIST!  \n1 Add task \n2 Remove task \n3 View list \n4 Exit program \n\nChoose the option: "))

    if type == '1':
        add_task()
    elif type == '2':
        remove_task()
    elif type == '3':
        view_list()
    if type == '4':
        print('Bye, have a nice day! :)\n\n')
        break

