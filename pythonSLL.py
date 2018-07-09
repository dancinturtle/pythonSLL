class SLL:
    def __init__(self):
        self.head = None
    def printallvalues(self):
        runner = self.head
        while runner != None:
            print(runner.val)
            runner = runner.next
        return self
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

class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

listOne = SLL()
listOne.addNode(20).addNode(30)
listOne.printallvalues()
listOne.deleteNodeTwo()
print("----------")
listOne.printallvalues()


