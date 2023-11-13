import ctypes


class Array:
    def __init__(self, size, initial_value = None):
        self.size = size
        self._capacity = max(16, 2 * size)

        array_data_type = ctypes.py_object * self._capacity
        self.memory = array_data_type()

        for i in range(self._capacity):
            self.memory[i] = initial_value

    def expand_capacity(self):
        self._capacity *= 2

        array_data_type = ctypes.py_object * self._capacity
        new_memory = array_data_type()

        for i in range(self.size):  # copy
            new_memory[i] = self.memory[i]

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
            self.expand_capacity()
        for p in range(self.size - 1, idx - 1, - 1):
            self.memory[p + 1] = self.memory[p]
        self.memory[idx] = item
        self.size += 1

    def pop(self, idx):
        assert idx >= -self.size and idx < self.size, 'pop index out of range'
        if idx < 0:
            idx += self.size
        val = self.memory[idx]
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


class Array2D:
    def __init__(self, rows, cols, initial_value=None):
        self.rows, self.cols = rows, cols

        self.grid = Array(rows) # 1-D array for each row
        for i in range(rows):
            self.grid[i] = Array(cols, initial_value)  # columns of ith row
    
    def __getitem__(self, index):
        r, c = index[0], index[1]
        return self.grid[r][c]

    def __setitem__(self, index, value):
        r, c = index[0], index[1]
        self.grid[r][c] = value

    def __repr__(self):
        result = ''
        for i in range(self.rows):
            result += str(self.grid[i]) + '\n'
        return result

if __name__ == '__main__':

    # create 2x4 grid initialized to 0
    arr2d = Array2D(2, 4, 0)
    arr2d[(0, 2)] = 3
    arr2d[(1, 1)] = 5
    arr2d[(1, 3)] = 7
    print(arr2d)
    # 0, 0, 3, 0,
    # 0, 5, 0, 7,
    print(arr2d[(1, 3)])    # 7

