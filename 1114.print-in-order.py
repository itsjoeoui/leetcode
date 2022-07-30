#
# @lc app=leetcode id=1114 lang=python3
#
# [1114] Print in Order
#

# @lc code=start
from threading import Event


class Foo:
    def __init__(self):
        self.channels = (Event(), Event())

    def first(self, printFirst: 'Callable[[], None]') -> None:

        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.channels[0].set()

    def second(self, printSecond: 'Callable[[], None]') -> None:

        # printSecond() outputs "second". Do not change or remove this line.
        self.channels[0].wait()
        printSecond()
        self.channels[1].set()

    def third(self, printThird: 'Callable[[], None]') -> None:

        # printThird() outputs "third". Do not change or remove this line.
        self.channels[1].wait()
        printThird()
# @lc code=end
