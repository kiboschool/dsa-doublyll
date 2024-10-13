class DoublyLL:
    class DNode:
        def __init__(self, val, next, prev):
            self.val = val
            self.next = next
            self.prev = prev

    def __init__(self, s):
        if s == '' or s is None:
            self.head = None

        first_node = DoublyLL.DNode(s[0], None, None)
        prev_node = first_node

        for char in s[1:]:
            next_node = DoublyLL.DNode(char, None, None)
            prev_node.next = next_node
            prev_node = next_node

        self.head = first_node

    def to_string(self):
        trav = self.head
        s = ''
        while trav is not None:
            s += trav.val
            trav = trav.next
        return s

    def init_prevs(self):
        # Implement here
        pass

    def reverse_string(self):
        if self.head is None:
            return ''

        # Get a reference to the last node.
        trav = self.head
        while trav.next is not None:
            trav = trav.next

        s = ''
        while trav is not None:
            s += trav.val
            trav = trav.prev
        return s

str1 = DoublyLL('hello')

print('before calling init_prevs():')
print('  original string: ' + str1.to_string())
# Note: the statement below should just print the last character
# since the null prev values don't allow us to go backward!
print('  reversed string: ' + str1.reverse_string())

str1.init_prevs()

print('after calling init_prevs():')
print('  original string: ' + str1.to_string())
# Once init_prevs() is correctly implemented, the statement below
# should print the reversed string.
print('  reversed string: ' + str1.reverse_string())
