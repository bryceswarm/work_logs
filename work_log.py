# Project 3 for Team Treehouse
#
#
#
#
# Author: Bryce Swarm

import csv
import os

from task import Task


fields = [
    'id',
    'first_name',
    'last_name',
    'task_name',
    'time_elapsed',
    'notes',
    'date'
    ]

# clear the command screen
def clear_screen():
    """ Clears the command screen for next prompts to be displayed
        more efficiently."""
    os.system('cls' if os.name == 'nt' else 'clear')


def new_task():
    clear_screen()
    first_name = input('What is your first name?\n> ')
    clear_screen()
    last_name = input('What is your last name?\n> ')
    clear_screen()
    task_name = input('What is the task?\n> ')
    clear_screen()
    time_elapsed = input('How much time was spent on the task?\n> ')
    clear_screen()
    notes = input('Please enter any additional notes.\n> ')
    task = Task(first_name, last_name, task_name, time_elapsed, notes)
    task.save_entry()
    return task


def start():
    try:
        log_file = open("work_logs.csv", 'x')
        writer = csv.DictWriter(log_file, fieldnames=fields)
        writer.writeheader()
        input('Please enter a new task, press any key to begin.')
        task = new_task()
        clear_screen()
        print('Added Task!\n')
        print(task)
        input('\nPress any key to continue.')
    except FileExistsError:
        pass

def menu():
    while True:
        print('Please make a selection:')
        print('1: Search\n'
            '2: Log New Task\n'
            '3: Quit\n')
        menu_select = input('> ')
        if menu_select == '3':
            clear_screen()
            quit()
        elif menu_select == '2':
            clear_screen()
            task = new_task()
            print('Added Task!\n')
            print(task)
            input('\nPress any key to continue.')
        elif menu_select == '1':
            clear_screen()
            search_menu()
        else:
            clear_screen()
            print('That is not a valid selection.')
            continue

def search_menu():
    while True:
        print('How would you like to search?\n'
              '1: Exact Date\n'
              '2: Date Range\n'
              '3: Task Name\n'
              '4: Return to main menu')
        menu_select = input('> ')
        if menu_select == '1':
            pass
        if menu_select == '2':
            pass
        if menu_select == '3':
            pass
        if menu_select == '4':
            clear_screen()
            menu()




if __name__ == '__main__':
    start()
    menu()
