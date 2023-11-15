import inspect


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'{self.data}'


class LinkedList:
    def __init__(self, initial_values=None):
        self.head = None
        self.tail = None
        self.length = 0

        self.debug_data = []  # add/remove nodes you use

        if initial_values:
            for value in initial_values:
                self.insert_end(value)

    def _add_node(self, node):
        self.debug_data.append(node)
        self.length += 1

    def _delete_node(self, node):
        if node in self.debug_data:
            self.debug_data.remove(node)
        else:
            print("Node does't exist!!")
            return

        self.length -= 1

    def debug_print_address(self):
        temp_head = self.head

        while temp_head is not None:
            print(f'{temp_head.data}@{id(temp_head)}', end='\t->\t')
            temp_head = temp_head.next
        print('None')

    def debug_print_node(self, node):
        if node is None:
            print('None')
            return

        print(str(node.data).ljust(5), end=' -> ')
        next_value = 'None' if node.next is None else str(node.next.data)
        print(next_value.ljust(5), end='\t')

        if node == self.head:
            print("head")
        elif node == self.tail:
            print("tail")
        else:
            print("")

    def debug_print_existing_nodes(self, msg=None):
        if msg:
            print(msg)

        for node in self.debug_data:
            self.debug_print_node(node)

        print('*******************')
        self.debug_verify_data_integrity()

    def debug_verify_data_integrity(self):
        if self.length == 0:
            assert self.head is None
            assert self.tail is None
            return

        assert self.head is not None
        assert self.tail is not None
        assert self.tail.next is None

        if self.length == 1:
            assert self.head == self.tail
        elif self.length == 2:
            assert self.head.next == self.tail
        else:
            actual_lst_len = 0
            temp_head = self.head

            while temp_head is not None:
                temp_head = temp_head.next
                actual_lst_len += 1
                assert actual_lst_len < 1000  # Consider infinite cycle

            assert self.length == actual_lst_len
            assert self.length == len(self.debug_data)

    def insert_front(self, value):
        node = Node(value)
        self._add_node(node)

        node.next = self.head
        self.head = node
        
        if self.length == 1:
            self.tail = self.head

        self.debug_verify_data_integrity()


    def insert_end(self, value):
        node = Node(value)
        self._add_node(node)

        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.debug_verify_data_integrity()  # ** verify as possible

    def print(self):
        temp_head = self.head

        while temp_head is not None:
            print(temp_head.data, end='->')
            temp_head = temp_head.next
        print('None')

    def __iter__(self):
        temp_head = self.head
        while temp_head is not None:
            yield temp_head
            temp_head = temp_head.next

    def __repr__(self):
        represent = ''
        temp_head = self.head

        while temp_head is not None:
            represent += str(temp_head.data)
            temp_head = temp_head.next
            if temp_head:
                represent += ', '

        return represent



def test1():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')
    lst = LinkedList([])

    lst.debug_print_existing_nodes()
    result = str(lst)
    expected = ''

    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')


def test2():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')
    lst = LinkedList([6])

    lst.debug_print_existing_nodes()
    result = str(lst)
    expected = '6'

    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')


def test3():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    lst = LinkedList([6, 10, 8, 15])
    lst.debug_print_existing_nodes()

    result = str(lst)
    expected = '6, 10, 8, 15'

    assert result == expected, \
        f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'

    print('PASSED\n')

def test4():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    lst = LinkedList([4])
    lst.insert_front(3)
    lst.insert_front(2)
    lst.insert_front(1)
    
    lst.debug_print_existing_nodes()

    result = str(lst)
    expected = '1, 2, 3, 4'

    assert result == expected, \
        f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'

    print('PASSED\n')


if __name__ == '__main__':
    test1()  # empty
    test2()  # one element
    test3()  # 6, 10, 8, 15
    test4()  # 1, 2, 3, 4

    # Must see to insure no RTE
    print('ALL CASES PASSED')

