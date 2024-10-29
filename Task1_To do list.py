import sys
todo_list = []
def display_menu():

    print("\nMENU:")
    print("1. Create new task")
    print("2. Update existing task")
    print("3. Track all tasks")
    print("4. Exit\n")
    option_no = 0
    while option_no not in [1, 2, 3, 4]:
        option_no = int(input("Please enter the option number(1/2/3): "))
    if option_no == 1:
        create_new_task()
    elif option_no == 2:
        update_existing_task()
    elif option_no == 3:
        track_all_tasks()
    else:
        sys.exit()


def create_new_task():
    new_task = input("To create new task enter the task name: ")
    todo_list.append(new_task)
    print("Successfully created new task",new_task)
    display_menu()

def track_all_tasks(show_menu=False):
    for i in range(len(todo_list)):
        print(str(i + 1) + ".", todo_list[i])
    if not show_menu:
        display_menu()


def update_existing_task():
    track_all_tasks(True)
    update_task_no = 0
    while not 0 < update_task_no <= len(todo_list):
        update_task_no = int(input("To update existing task, please enter the number: "))
    updated_task = input(f"Enter new data to update task number {update_task_no}: ")
    todo_list[update_task_no - 1] = updated_task
    print("Successfully updated existing task",update_task_no)
    display_menu()

display_menu()

