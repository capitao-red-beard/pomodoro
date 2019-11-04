import program_pomodoro


def main():
    try:
        while True:
            print('\n[n]ew pomodoro session')
            print('[l]oad a pomodoro session from disk')
            print('[q]uit the program \n')
            choice = input("Please input what you'd like to do: ")

            if choice == 'n':
                program_pomodoro.run(new=True)
            elif choice == 'l':
                program_pomodoro.run(new=False)
            elif choice == 'q':
                break
            else:
                print('\nPlease input a correct value from the list')
    except KeyboardInterrupt:
        return

if __name__ == '__main__':
    main()