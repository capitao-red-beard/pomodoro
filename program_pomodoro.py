from pomodoro import Pomodoro


def run(new):
    while True:
        if new == False:
            load_pomodoro()
            new = True

        show_commands()
        choice = input('What would you like to do? ')

        if choice == 'a':
            if not p:
                p = Pomodoro()
            else:
                load_pomodoro()

            while True:
                task = input('Task: ')
                p.add_task({"task": task, "complete": False})
                response = input('Would you like to add another task? ')

                if response == 'n':
                    break

        elif choice == 'r':
            try:
                print(p.check_tasks())
                to_remove = input('Please select a task to remove: ')
                p.remove_task(int(to_remove))

            except UnboundLocalError:
                print('You have not loaded a pomodoro session, so no tasks can be deleted')
        
        elif choice == 's':
            filename = input('Please enter a name for your save: ')
            p.save_tasks(filename=filename)
        
        elif choice == 'p':
            print(p.check_tasks())
        
        elif choice == 'b':
            p.start_timer()

        else:
            break

def load_pomodoro():
    print(Pomodoro.show_saved_pomodoros())
    choice = input('Please select a pomodoro to load: ')
    p = Pomodoro(Pomodoro.load_pomodoro(choice))

def show_commands():
    print('[p]rint all pomodoro tasks to terminal')
    print('[a]dd a new task to your pomodoro session')
    print('[r]emove a task from your pomodoro session')
    print('[s]ave pomodoro session to disk')
    print('[b]egin the pomodoro session')
    print('[q]uit to the main menu')
