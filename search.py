import csv
import re
import os

from task import Task


# clear the command screen
def clear_screen():
    """ Clears the command screen for next prompts to be displayed
        more efficiently."""
    os.system('cls' if os.name == 'nt' else 'clear')

class Search:
    def __init__(self):
        self.results = []
        with open('work_logs.csv', 'r', newline='') as log_file:
            reader = csv.DictReader(log_file, delimiter=',')
            for row in reader:
                self.results.append(row)

    def exact_date(self):
        count = 1
        for row in self.results:
            print('{}. {}'.format(count, row['date']))
            count += 1
        selected_date = input('Which entry would you like to view?\n'
                              '> ')
        try:
            selected_date = int(selected_date)
        except ValueError:
            print('That is not a valid selection')
            return self.exact_date()
        task = Task(self.results[selected_date - 1]['date'],
                    self.results[selected_date - 1]['first_name'],
                    self.results[selected_date - 1]['last_name'],
                    self.results[selected_date - 1]['task_name'],
                    self.results[selected_date - 1]['time_elapsed'],
                    self.results[selected_date - 1]['notes'],
                    )
        clear_screen()
        print(task)
        return task


    def exact_input(self, search_string):
        input_results = []
        count = 1
        for row in self.results:
            if search_string in row['task_name'].lower() \
                    or search_string in row['notes'].lower():
                input_results.append(row)
        for row in input_results:
            print('{}. {}'.format(count, row['task_name']))
            count += 1
        selected_task = input('Which entry would you like to view?\n'
                              '> ')
        try:
            selected_task = int(selected_task)
        except ValueError:
            print('That is not a valid selection')
            return self.exact_input(search_string)
        task = Task(input_results[selected_task - 1]['date'],
                    input_results[selected_task - 1]['first_name'],
                    input_results[selected_task - 1]['last_name'],
                    input_results[selected_task - 1]['task_name'],
                    input_results[selected_task - 1]['time_elapsed'],
                    input_results[selected_task - 1]['notes'],
                    )
        print(task)


    def input_pattern(self, search_string):
        #print task matching regex pattern
        pass
