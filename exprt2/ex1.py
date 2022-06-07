


HELP = """
help - справка
add - добавить задачу
show - напечатать список задач
exit - exit
"""
taskss = []
run = True
while run:

    command = input("""
    Введите команду: """)
    if command == "help":
        print(HELP)
    elif command == "show":
        print(taskss)
    elif command == "add":
        taskss1 = input("Введите задачу")
        taskss.append(taskss1)
    elif command == "exit":
        print("вы закрыли программу")
        break
    else:
        print("Неизвестная команда")
        print("exit")
        run = False 
        # или команда break 
