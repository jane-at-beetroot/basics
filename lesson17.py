class Task:

    def __init__(self, title):
        self.done = False
        self.title = title
        self._priority = 1

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


