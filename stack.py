class Stack:
    def __init__(self):
        self.nodes = []

    def pushToStack(self, node):
        self.nodes.append(node)

    def popFromStack(self):
        if (self.hasNodes() == True):
            print("You popped item: ", self.nodes.pop())
        else:
            print("The stack is empty.")
    
    def printNodes(self):
        print(self.nodes)

    def hasNodes(self):
        if(self.nodes == []):
            return False 
        else:
            return True

def main():
    
    stack = Stack()
    choice = 0

    while(choice != '4'):

        print("\n\nMenu: \n1. Display items in stack \n2. Push item into stack \n3. Pop item from stack \n4. Exit program\n\n")
        choice = input("Choose option from menu above\n")
        
        if(choice == '1'):
            stack.printNodes()

        elif(choice == '2'):
            node = input("\nEnter a value you would like to add to the stack. Preferably a number.\n")
            stack.pushToStack(node)
        
        elif(choice == '3'):
            stack.popFromStack()
        
        elif(choice == '4'):
            print("Good bye.\n")

        else:
            print("Sorry, please enter a number between 1 and 4.")
    
main()
