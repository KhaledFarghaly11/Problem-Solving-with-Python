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

    def index_transposition(self, value):
        for idx in range(self.size):
            if self.memory[idx] == value:
                if idx == 0:
                    return 0
                # Swap the 2 elements
                self.memory[idx], self.memory[idx - 1] = self.memory[idx - 1], self.memory[idx]
                return idx - 1
        return -1

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

def test_index_transposition():

    array = Array(0)
    array.append(10)
    array.append(20)
    array.append(30)
    array.append(40)
    array.append(50)
    print(array)
    # 10, 20, 30, 40, 50,

    print(array.index_transposition(10))
    print(array)    # 0
    # 10, 20, 30, 40, 50,

    print(array.index_transposition(50))
    print(array)    # 3
    # 10, 20, 30, 50, 40,

    print(array.index_transposition(50))
    print(array)    # 2
    # 10, 20, 50, 30, 40,

    print(array.index_transposition(60))    # -1

if __name__ == '__main__':
    test_index_transposition()