class LRUCache(object):
    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.head = self.Node(-1,-1)
        self.tail = self.Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.dictionary = {}
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dictionary:
            node = self.dictionary[key]
            self.delNode(node)
            self.addNode(node)
            return node.val
        return -1

        
    def addNode(self, node):
        temp = self.tail.prev
        node.prev = temp
        node.next = self.tail
        self.tail.prev = node
        temp.next = node

    def delNode(self, node):
        node_prev = node.prev
        node_next = node.next
        node_prev.next = node_next
        node_next.prev = node_prev

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.dictionary:
            curr_node = self.dictionary[key]
            del self.dictionary[key]
            self.delNode(curr_node)
        
        if len(self.dictionary) == self.capacity:
            del self.dictionary[self.head.next.key]
            self.delNode(self.head.next)

        self.addNode(self.Node(key, value))
        self.dictionary[key] = self.tail.prev

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)