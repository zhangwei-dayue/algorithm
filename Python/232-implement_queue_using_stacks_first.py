# Difficulty - Easy
# Url - https://leetcode.com/problems/implement-queue-using-stacks/
# Time complexity: O();
# Space complexity: O();

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None



class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        if self.stack2:
            while self.stack2:
                self.stack1.append(self.stack2.pop())

        self.stack1.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.stack1:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        if self.stack2:
            return self.stack2.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.stack1:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        if self.stack2:
            return self.stack2[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.stack1 and not self.stack2

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()