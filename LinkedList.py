class LLNode:
    def __init__(self, data, link=None):
        """A linked list node"""
        self.data = data
        self.link = link

    # Recursive Example - recursively call on self.link until tail node
    def __len__(self):
        """Reursively calculates how many items are in LL starting at this node"""
        if self.link is None: return 1  # base case - tail node, len = 1
        return 1 + len(self.link)  # otherwise, len = 1 + len(next)

    # Recursive example - helper function to create a mutable to store state at all levels of recursion
    def __repr__(self):
        """Recursively prints all nodes"""
        return ''.join(self._repr([]))

    def _repr(self, item_list):
        """Helper function (so item_list can be initialized as an empty mutable)"""
        if self.link is None:
            item_list.append(f"{self.data}")  # Base case - add final item
        else:
            item_list.append(f"{self.data} ->")  # Print the current node, no newline
            self.link._repr(item_list)

        return item_list

    # Recursive example - get the last item, and pass it back through all level of recursion
    def get_tail(self):
        """Recursively gets the item stored in the tail node"""
        if self.link is None:
            return self.data
        else:
            return self.link.get_tail()

    def add_last(self, item):
        """
        Recursively adds an item to the list
        :param item: Item to be added
        :return: None
        """
        if self.link is not None:
            self.link.add_last(item)
            return
        self.link = LLNode(item)

    def sum_all(self):
        """
        Recursively adds all the items in the list
        :return: The sum of the items in the list
        """
        if self.link is None:
            return self.data
        return self.data + self.link.sum_all()

    def reverse(self, prev=None):
        """
        Recursively reverses the list
        :param prev: The previous node (Default None)
        :return: The first item in the list (Now the last)
        """
        if self.link is None:
            self.link = prev
            return self
        new_node = self.link.reverse(prev=self)
        self.link = prev
        return new_node


# Do not make any changes to LinkedList - all your code should be above in the LLNode class
class LinkedList:
    def __init__(self, items=None):
        """Initializes a new empty LinkedList"""
        self._head = None
        if items is not None:
            for item in items:
                self.add_last(item)  # use add_last() to maintain ordering

    def add_first(self, item):
        """Adds to beginning of Linked List"""
        self._head = LLNode(item, self._head)

    def remove_first(self):
        """Removes and returns first item"""
        if self._head is None: raise RuntimeError('Cannot remove from an empty list.')  # Edge case

        item = self._head.data  # retrieve data
        self._head = self._head.link  # update head
        return item  # return

    # For demonstration and debug purposes: Prints all the elements
    def __repr__(self):
        """Recursively prints the Linked List"""
        return repr(self._head)

    def __len__(self):
        """Returns the number of nodes in Linked List"""
        return len(self._head) if self._head else 0

    def add_last(self, item):
        """Adds item to end of Linked List"""
        if self._head is None: return self.add_first(item)
        self._head.add_last(item)

    def sum_all(self):
        """Returns sum of all items in Linked List"""
        return self._head.sum_all() if self._head else 0

    # Reverses the list in linear time, no copying of the data
    def reverse(self):
        """Reverses linked list"""
        # Note that LLNode.reverse() should return the new head
        self._head = self._head.reverse() if self._head else None

    def get_tail(self):
        """Returns the item stored in tail"""
        return self._head.get_tail() if self._head else None
