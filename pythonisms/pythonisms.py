from functools import wraps
import time

class Node:
    def __init__(self, value, next_ = None):
        self.value = value
        self.next = next_

class LinkedList:

    def __init__(self, collection=None):
        self.head = None
        if collection:
            for item in reversed(collection): 
                self.insert(item)


    def __iter__(self):

        def value_generator():

            current = self.head

            while current:

                yield current.value

                current = current.next

        return value_generator()

    def __str__(self):

        out = ""

        for value in self:
            out += f"[ {value} ] -> "

        return out + "None"

    def __len__(self):
        return len(list(iter(self)))

    def __eq__(self, other):
        return list(self) == list(other)

    def __getitem__(self, index):


        if index < 0:
            raise IndexError

        for i, item in enumerate(self):
            if i == index:
                return item

        raise IndexError


    def insert(self, value):
        self.head = Node(value, self.head)

    def append(self, value):

        node = Node(value)

        if not self.head:
            self.head = node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = node


def to_sara(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        original_val = func(*args, **kwargs)
        return f'Mother, {original_val}'
    return wrapper

@to_sara
def sara_saying(txt):
    return txt

def to_sama(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        original_val = func(*args, **kwargs)
        return f'daughter, {original_val}'
    return wrapper

@to_sama
def sama_saying(txt):
    return txt 

def tamtam(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        original_val = func(*args, **kwargs)
        return f'{original_val} ...!'
    return wrapper 

@tamtam
def tamtam_saying(txt):
    return txt 

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        value = func(*args, **kwargs)
        end = time.perf_counter()
        run = end - start
        print(f'Finished {func.__name__!r} in {run:.4f} secs')
        return value
    return wrapper 

def calculate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        original_val = func(*args, **kwargs)
        return original_val
    return wrapper

@timer
@calculate
def addition(x, y):
    return x + y



@timer
def waste_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

if __name__ == "__main__":
    print(sara_saying('How old are you?'))
    print(sama_saying('4 years old'))
    print(tamtam_saying('happy birthday'))
    print(addition(3, 4))
    print(waste_time(100))