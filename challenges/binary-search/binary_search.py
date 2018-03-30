def binary_search(arr, el):  #function with two arguments
    counter = 0  #Declare counter
    for i in arr:  #For loop through the list
        counter += 1  #Counter increment
        if i == el:  #If current item is equal to second argument
            return counter -1  #Return counter -1
    return -1  #If no match found return -1


