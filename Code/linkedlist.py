#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return f'Node({self.data})'


class LinkedList:

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list."""
        ll_str = ""
        for item in self.items():
            ll_str += f'({item}) -> '
        return ll_str

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(n) Constant time throught direct access of self."""
        # Loop through all nodes and count one for each
        length = 0
        for node in self:
            length += 1
        return length


    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Running time: O(1) direct access of self.tail to append the node."""
        # Create new node to hold given item
        new_node = Node(item)
        # If self.is_empty() == True set the head and the tail to the new node
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        # Else append node after tail
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(1) Direct access of self to set the head node."""
        # Create new node to hold given item
        new_node = Node(item)
        # Prepend node before head, if it exists
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def find(self, matcher):
        """Return an item from this linked list if it is present.
        Best case running time: O(1) When current_node is None, or first node matches
        Worst case running time: O(n) If matcher is not in the first node."""
        # Loop through all nodes to find item, if present return True otherwise False
        current_node = self.head
        while current_node is not None:
            if current_node.data == matcher:
                return True
            current_node = current_node.next
        return False

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Best case running time: O(1) When current_node is None, or first node matches
        Worst case running time: O(n) if item is not in first node."""
        # TODO: Loop through all nodes to find one whose data matches given item
        previous_node = None
        current_node = self.head

        while current_node is not None:
            if current_node.data == item:
                if previous_node is None:
                    self.head = current_node.next
                    if self.head is None:
                        self.tail = None
                else:
                    previous_node.next = current_node.next
                    if current_node.next is None:
                        self.tail = previous_node
                return
            previous_node = current_node
            current_node = current_node.next
        raise ValueError('Item not found: {}'.format(item))
    
    def __iter__(self):
        """Make the linked list iterable."""
        current = self.head
        while current:
            yield current.data
            current = current.next

    def replace(self, old_item, new_item):
        """Replace the first occurrence of old_item with new_item."""
        current_node = self.head
        while current_node is not None:
            if current_node.data == old_item:
                current_node.data = new_item
                return True  # Return True if replacement was made
            current_node = current_node.next
        return False  # Return False if old_item was not found


        # Update previous node to skip around node with matching data
                
            
        # Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))
    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
