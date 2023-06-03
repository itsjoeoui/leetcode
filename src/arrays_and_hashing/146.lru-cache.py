#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#


from collections import OrderedDict


# @lc code=start
class LRUCache:
    # this can also be implemented using a doubly linked list
    def __init__(self, capacity: int):
        self.cap: int = capacity
        self.cache: OrderedDict = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
