#class node needed for class queue for task 3
class Node:
    def __init__(self,item,next):
        self.item = item
        self.next = next

#class that represents linked queue for task 3
class Queue:
    def __init__(self):
        self.rear = None
        self.front = None
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def append(self, item):
        new_node = Node(item, None)

        if self.is_empty():
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node

        self.count+=1

    def serve(self):
        if self.is_empty():
            raise IndexError("queue is empty")
        item = self.front.item
        self.front = self.front.next
        if self.is_empty():
            self.rear = None
        self.count -=1
        return item

    #function to perform rotation (get rid of item in front and put it at the rear)
    #takes O(1) time
    def turn(self):
        if self.is_empty():
            raise IndexError("queue is empty")
        item = self.front.item
        new_node = Node(item, None)
        self.front = self.front.next
        self.rear.next = new_node
        self.rear = self.rear.next


############################################################ Task 1 ######################################################################


#function to get max number from the list
def get_max(list):
    max = list[0]
    for i in list:
        if i > max:
            max = i
    return max

def count_sort(list,digit,base):
    import math

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

def radix_sort(list, base):
    import math

    l = list
    if len(l) == 0:  # if list is empty - return empty list
        return l
    max = get_max(list)
    num_of_digits = int(math.floor(math.log(max, base) + 1))  # finds number of digits needed to represent max number in given base
    for i in range(num_of_digits):  # do sorting based on the value gotten above
        l = count_sort(l, i, base)

    return l

############################################################ Task 2 ######################################################################

def time_radix_sort():
    from timeit import default_timer as timer
    import random

    f1 = open("./output_task2.csv", 'w')
    bases = [2**1,2**5,2**10,100000,2**22,2**23]
    output = []
    test_data = [random.randint(1,(2**64)-1) for _ in range(100000)]
    for base in bases:
        start = timer()
        radix_sort(test_data,base)
        end = timer()
        output.append((base, end-start))
    print(output)
    for i in range(len(output)):
        s = str(output[i][0]) + ", " + str(output[i][1]) + '\n'
        f1.write(s)
    f1.close()



def plot_csv(csv_file, title=None):
    import numpy as np
    import matplotlib.pyplot as plt

    time_radix_sort()
    with open(csv_file) as csv_file:
        base, time = np.loadtxt(csv_file, delimiter=',', unpack=True)
        # Set up the figure and axes
        plt.scatter(base, time)
        plt.plot(base,time, label = 'time to base correlation')
        plt.xlabel('base used')
        plt.ylabel('time taken (s)')
        plt.legend()
        plt.show()


###################################################### Task 3 ##########################################################################

# performs in O(N*l + N*l + N*l + N*l) ~ O(4(N*l) ~ O(N*l)
def find_rotations(string_list, p):
    rotated_strings = rotate_string(string_list,
                                    p)  # rotates strings in list p times in O(N * l), where N number of items in list, l length of longest string, z is number of turns % l
    matches = check_for_matches(string_list,
                                rotated_strings)  # compares strings in turned strings list to original list in O(N * l)

    p = p * -1  # reverse number of p (if p = 2, then p = -2
    rotate_matches_back = rotate_string(matches, p)  # rotate strings in list of matched strings back
    matches = check_for_matches(string_list,
                                rotate_matches_back)  # check for matches between original list and rotated back match list

    return matches

def get_max_str(list):
    max = len(list)
    for i in range(0,len(list)):
        if len(list[i])-1 > max:
            max = len(list[i])-1
    return max


def count_sort_str(list,index):
    count = [0] * (ord('z') - ord(' ')+2)   #count array to store number of occurences in range of lowest (ASCII of space) to highest (ASCII of 'z'),
    temp_array = [''] * (len(list))                # + 2 for themselves. That will cover space of the whole english alphabet including numbers

    #find the index in count array of current character and add to its occurence
    for i in range(len(list)):
        if index < (len(list[i])):                                  #check if the index less than lenght of the current string
            char_count_index = ord(list[i][index]) - ord(' ') + 1   #if it is, find the correct place where to increment occurence
        else:                                                       #by getting ASCII number of current char - ASCII of the smallest value + 1
            char_count_index = 0                                    #if index is bigger the the current word, means its an empty space, so place of
        count[char_count_index] += 1   #add to the occurence        #occurence is very first element in count array (space)

    #add count of current with the previous
    for i in range(1,len(count)):
        count[i] += count[i-1]

    #start sorting from the back of the list based on character determined by index
    for i in range(len(list)-1,-1,-1):
        if index < (len(list[i])):
            char_count_index = ord(list[i][index]) - ord(' ') + 1
        else:
            char_count_index = 0
        temp_array[count[char_count_index] - 1] = list[i] #assign the item to temp array based on count list index
        count[char_count_index] -= 1                      #decrement count of the char in count array

    #assign every element of the list to the temp list
    for i in range(len(temp_array)):
        list[i] = temp_array[i]
    return list

#Performs in O(N*l), where N num of strings, l - length of longest string
def radix_sort_str(list):
     max = get_max_str(list)        #find max (longest) in list, assigns its' length to max
     for i in range(max,-1,-1): #sort from the back to front
         count_sort_str(list,i)
     return list                #return sorted list


# help function to rotate strings from list p times in
# O(N * (2l + z)))
# ~ O(N * 2l) (since z < l)
# ~ O(N * l)
def rotate_string(string_list, p):
    rotated_strings = []

    # for each string in list O(N), where N is number of strings in list
    for i in range(len(string_list)):
        l, str = len(string_list[i]), string_list[i]  # l is length of string
        q = Queue()  # queue to store a string

        # put string in queue letter by letter O(l) where l lenght of string
        for j in range(l):
            q.append(str[j])

        # if p is positive
        if p > 0:
            z = p % l  # equation to minimize amount get rid of unnecessary turns based on length of string (if p = 6 and l = 4, it will perform 2 turns instead of all 6)
            while z != 0:  # until no more turns left
                q.turn()  # turn string
                z -= 1  # decrese amount of turns

        else:
            z = (p + l) % l  # for negative p value rotation is same if p+l rotation
            while z != 0:
                q.turn()
                z -= 1

        # put string back together from queue
        string = ''
        while not q.is_empty():
            item = q.serve()
            string += item
        rotated_strings.append(string)  # put string to list rotated_strings

    return rotated_strings


#compares 2 lists in O(N + M + N * n + M * m + (N * n + M * m))
# ~ O (5N + 2(N * n)) (since M will be always <= N and m <= n)
# ~ O(N + N * n) ~ O(N*n)
# ~ O(N * n) time
#where
#N is number of strings in l1 and
#M is num of strings in l2,
#n longest string in l1,
#m longest string in l2
def check_for_matches(l1,l2):
    newL1 = []
    newL2 = []
    out = []

    #copy l1 to new list newL1
    for i in range(len(l1)):
        newL1.append(l1[i])

    #copy l2 to new list newL2
    for i in range(len(l2)):
        newL2.append(l2[i])

    newL1 = radix_sort_str(newL1)   #sort newL1
    newL2 = radix_sort_str(newL2)   #sort newL2


    i = 0
    j = 0
    while (i < len(newL1) and j < len(newL2)):
        item1 = newL1[i]
        item2 = newL2[j]
        if item1 == item2:      #if string from list newL1 == string from list newL2
            out.append(newL1[i])    #add string to new list of matches
            i+=1                    #increment both i and j
            j+=1
        elif item1 < item2:     #if string from list 1 is less than string from list 2
            i+=1                #increment only i (counter for list 1)
        else:                   #else increment counter for list 2
            j+=1

    return out