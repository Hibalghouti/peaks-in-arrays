def find_peaks(array):
    peaks = []
    
    #skipping the first and last elements
    for i in range(1, len(array) - 1):
        if array[i] > array[i - 1] and array[i] > array[i + 1]:
            peaks.append(i)  

    return peaks


array = [1, 3, 2, 5, 4, 6, 3]
print(find_peaks(array)) 

#for index 1: 3>1 & 3>2 so add 1 to the list
#for index 2: 2!>3 and 2!>5 so dont add 2
#for index 3: 5>2 and >4 so add 3 to the list
#for index 4: 4!>5 and !>6 so dont add 4
#for index 5: 6>4 and 6>3 so add 5 to the list
