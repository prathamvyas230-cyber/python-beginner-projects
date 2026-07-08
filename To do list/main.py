
tasks = []
def show_menu():
    print('\n--- TO-DO LIST ---')
    print('1. Add task')
    print('2. view task')
    print('3. Mark task as done')
    print('4. Delete task')
    print('5. Exit')

def add_task():
    task = input('Enter task: ')
    tasks.append({"Task": task, "Done": False})
    print(f'Task {task} Added')

def view_task():
    if not tasks:
        print('No task yet')
        return
    print('\n Your task:')
    for i, task in enumerate(tasks, start=1):
        status = "✅" if task["Done"] else "❌"
        print(f"{i} {task["Task"]} {status}")

def mark_as_done():
    view_task()
    try:
        if not tasks:
            print("No tasks yet")
            return
        index = int(input('Enter the task number you want to mark as done: ')) -1
        if 0<= index < len(tasks):
            tasks[index]["Done"] = True
            print('Your task is marked as done')
        else:
            print('Invalid number')
    except ValueError:
        print('Please select a valid number')
    
def delete_task():
    view_task()
    try:
        if not tasks:
            print('No task yet')
            return
        index = int(input('Enter index number of task you want to delete: '))-1
        if 0<= index < len(tasks):
            remove = tasks.pop(index)
            print(f'Task {index} {remove["Task"]} Deleted')
        else:
            print('Invalid number')
    except ValueError:
        print('Please chose the correct index number') 

def main():
    show_menu()
    while True:
        try:
            chose = int(input('Enter the number from between (1-5): '))
            if chose == 1:
                add_task()
            elif chose == 2:
                view_task()
            elif chose == 3:
                mark_as_done()
            elif chose == 4:
                delete_task()
            elif chose == 5:
                print('Thank you & GoodBye')
                break              

        except ValueError:
            print('Please Enter a valid number')

main()
