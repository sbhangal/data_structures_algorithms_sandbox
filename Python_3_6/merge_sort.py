
def mergeSort(l):
    length = len(l)
    
    if(length <= 1):
        return l
    
    #split in half
    lIndex = int(length/2)
    rIndex = int(length/2)

    left = l[0:lIndex]
    right = l[rIndex:]

    mergeSort(left)
    mergeSort(right)

    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l[k] = left[i]
            i += 1
        else:
            l[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        l[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        l[k] = right[j]
        j += 1
        k += 1


def main():
    toSort = [4, 2, 6, 46, 12, 1, 87, 14]
    print(toSort)

    
    mergeSort(toSort)
    print(toSort)

main()