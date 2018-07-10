class SLL:
    def __init__(self):
        self.head = None
    def printallvalues(self):
        runner = self.head
        while runner != None:
            print(runner.val)
            runner = runner.next
        return self
    def removeLast(self):
        if self.head == None:
            return None
        if self.head.next == None:
            # if there is only a head, then we'll be removing the head
            # store the node in the variable last
            last = self.head
            # make the list's head point to nothing
            self.head = None
            return last
        # When there are more nodes after the head, we need to find the second to last node
        runner = self.head
        # The second to last node will have no next.next
        while runner.next.next != None:
            runner = runner.next
        last = runner.next
        runner.next = None
        return last
    def deleteNodeTwo(self):
        if self.head != None and self.head.next != None:
            self.head.next = self.head.next.next
        return self
    def addNode(self, value):
        # create the new node
        newnode = Node(value)
        # if the list does not have a head, make the new node the head
        if self.head == None:
            self.head = newnode
        # if the list does have a head, create a new variable called runner and have it point to the head node.
        
        else:
            runner = self.head
            # the purpose of runner is to reassign itself to the different nodes in the list by following the 'next' pointers all the way until it comes to the final node
            # the final node is the one whose 'next' pointer is not pointing to anything
            while(runner.next != None):
                runner = runner.next
            # when the while loop ends, it is because runner.next is None. Therefore, runner is the final node, and to attach our new node, all we need to do is assign the runner's next pointer to the new node.
            runner.next = newnode
        # regardless of whether there was a head node or not when we started this method, we should return self, which is the list. This way, we may chain methods!
        return self
    def removal(self, val):
        if self.head == None:
            return None
        # maybe we need to remove the list's head
        if self.head.val == val:
            guy = self.head
            self.head = self.head.next
            return guy
        # travel through the list to find the node to remove
        runner = self.head
        # check to make sure there is something coming up after the head node
        if runner.next == None:
            return None
        while runner.next.val != val:
            runner = runner.next
            if runner.next == None:
            # runner got to the end of the list without finding the value to remove
            # the value does not exist in the list, nothing to remove
                return None
        # if we get to the end of the while loop, that means that runner.next.val is the value we're looking for
        # store the next node in a variable
        guy = runner.next
        # change the pointer of the runner
        runner.next = runner.next.next
        # return what we stored
        return guy

class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

listOne = SLL()
listOne.addNode(30)
listOne.printallvalues()
removedNode = listOne.removal(20)
if removedNode != None:
    print("removed this node", removedNode.val)
print("----------")
listOne.printallvalues()



