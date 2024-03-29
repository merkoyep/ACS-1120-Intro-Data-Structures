#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = []
        for i in range(init_size):
            self.buckets.append(LinkedList())

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = []
        for key, val in self.items():
            items.append('{!r}: {!r}'.format(key, val))
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        Running time: O(n) Iteration through all linked lists in all buckets."""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        Running time: O(n) Iterating through all linked lists in all buckets"""
        # Loop through all buckets
        # Collect all values in each bucket
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values


    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        Running time: O(n) Iterating through all buckets in self.buckets"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        Running time: O(n) iterating through all entries in each linked list."""
        # Loop through all buckets
        # Count number of key-value entries in each bucket
        entry_count = 0
        for linked_list in self.buckets:
            for entry in linked_list:
                entry_count += 1
        return entry_count

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        Running time: O(n) Worst case iterate through the whole linked list.
        best case O(1) if key is at the beginning of list or empty bucket."""
        # Find bucket where given key belongs
        # Check if key-value entry exists in bucket
        bucket_index = self._bucket_index(key)
        linked_list = self.buckets[bucket_index]
        current = linked_list.head
        while current:
            if key == current.data[0]:
                return True
            current = current.next
        return False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        Running time: O(n) Worst case iterate through the whole linked list.
        best case O(1) if key is at the beginning of list or empty bucket."""
        # Find bucket where given key belongs
        # Check if key-value entry exists in bucket
        # If found, return value associated with given key
        # Otherwise, raise error to tell user get failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        bucket_index = self._bucket_index(key)
        linked_list = self.buckets[bucket_index]
        current = linked_list.head
        while current:
            if key == current.data[0]:
                return current.data[1]
            current = current.next
        raise KeyError('Key not found: {}'.format(key))


    def set(self, key, value):
        """Insert or update the given key with its associated value.
        Running time: O(n) Worst case iterate through the whole linked list.
        best case O(1) if key is at the beginning of list or empty bucket."""
        # Find bucket where given key belongs
        # Check if key-value entry exists in bucket
        # If found, update value associated with given key
        # Otherwise, insert given key-value entry into bucket
        bucket_index = self._bucket_index(key)
        linked_list = self.buckets[bucket_index]
        current = linked_list.head
        found = False
        while current:
            if key == current.data[0]:
                current.data = (key, value)
                found = True
                break
            current = current.next
        if not found:
            linked_list.append((key, value))

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        Running time: O(n) Worst case iterate through the whole linked list.
        best case O(1) if key is at the beginning of list or empty bucket."""
        # Find bucket where given key belongs
        # Check if key-value entry exists in bucket
        # If found, delete entry associated with given key
        # Otherwise, raise error to tell user delete failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        bucket_index = self._bucket_index(key)
        linked_list = self.buckets[bucket_index]
        previous_node = None
        current_node = linked_list.head

        while current_node:
            if current_node.data[0] == key:
                if previous_node is None:
                    linked_list.head = current_node.next
                    if linked_list.head is None:
                        linked_list.tail = None
                else:
                    previous_node.next = current_node.next
                    if current_node.next is None:
                        linked_list.tail = previous_node
                return
            previous_node = current_node
            current_node = current_node.next
        raise KeyError('Key not found: {}'.format(key))

def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
