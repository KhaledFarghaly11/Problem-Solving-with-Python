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

    def right_rotate(self):
        if self.size == 0:
            return

        last_element = self.memory[self.size - 1]
        for idx in range(self.size - 2, - 1, - 1):
            self.memory[idx + 1] = self.memory[idx]
        self.memory[0] = last_element

    def right_rotate_steps(self, times):
        times %= self.size
        for step in range(times):
            self.right_rotate()


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

def test_right_rotate_steps():
    array = Array(0)
    array.append(0)
    array.append(1)
    array.append(2)
    array.append(3)
    array.append(4)
    print(array)
    # 0, 1, 2, 3, 4,

    array.right_rotate_steps(3)
    print(array)
    # 2, 3, 4, 0, 1,
    array.right_rotate_steps(7)
    print(array)
    # 0, 1, 2, 3, 4,

    array.right_rotate_steps(123456789)
    print(array)
    # 1, 2, 3, 4, 0,

if __name__ == '__main__':
    test_right_rotate_steps()