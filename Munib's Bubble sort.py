from array import array

array = []
upperBound = 0
swap = False
top = 0

InputDone = False
InputValue = 0


while InputDone == False:

    InputValue = (input("Please enter a value to add to the array or enter an empty string"))
    try:
        int(InputValue)
        array.append(int(InputValue))
    except: 
        InputDone = True
        break
print(array)

upperBound = len(array)
top = len(array)


while top > 0:

    swap = False
    
    top -= 1

    while swap == False:
        
        for num in range(upperBound-1):

            for j in range(0, upperBound-num-1):
            
                if array[j] > array[j + 1]:
                    swap = True
                    array[j], array[j + 1] = array[j + 1], array[j]

                
            
    print (array)

