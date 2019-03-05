import array

def printArray(arr):
    length = len(arr)
    if(length == 0):
        print("Array is empty")
        return
    for i in range(0, length):
        print(arr[i])
    
def insertVal(arr, val):
    arr.append(val)

def searchVal(arr, val):
    length = len(arr)
    if(length == 0):
        print("Array is empty")
        return
    for i in range(0, length):
        if(arr[i] == val):
            print("Value found")
            return
    print("Value not found")

def deleteVal(arr, val):
    length = len(arr)
    if(length == 0):
        print("Array is empty")
        return
    for i in range(0, length):
        if(arr[i] == val):
            print("value found")
            del(arr[i])
            print("value deleted")
            return
    print("value not found")
    
def main():
    arr = array.array('i')
    choice = -1

    while(choice != 0):

        print("\n\nMenu: \n1. Print array \n2. Insert number into array \n3. Remove a number from the array \n4. Search for an item. \n0. Exit program\n\n")
        choice = input("Choose option from menu above\n")

        if(choice == 1):
            print("Array: \n")
            printArray(arr)

        elif(choice == 2):
            val = int(input("\nEnter a number you would like to add\n"))
            insertVal(arr,val)

        elif(choice == 3):
            val = int(input("Please enter a number you would like to remove\n"))
            deleteVal(arr, val)

        elif(choice == 4):
            val = int(input("Please enter a number you would like to search for\n"))
            searchVal(arr, val)

        elif(choice == 0):
            print("Good bye.\n")

        else:
            print("Sorry, please enter a number between 0 and 4.")
    
main()