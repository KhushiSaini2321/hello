def task():
    tasks = []#empty list
    print("-----------welcome----------")
total_tasks = int(input("enter how many tasks you went to add = "))
for i in range(1, total_tasks+1):
    tasks_name = input(f"enter task({i}) ")
    tasks.append = [tasks_name]
    print(f"todays tasks are \n {tasks_name}")
while True:
    operation = int(input("enter 1. add \n 2.update \n, 3. delete \n, 4. view \n, 5. exit\n"))
    if operation == 1:
        add = input("enter task you went to add = ")
        task.append(add)
        print(f"task{add} has been succesfully added....")
    elif operation == 2:
        updated_val = input("enter the task name you want to updatee = ")
        if updated_val in task:
            up = input("enter the task")
            ind = up(updated_val)
            task[ind] = up
            print(f"uodated task {up}")
    elif operation == 3:
        del_val = input("which task you went to delete = ")
        if del_val in task:
            ind = task.index(del_val)
            del task[ind]
            print(f"task{del_val} has been deleted ")
    elif operation == 4:
        print(f" total tasks = {task}")
    elif operation == 5:
        print("closing the program")
        break
    else:
        print("invalid input")
