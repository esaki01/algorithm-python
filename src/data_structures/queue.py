class Queue:
    def __init__(self, queue=None):
        if isinstance(queue, list):
            self.queue = queue
        elif queue is None:
            self.queue = []
        else:
            print(f'The queue is invalid type: {queue}')

    def enqueue(self, e):
        self.queue.append(e)

    def dequeue(self):
        try:
            element = self.queue[0]
            del self.queue[0]
            return element
        except IndexError:
            print('The queue has no element')
