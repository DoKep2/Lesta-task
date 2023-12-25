from utils import average_benchmark_decorator


class CircularBufferListItem:
    def __init__(self, next_element=None):
        self._data = 0
        self._next_element = next_element

    def next_element(self):
        return self._next_element

    def set_next_element(self, next_element):
        self._next_element = next_element

    def data(self):
        return self._data

    def set_data(self, data):
        self._data = data


class CircularBuffer:
    def __init__(self, capacity):
        self._capacity = capacity
        self._size = 0

        temp = CircularBufferListItem()
        first = temp

        for i in range(capacity - 1):
            temp = CircularBufferListItem(temp)

        first.set_next_element(temp)

        self._head = first
        self._tail = first

    def size(self):
        return self._size

    def capacity(self):
        return self._capacity

    def is_empty(self):
        return self._capacity == 0

    def is_full(self):
        return self._capacity == self._size

    def enqueue(self, el):
        if self.is_full():
            raise Exception("Queue is full!")

        self._head.set_data(el)
        self._size += 1
        self._head = self._head.next_element()

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty!")

        item = self._tail.data()

        self._size -= 1

        self._tail = self._tail.next_element()
        return item


if __name__ == '__main__':
    BUFFER_SIZE = 10000000
    @average_benchmark_decorator
    def test_circular_buffer():
        circular_buffer = CircularBuffer(BUFFER_SIZE)
        for i in range(BUFFER_SIZE):
            circular_buffer.enqueue(i)
        for i in range(BUFFER_SIZE):
            circular_buffer.dequeue()


    test_circular_buffer()
