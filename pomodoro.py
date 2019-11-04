import json
import os
from time import time, sleep
import sys

'''
task_list = [
    {"name": "clean dishes", "complete": False}
    {"name": "hoover floor", "complete": False}
]
'''

class Pomodoro:
    def __init__(self, tasks = []):
        self.tasks = tasks

    def add_task(self, task):
        self.tasks.append(task)
    
    def remove_task(self, task):
        del self.tasks[task]

    def check_tasks(self):
        for i, t in enumerate(self.tasks):
            print(f'[{i}]: {t}')
    
    def save_tasks(self, filename):
        with open(f'tasks/{filename}.json', 'w', encoding='utf-8') as f:
            json.dump(self.tasks, f, ensure_ascii=False, indent=4)

    @staticmethod
    def show_saved_pomodoros():
        for i, f in enumerate(os.listdir('tasks/')):
            if os.path.isfile(os.path.join('tasks/', f)):
                print(f'[{i}]: {f}')
    
    @staticmethod
    def load_pomodoro(pomodoro):
        try:
            with open(f'tasks/{pomodoro}.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print('File does not exist')
    
    def start_timer(self):
        start_time = int(time())
        end_time = start_time + 1500
        difference = end_time - start_time
        while True:
            difference -= 1
            if difference == 0:
                break
            sys.stdout.write("\r")
            sys.stdout.write("{:2d} seconds remaining".format(difference)) 
            sys.stdout.flush()
            sleep(1)
    
    def mark_task_complete(self, task):
        self.tasks[task]['complete'] = True
