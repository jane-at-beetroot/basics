class ListItem:
    
    prev = None
    data = None
    next = None

    def __init__(self, data):
        self.data = data


class LinkedList:

    head = None
    
    def __init__(self, data):
        self.head = ListItem(data=data)

    def add_element(self, data):
        new_element = ListItem(data=data)
        tail = self.head
        print('Tail now {}'.format(tail.data))
        while tail.next is not None:
            tail = tail.next
            print('Tail now {}'.format(tail.data))
        tail.next = new_element
        new_element.prev = tail

    def delete_element(self, data):
        pass


class Dequeue:
    
    def __init__(self):
        self._items = []

    def add_to_tail(self, element):
        self._items.append(element)

    def add_to_head(self, element):
        self._items.insert(0, element)

    def pop_from_tail(self):
        return self._items.pop(-1)

    def pop_from_head(self):
        return self._items.pop(0)

    @property
    def empty(self):
        return not bool(self._items)






