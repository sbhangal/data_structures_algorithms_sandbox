class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = Node(None)

    def printTree(self):
        if(self.root.value is not None):
            self.printNode(self.root)
        else:
            print("Tree is empty.")
    
    def printNode(self, node):
        #print in-order
        if(node.left is not None):
            self.printNode(node.left)
        
        print(node.value)
        
        if(node.right is not None):
            self.printNode(node.right)

    def addNode(self, node):
        if(self.root.value == None):
            self.root = node
        else:
            curNode = self.root
            self.addOtherNode(curNode, node)

    def addOtherNode(self, curNode, nodeToAdd):  
        if(nodeToAdd.value < curNode.value):
            if(curNode.left == None):
                curNode.left = nodeToAdd
            else:
                self.addOtherNode(curNode.left, nodeToAdd)
        elif(nodeToAdd.value >= curNode.value):
            if(curNode.right == None):
                curNode.right = nodeToAdd
            else:
                self.addOtherNode(curNode.right, nodeToAdd)
    
    def search(self, val, curNode):
        if(curNode.value ==  None):
            return False
        
        elif(curNode.value == val):
            return True
        
        elif(val < curNode.value):
            if(curNode.left == None):
                return False
            else:
                return(self.search(val, curNode.left))
        
        elif(val > curNode.value):
            if(curNode.right == None):
                return False
            else:
                return(self.search(val, curNode.right))


    def removeNode(self):

        print("not implemented yet")


def main():
    
    tree = BinaryTree()
    choice = 0
    
    while(choice != '5'):

        print("\n\nMenu: \n1. Print tree \n2. Add a number to the tree \n3. Remove a number from the tree \n4. Search for an item. \n5. Exit program\n\n")
        choice = input("Choose option from menu above\n")
        
        if(choice == '1'):
            print("\n")
            tree.printTree()

        elif(choice == '2'):
            nodeVal = int(input("\nEnter a number you would like to add to the binary tree.\n"))
            node = Node(nodeVal)
            tree.addNode(node)
        
        elif(choice == '3'):
            val = int(input("Please enter a value you would like to remove\n"))
            tree.removeNode()
        
        elif(choice == '4'):
            val = int(input("Please enter a value you would like to search for\n"))
            found = tree.search(val, tree.root)
            if(found == True):
                print("Value was found\n")
            else:
                print("Value was not found\n")

        elif(choice == '5'):
            print("Good bye.\n")

        else:
            print("Sorry, please enter a number between 1 and 5.")
    
main()
