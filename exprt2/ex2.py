


HELP = """
help - справка
add - добавить задачу
show - напечатать список задач
exit - exit
"""
taskss = []

today = []
tomorrow = []
other = []

run = True
while run:

    command = input("""
    Введите команду: """)
    if command == "help":
        print(HELP)
    elif command == "show":
        day = input("Выберите день: ")
        if day == "t":
            print(today)
        elif day == "tom":
            print(tomorrow)
        elif day == "qq":
            print(other)
    elif command == "add":
        day = input("Выберите день: ")
        if day == "t":
            taskss1 = input("Введите задачу ")
            taskss.append(taskss1)
            today.append(taskss1)
        elif day == "tom":
            taskss1 = input("Введите задачу ")
            taskss.append(taskss1)
            tomorrow.append(taskss1)
        elif day == "qq":
            taskss1 = input("Введите задачу ")
            taskss.append(taskss1)
            other.append(taskss1)
    elif command == "exit":
        print("вы закрыли программу")
        break
    else:
        print("Неизвестная команда")
        print("exit")
        run = False 
        # или команда break 