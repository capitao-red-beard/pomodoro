import program_pomodoro


def main():
    try:
        while True:
            if find_user_intent() == 'new_pomodoro_session':
                program_pomodoro.run()
            else:
                break
    except KeyboardInterrupt:
        return


def find_user_intent():
    print('[n] Create a new pomodoro session')

    choice = input('What would you like to do: ')

    if choice == 'n':
        return 'new_pomodoro_session'
    else:
        return 'exit'


if __name__ == '__main__':
    main()