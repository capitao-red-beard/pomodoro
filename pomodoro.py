import json
import os
from time import time, sleep
import sys
from threading import Timer


'''
task_list = [
    {"name": "clean dishes", "complete": False}
    {"name": "hoover floor", "complete": False}
]
'''


class Pomodoro:
    def __init__(self, tasks=[], status=False):
        self.tasks = tasks
        self.status = status

    def add_task(self, task):
        self.tasks.append(task)
    
    def remove_task(self, task):
        del self.tasks[task]

    def check_tasks(self):
        print('\n')
        for i, t in enumerate(self.tasks):
            print(f'[{i}]: {t}')
    
    def save_tasks(self, filename):
        with open(f'tasks/{filename}.json', 'w', encoding='utf-8') as f:
            json.dump(self.tasks, f, ensure_ascii=False, indent=4)

    @staticmethod
    def show_saved_pomodoros():
        print('\n')
        for i, f in enumerate(os.listdir('tasks/')):
            if os.path.isfile(os.path.join('tasks/', f)):
                print(f'- {f[:-5]}')
    
    @staticmethod
    def load_pomodoro(pomodoro):
        try:
            with open(f'tasks/{pomodoro}.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print('File does not exist')
    
    def mark_task_complete(self, task):
        self.tasks[task]['complete'] = True

    def begin_timer():
        timer = Timer(1500, self.break_prompt())

    
    def begin_pomodoro():
        # TODO: implement the function 
        self.status = True

    def break_prompt():
        pause = input('\nHow long will your break be? ')
        