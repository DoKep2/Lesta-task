from utils import average_benchmark_decorator


class CircularBuffer:
    def __init__(self, capacity):
        self._capacity = capacity
        self._buffer = [None] * capacity
        self._size = 0
        self._head = 0
        self._tail = 0

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def is_full(self):
        return self._size == self._capacity

    def enqueue(self, value):
        if self.is_full():
            raise Exception("Queue is full!")

        self._buffer[self._tail] = value
        self._tail = (self._tail + 1) % self._capacity
        self._size += 1
        return True

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty!")

        value = self._buffer[self._head]
        self._head = (self._head + 1) % self._capacity
        self._size -= 1
        return value


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
