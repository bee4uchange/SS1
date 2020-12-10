# Node class
class Node:
    # Constructor to initialize the node object
    def __init__(self, name, data):
        self.name = name
        self.data = data
        self.next = None


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    def sortedInsert(self, new_node):

        # Special case for the empty linked list
        if self.head is None:
            new_node.next = self.head
            self.head = new_node

        # Special case for head at end
        elif self.head.data >= new_node.data:
            new_node.next = self.head
            self.head = new_node

        else:

            # Locate the node before the point of insertion
            current = self.head
            while (current.next is not None and
                   current.next.data < new_node.data):
                current = current.next

            new_node.next = current.next
            current.next = new_node

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to print it the linked LinkedList
    def printList(self):
        temp = self.head
        str = ""
        while (temp):
            str += '({} {})'.format(temp.name, temp.data)
            temp = temp.next
        print(str)


if __name__ == "__main__":
    string = 'BCAADDDCCACACAC'
    # Calculating frequency
    freq = {}
    for c in string:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
    f = []
    for i in freq:
        f.append(i)
    print(f)
    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    f = []
    for i in freq:
        f.append(i)
    print(f)

    nodes = freq
    print(nodes)

    llist = LinkedList()
    new_node = Node(5)
    llist.sortedInsert(new_node)
    new_node = Node('b', 10)
    llist.sortedInsert(new_node)
    new_node = Node('d', 7)
    llist.sortedInsert(new_node)
    new_node = Node('t', 3)
    llist.sortedInsert(new_node)
    new_node = Node('v', 1)
    llist.sortedInsert(new_node)

    print("Final Linked List")
    llist.printList()
