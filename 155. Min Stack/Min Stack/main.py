# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
#
# Example:
#
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.


class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lst = []
        self.min_ind = 0

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.lst.append(x)
        if x < self.lst[self.min_ind]:
            self.min_ind = len(self.lst) - 1

    def pop(self):
        """
        :rtype: None
        """
        del self.lst[-1]
        if self.min_ind > len(self.lst) - 1 and len(self.lst) > 0:
            self.min_ind = self.lst.index(min(self.lst))

    def top(self):
        """
        :rtype: int
        """
        return self.lst[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.lst[self.min_ind]


if __name__ == '__main__':

    # Your MinStack object will be instantiated and called as such:
    x1 = 10
    x2 = 20
    x3 = 30
    obj = MinStack()
    obj.push(x1)
    obj.push(x2)
    obj.push(x3)
    obj.pop()
    param_3 = obj.top()
    param_4 = obj.getMin()

