from collections import deque
  
def pushToQueue(q, node):
    q.append(node)

def popFromQueue(q):
    if(hasNodes(q) == True):
        print("Value removed from Queue: ", q.popleft())
    else:
        print("\nQueue is empty.\n")

def printNodes(q):
    print(q)

def hasNodes(q):
    if(len(q) == 0):
        return False 
    else:
        return True

def main():
    
    q = deque()
    choice = 0

    while(choice != '4'):

        print("\n\nMenu: \n1. Display items in queue \n2. Push item into queue \n3. Remove item from queue \n4. Exit program\n\n")
        choice = input("Choose option from menu above\n")
        
        if(choice == '1'):
            printNodes(q)

        elif(choice == '2'):
            node = input("\nEnter a value you would like to add to the queue. Preferably a number.\n")
            pushToQueue(q, node)
        
        elif(choice == '3'):
            popFromQueue(q)
        
        elif(choice == '4'):
            print("Good bye.\n")

        else:
            print("Sorry, please enter a number between 1 and 4.")
    
main()
