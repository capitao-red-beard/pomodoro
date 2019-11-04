from pomodoro import Pomodoro


def run(new):
    while True:
        if new == False:
            p = load_pomodoro()
            new = True

        show_commands()
        choice = input('\nWhat would you like to do? ')

        if choice == 'a':
            if not p:
                p = Pomodoro()

            while True:
                task = input('\nTask: ')
                p.add_task({"task": task, "complete": False})
                response = input('\nWould you like to add another task? ')

                if response == 'n':
                    break

        elif choice == 'r':
            try:
                p.check_tasks()
                to_remove = input('\nPlease select a task to remove: ')
                p.remove_task(int(to_remove))

            except UnboundLocalError:
                print('\nYou have not loaded or created a pomodoro session, so no tasks can be deleted')
        
        elif choice == 's':
            filename = input('\nPlease enter a name for your save: ')
            p.save_tasks(filename=filename)
        
        elif choice == 'p':
            p.check_tasks()
        
        elif choice == 'b':
            # TODO: add the running of a pomodoro
            p.begin_pomodoro()

        else:
            break

def load_pomodoro():
    Pomodoro.show_saved_pomodoros()
    choice = input('\nPlease select a pomodoro to load: ')
    p = Pomodoro(Pomodoro.load_pomodoro(choice))
    return p

def show_commands():
    print('\n[p]rint all pomodoro tasks to terminal')
    print('[a]dd a new task to your pomodoro session')
    print('[r]emove a task from your pomodoro session')
    print('[s]ave pomodoro session to disk')
    print('[b]egin the pomodoro session')
    print('[q]uit to the main menu')
