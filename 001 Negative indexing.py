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

    def insert(self, idx, item):
        if idx >= self.size:
            self.append(item)
            return
        if idx < -self.size:
            idx = -self.size
        if idx < 0:
            idx += self.size

        if self.size == self._capacity:
            # we can't add any more
            self.expand_capacity()

        # Shift all the data to right first CORRECTLY
        # Shift range (idx, size-1) from the back
        for p in range(self.size - 1, idx - 1, - 1):
            self.memory[p + 1] = self.memory[p]
        self.memory[idx] = item
        self.size += 1

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


def test_insert():
    array = Array(0)
    array.append(1)
    array.append(2)
    array.append(3)
    array.append(4)
    # 1, 2, 3, 4
    array.insert(-1, -10)
    print(array)  # 1, 2, 3, -10, 4,

    array.insert(-2, -20)
    print(array)  # 1, 2, 3, -20, -10, 4,

    array.insert(-3, -30)
    print(array)  # 1, 2, 3, -30, -20, -10, 4,

    array.insert(-4, -40)
    print(array)  # 1, 2, 3, -40, -30, -20, -10, 4,

    array.insert(-5, -50)
    print(array)  # 1, 2, 3, -50, -40, -30, -20, -10, 4,

    array.insert(8, 80)
    print(array)  # 1, 2, 3, -50, -40, -30, -20, -10, 80, 4,

    array.insert(20, 90)
    print(array)  # 1, 2, 3, -50, -40, -30, -20, -10, 80, 4, 90,


if __name__ == '__main__':
    test_insert()