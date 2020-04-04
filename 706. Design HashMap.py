class ListNode:
    def __init__(self, key, val):
        self.pair = (key, val)
        self.next = None


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = 1000
        self.h = [None] * self.m

    def put(self, key: int, val: int) -> None:
        """
        value will always be non-negative.
        """
        index = key % self.m

        if self.h[index] is None:
            self.h[index] = ListNode(key, val)
            return
        cur = self.h[index]

        while True:
            if cur.pair[0] == key:
                cur.pair = (key, val)
                return
            if cur.next is None:
                break
            cur = cur.next
        cur.next = ListNode(key, val)

        return

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = key % self.m

        if self.h[index] is None:
            return -1
        cur = self.h[index]
        while cur:
            if cur.pair[0] == key:
                return cur.pair[1]
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = key % self.m

        if self.h[index] is None:
            return
        if self.h[index].pair[0] == key:
            self.h[index] = self.h[index].next
            return
        prev, cur = self.h[index], self.h[index].next
        while cur:
            if cur.pair[0] == key:
                prev.next = cur.next
                return
            prev, cur = prev.next, cur.next
        return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
