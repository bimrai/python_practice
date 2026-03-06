def task_list():
    
    tasks = []
    
    while True:
        
        print("1. New Task")
        print("2. Delete Task")
        print("3. All Tasks")
        print("4. Quit Tasks")
        print("----------------")
        option = input("Select Option: ")
        
        if option == "1":
            
            task = input("Task: ")
            tasks.append(task)
            
        elif option == "2":
            task = input("Select Task Number To Delete: ")
            if task in tasks:
                task.remove(task)
            else:
                print("Task Does Not Exist")
        elif option == "3":
            print("All Tasks: ")
            for task in tasks:
                print("- " + task)
        elif option == "4":
            break
        else:
            print("Invalid Option.")
        
        
task_list()