import json

from ..utils.bubble_sort import bubble_sort
from ..utils.insertion_sort import *
from ..utils.binary_search import binary_search

class Task:

    objects = []

    def __init__(self, title, priority=1):
        self.id = len(Task.objects) + 1
        self.done = False
        self.title = title
        self.priority = priority
        self.location = None
        self.tag = None
#        self.parent = None 
        self.children = []
        Task.objects.append(self)

    def __str__(self):
        return self.title

    def __repr__(self):
        return 'Task(title=\'{}\')'.format(self.title)

    @property
    def priority(self):
        return self._priority

    @priority.setter    
    def priority(self, value):
        if value in range(1, 11):
            self._priority = value
        else:
            raise ValueError('Priority value is out of range')

    def to_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def get_list(cls):
        return cls.objects

    @classmethod
    def list_to_json(cls):
        task_list = [t.__dict__ for t in cls.objects]
        return json.dumps(task_list)

    def add_child(self, title, priority):
        child_task = Task(title, priority)
        self.children.append(child_task.id)

    def get_subtasks(self):
        if not self.children:
            return []
        children = []
        for child_id in self.children:
            child_task = binary_search_by_id(Task.objects, child_id)
            if child_task is not None:
                children.append(child_task)
                children.extend(child_task.get_subtasks())
        return children







