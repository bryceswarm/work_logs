# Project 3 for Team Treehouse
#
#
#
#
# Author: Bryce Swarm

import csv
import os
import datetime

from task import Task
from search import Search


time_format = ('%m/%d/%y')
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

# record new task submissions
def new_task():
    """ Prompts user and records each input for new task submissions """
    clear_screen()
    # input first name
    first_name = input('What is your first name?\n> ')
    clear_screen()
    # input last name
    last_name = input('What is your last name?\n> ')
    clear_screen()
    # input task
    task_name = input('What is the task?\n> ')
    clear_screen()
    # input time elapsed and check validity.
    time_elapsed = None
    while not time_elapsed:
        try:
            time_elapsed = int(input('How much time was spent on the task?' 
                                     ' (Whole minutes)\n> '))
        except ValueError:
            print('That is not a valid entry')
            continue
    clear_screen()
    # input notes
    notes = input('Please enter any additional notes.\n> ')
    # record date of entry
    date = datetime.datetime.today().strftime(time_format)
    task = Task(date, first_name, last_name, task_name, str(time_elapsed), notes)
    # save entry to csv
    task.save_entry()
    return task


def start():
    """checks for existing csv file, else creates one and writes header."""
    try:
        with open("work_logs.csv", 'x') as log_file:
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
    """initial menu on run"""
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
    """menu for search items"""
    search = Search()
    while True:
        print('How would you like to search?\n'
              '1: Exact Date\n'
              '2: Exact input\n'
              '3: Input pattern\n'
              '4: Return to main menu')
        menu_select = input('> ')
        if menu_select == '1':
            search.exact_date()
        elif menu_select == '2':
            search_string = input('Search query: ').lower()
            search.exact_input(search_string)
        elif menu_select == '3':
            search_string = input('Search query: ')
            search.input_pattern(search_string)
        elif menu_select == '4':
            clear_screen()
            menu()
        else:
            clear_screen()
            print('That is not a valid selection.')
            continue


if __name__ == '__main__':
    start()
    menu()
