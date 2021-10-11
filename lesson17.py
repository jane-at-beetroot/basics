import os
import json
import googlemaps
from datetime import datetime


class OpenFile:

    def __init__(self, filename, mode):
        self._file = open(filename, mode)

    def __enter__(self):
        return self._file

    def __exit__(self, type, value, traceback):
        self._file.close()
        return True



class Task:

    def __init__(self, title):
        self.done = False
        self.title = title
        self._priority = 1
        self.location = None

    def __str__(self):
        return self.title

    @property
    def priority(self):
        return self._priority

    @priority.setter    
    def priority(self, value):
        if value in range(1, 11):
            self._priority = value
        else:
            raise ValueError('Priority value is out of range')

    def add_location(self):
        place_lookup = input('Enter location name: \t')
        gmaps = googlemaps.Client(
            key='AIzaSyDZUTx1HWrOcNDng1V7-smaaHTBSobrw0I')
        try:
            place = gmaps.find_place(
                place_lookup,
                'textquery',
                fields=['geometry/location', 'name', 'place_id']
            )
            if place['status'] == 'OK':
                self.location = {
                    'coordinates': place['candidates'][0]['geometry']['location'],
                    'name': place['candidates'][0]['name'],
                    'google_id': place['candidates'][0]['place_id']
                }
            else:
                raise RuntimeError('Cannot set location')
        except:
            return

class Dashboard:

    def __init__(self):
        self.task_list = []

    def add_task(self):
        title = input('Task name:   ')
        new_task = Task(title)
        self.task_list.append(new_task)

    def print_all_tasks(self):
        for task in self.task_list:
            print(task)

    def sort_by_title(self):
        return sorted(self.task_list, 
            key=lambda task: task.title)

    def dump_to_json(self):
        task_list = [t.__dict__ for t in self.task_list]
        dump_time = datetime.now()
        filename = 'tasks_{}.json'.format(
            dump_time.strftime('%Y%m%d%H%M%S'))
        filepath = os.path.join(os.getcwd(),'data', filename)
        '''
        try:
            file = open(filename, 'w')
            json.dump(task_list, file)
            raise RuntimeError()
        except Exception as e:
            print(e)
        finally:
            file.close()
        '''
        with OpenFile(filepath, 'w') as dump_file:
            json.dump(task_list, dump_file)



