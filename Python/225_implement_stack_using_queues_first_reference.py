# Difficulty - Easy
# Url - https://leetcode.com/problems/implement-stack-using-queues/
# Time complexity: O();
# Space complexity: O();

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []


    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.queue1.append(x)
        self.top = x


    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))

        element = self.queue1.pop()
        self.queue1 = self.queue2
        self.queue2 = []

        return element

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.top

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not self.queue1

# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)

obj.push(3)
print(obj.pop())
print(obj.pop())
obj.push(2)
print(obj.pop())
