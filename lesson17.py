import googlemaps

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
        place = gmaps.find_place(
            place_lookup,
            'textquery',
            fields=['geometry/location', 'name', 'place_id']
        )
        self.location = {
            'coordinates': place['candidates'][0]['geometry']['location'],
            'name': place['candidates'][0]['name'],
            'google_id': place['candidates'][0]['place_id']
        }

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


