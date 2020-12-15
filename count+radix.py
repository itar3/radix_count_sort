import math

#function to get max number from the list
def get_max(list):
    max = list[0]
    for i in list:
        if i > max:
            max = i
    return max

def count_sort(list,digit,base):
    count = [0] * base #array represents buckets with size of base number
    temp_array = [0] * len(list) #temp array needed for sorting


    #filling up the count array
    for i in range(0,len(list)):
        digit_count_index = ((list[i]//int(math.pow(base,digit))) % base) #finding digit count index using formula (number/base^digit) % base
        count[digit_count_index] += 1                                     #recording the occurence of digit in count array

    # modifying count array by adding count of current with the previous
    for i in range(1,base):
        count[i] += count[i-1]

    #sorting is done from right to left
    for i in range(len(list)-1,-1,-1):
        digit_count_index = ((list[i]//int(math.pow(base,digit))) % base)   #finding digit count index using formula (number/base^digit) % base
        temp_array[count[digit_count_index]-1] = list[i]                    #assign the item to temp array based on count list index
        count[digit_count_index] -= 1                                       #decrement count of the digit in count array

    return temp_array

#implementation for radix sort
def radix_sort(list, base):
    l = list
    if len(l) == 0:                                        #if list is empty - return empty list
        return l
    max = get_max(list)
    num_of_digits = int(math.floor(math.log(max, base)+1)) #finds number of digits needed to represent max number in given base
    for i in range(num_of_digits):                         #do sorting based on the value gotten above
       l = count_sort(l, i, base)

    return l



list = [2,1,3,4]
print(radix_sort(list,64))