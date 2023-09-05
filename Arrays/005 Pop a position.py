import ctypes


class Array:
    def __init__(self, size):
        self.size = size  # user size
        self._capacity = max(16, 2 * size)  # actual memory size

        array_data_type = ctypes.py_object * self._capacity
        self.memory = array_data_type()

        for i in range(self._capacity):
            self.memory[i] = None

    def expand_capacity(self):
        # Double the actual array size
        self._capacity *= 2
        print(f'Expand capacity to {self._capacity}')

        # create a new array of _capacity
        array_data_type = ctypes.py_object * self._capacity
        new_memory = array_data_type()

        for i in range(self.size):  # copy
            new_memory[i] = self.memory[i]

        # use the new memory and delete old one
        del self.memory
        self.memory = new_memory

    def append(self, item):
        if self.size == self._capacity:
            self.expand_capacity()
        self.memory[self.size] = item
        self.size += 1

    def pop(self, idx):
        assert idx >= -self.size and idx < self.size, 'pop index out of range'

        if idx < 0:
            idx += self.size

        val = self.memory[idx]

        # left shift the array
        # observe: if we remove the last a few values,
        # it will be very efficient due to few steps
        for p in range(idx + 1, self.size):
            self.memory[p - 1] = self.memory[p]

        self.size -= 1
        return val

    def __len__(self):
        return self.size

    def __getitem__(self, idx):
        return self.memory[idx]  # Is valid idx?

    def __setitem__(self, idx, value):
        self.memory[idx] = value

    def __repr__(self):
        result = ''
        for i in range(self.size):
            result += str(self.memory[i]) + ', '
        return result

def test_pop():
    array = Array(0)
    array.append(10)
    array.append(20)
    array.append(30)
    array.append(40)
    print(array)
    # 10, 20, 30, 40,

    print(array.pop(0))  # 10
    print(array)
    # 20, 30, 40,

    print(array.pop(2))  # 40
    print(array)
    # 20, 30,
    array.append(60)
    array.append(70)
    array.append(80)

    print(array.pop(-1))  # 80
    print(array)
    # 20, 30, 60, 70,

    print(array.pop(-4))  # 20
    print(array)
    # 30, 60, 70,
    # pop index out of range
    # array.pop(-4)
    # array.pop(3)

if __name__ == '__main__':
    test_pop()
