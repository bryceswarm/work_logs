import random
import string
import csv
import datetime

class Task:
    def __init__(self, date, first_name, last_name, task_name,
                 time_elapsed, notes=None, id=None, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.time_elapsed = time_elapsed
        self.notes = notes
        self.task_name = task_name
        self.date = date

        if id:
            self.id = id
        else:
            self.id = self.get_id()
        self.fields = [
            'id',
            'first_name',
            'last_name',
            'task_name',
            'time_elapsed',
            'notes',
            'date',
        ]


    def __str__(self):
        """Prints out readable task request"""
        str_fmt = ('Date: {}\n'
                   'Task Name: {}\n'
                   'First Name: {}\n'
                   'Last Name: {}\n'
                   'Time Spent: {}\n'
                   'Notes: {}')
        return str_fmt.format(self.date, self.task_name,
                               self.first_name, self.last_name,
                               self.time_elapsed, self.notes)


    def save_entry(self):
        """Saves tasks to csv file"""
        with open('work_logs.csv', 'a', newline='') as log_file:
            writer = csv.DictWriter(log_file, fieldnames=self.fields)
            writer.writerow({
                'id' : self.id,
                'first_name' : self.first_name,
                'last_name' : self.last_name,
                'task_name' : self.task_name,
                'time_elapsed' : self.time_elapsed,
                'notes' : self.notes,
                'date' : self.date,
            })


    def get_id(self):
        """adds unique identifier to each task"""
        id_list = []
        with open('work_logs.csv', 'r') as log_file:
            reader = csv.DictReader(log_file)
            for row in reader:
                id_list.append(row['id'])

        while True:
            id = ''.join(random.choices(string.ascii_uppercase
                                        + string.digits, k=10))
            if id not in id_list:
                break
        return id

