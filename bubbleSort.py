def bubbleSortAlgorithm(arr):
    # bubble sort loop
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            # swap if current > next
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr

def printArray():
    # input list
    bubble_list = bubbleSortAlgorithm([34, -2, 0, 99, 34, -45, 0, 23, -2, 88, 1000, -999, 23, 0])
    
    # print each item
    for i in range(len(bubble_list)):
        print(bubble_list[i])

printArray()
