class node:
    def __init__(self,data):
        self.data=data
        self.right = None
        self.left = None

    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    def find(self,val):
        if val < self.data:
            if self.left is None:
                return str(val)+' Not Found'
            return self.left.find(val)
        elif val > self.data:
            if self.right is None:
                return str(val)+' Not Found'
            return self.right.find(val)
        else:
            print(str(self.data)+' is found')
                

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()
root = node(12)
root.insert(14)
root.insert(6)
root.insert(0)

root.printTree()
print(root.find(3))
