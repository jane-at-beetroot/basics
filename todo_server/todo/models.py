import json

class Task:

    objects = []

    def __init__(self, title, priority=1):
        self.id = len(Task.objects) + 1
        self.done = False
        self.title = title
        self.priority = priority
        self.location = None
        self.tag = None
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
        if int(value) in range(1, 11):
            self._priority = int(value)
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