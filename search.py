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
        clear_screen()
        count = 1
        print('The following tasks are available for view:')
        for row in self.results:
            print('{}. {}'.format(count, row['date']))
            count += 1
        selected_date = input('Which entry would you like to view?\n'
                              '> ')
        clear_screen()
        try:
            selected_date = int(selected_date)
        except ValueError:
            clear_screen()
            print('That is not a valid selection')
            return self.exact_date()
        if selected_date <= 0 or selected_date > count:
            clear_screen()
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
        input('Press any key to continue')
        clear_screen()

    def exact_input(self, search_string):
        clear_screen()
        input_results = []
        count = 1
        print('The following tasks are available for view:')
        for row in self.results:
            if search_string in row['task_name'].lower() \
                    or search_string in row['notes'].lower():
                input_results.append(row)
        for row in input_results:
            print('{}. {}'.format(count, row['task_name']))
            count += 1
        selected_task = input('Which entry would you like to view?\n'
                              '> ')
        clear_screen()
        try:
            selected_task = int(selected_task)
        except ValueError:
            clear_screen()
            print('That is not a valid selection')
            return self.exact_input(search_string)
        if selected_task <= 0 or selected_task > count:
            clear_screen()
            print('That is not a valid selection')
            return self.exact_input(search_string)
        task = Task(input_results[selected_task - 1]['date'],
                    input_results[selected_task - 1]['first_name'],
                    input_results[selected_task - 1]['last_name'],
                    input_results[selected_task - 1]['task_name'],
                    input_results[selected_task - 1]['time_elapsed'],
                    input_results[selected_task - 1]['notes'],
                    )
        clear_screen()
        print(task)
        input('Press any key to continue')
        clear_screen()

    def input_pattern(self):
        # print task matching regex pattern
        clear_screen()
        while True:
            search_pattern = input('Search regex pattern, press "Q" to quit: ')
            input_results = []
            count = 1
            if search_pattern.upper() == 'Q':
                break

            for row in self.results:
                if (re.search(r'{}'.format(search_pattern), row['task_name']) or
                        re.search(r'{}'.format(search_pattern), row['notes'])):
                    input_results.append(row)
            if input_results:
                print('The following tasks are available for view:')
                for row in input_results:
                    print('{}. {}'.format(count, row['task_name']))
                    count += 1
                selected_task = input('Which entry would you like to view?\n'
                                      '> ')
                clear_screen()
            else:
                clear_screen()
                print("No matches found for '{}' in Task Name or Notes"
                      "".format(search_pattern))
                break

            try:
                selected_task = int(selected_task)
            except ValueError:
                clear_screen()
                print('That is not a valid selection')
                return self.exact_input(search_pattern)
            if selected_task <= 0 or selected_task > count:
                clear_screen()
                print('That is not a valid selection')
                return self.exact_input(search_pattern)
            task = Task(input_results[selected_task - 1]['date'],
                        input_results[selected_task - 1]['first_name'],
                        input_results[selected_task - 1]['last_name'],
                        input_results[selected_task - 1]['task_name'],
                        input_results[selected_task - 1]['time_elapsed'],
                        input_results[selected_task - 1]['notes'],
                        )
            clear_screen()
            print(task)
            break
        input('Press any key to continue')
        clear_screen()
