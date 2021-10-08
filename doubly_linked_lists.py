class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

    def __repr__(self):
        return "Node Object: data={}".format(self.data)

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

    def get_previous(self):
        return self.previous

    def set_previous(self, new_previous):
        self.previous = new_previous

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def __str__(self) -> str:
        output = ""
        current_node = self.head
        while current_node is not None:
            output += " <- " + str(current_node.get_data()) + " -> "
            current_node = current_node.get_next()
        return output

    def is_empty(self):
        return self.head is None

    def size(self):
        if self.head is None:
            return 0
        
        size = 0
        current_node = self.head
        while current_node is not None:
            size += 1
            current_node = current_node.get_next()
        return size

    def search(self, data):
        if self.head is None:
            return False
        
        current_node = self.head
        while current_node is not None:
            if current_node.get_data() == data:
                return True
            else:
                current_node = current_node.get_next()
        return False

    def add_front(self, data):
        node = Node(data)
        node.set_next(self.head)
        if self.head is not None:
            self.head.set_previous(node)
        self.head = node

    def remove(self, data):
        if self.head.get_data() == data:
            self.head = self.head.next
            return True

        current_node = self.head.get_next()
        while current_node is not None:
            if current_node.get_data() == data:
                prev_node = current_node.get_previous()
                next_node = current_node.get_next()
                prev_node.set_next(next_node)
                if next_node is not None:
                    next_node.set_previous(prev_node)
                return True
            else:
                current_node = current_node.get_next()
        return False
