import program_pomodoro


def main():
    try:
        while True:
            if find_user_intent() == 'run_new':
                program_pomodoro.run(new=True)
            elif find_user_intent() == 'run_load':
                program_pomodoro.run(new=False)
            else:
                break
    except KeyboardInterrupt:
        return


def find_user_intent():
    print('[n] Create a new pomodoro session')
    print('[l]oad a pomodoro session from disk')

    choice = input('What would you like to do: ')

    if choice == 'n':
        return 'run_new'
    
    elif choice == 'l':
        return 'run_load'
    else:
        return 'exit'


if __name__ == '__main__':
    main()