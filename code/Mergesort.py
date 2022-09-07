from random import randint
import time

def random_list(size,lowest,highest):
    '''
    This function is used to generate random list of elements
    Inputs: size of the list, lowest element in the list, highest element in the list
    Outputs: random list of elements
    '''
    list = []
    #generating random elements
    for _ in range(size):
        value = randint(lowest, highest)
        list.append(value)
    ls_elements = list
    return ls_elements

#Merge sort
def merge_sort_conquer(left_ls_elements,right_ls_elements):
    '''
    This function is used to conquer the given two unsorted lists into sorted list by using merge sorting technique
    Inputs: unsorted left sublist, unsorted right sublist
    Outputs: sorted list of given elements
    '''
    sorted_list =[]
    i = 0
    j = 0
    while(i<len(left_ls_elements) and j<len(right_ls_elements)):
        #if right list element is greater than left list element then add left list element to sorted list
        if(left_ls_elements[i]<right_ls_elements[j]):
            sorted_list.append(left_ls_elements[i])
            #increment index of left list by 1
            i =i+1
        #if right list element is less than left list element then add right list element to sorted list
        else:
            sorted_list.append(right_ls_elements[j])
            #increment index of right list by 1
            j =j+1
    #append all remaining elements in left list to sorted list
    sorted_list.extend(left_ls_elements[i:])
    #append all remaining elements in right list to sorted list
    sorted_list.extend(right_ls_elements[j:])
    return sorted_list

def merge_sort(ls_elements):
    '''
    This function is used to divide the given list into sublists and calls conquer function to merge them
    Inputs: unsorted list of elements
    Outputs: sorted list of given elements
    '''
    #if there is only one element in the list then return list
    if(len(ls_elements)<=1):
        return ls_elements
    #calculate middle index
    mid = round(len(ls_elements)/2)
    #recursively calling merge_sort
    left_ls_elements = merge_sort(ls_elements[:mid])
    #recursively calling merge_sort
    right_ls_elements = merge_sort(ls_elements[mid:])
    return merge_sort_conquer(left_ls_elements,right_ls_elements)


# Asking input for list size
print('Enter size of the list : ')
size = int(input())

# Asking input for lowest number in the list
print('Enter Lowest number in the list : ')
lowest = int(input())

# Asking input for highest number in the list
print('Enter Highest number in the list : ')
highest = int(input())

unsorted_ls_elements = random_list(size, lowest, highest)

# merge sort
# store program starting time
start_m = time.time()
sorted_list = merge_sort(unsorted_ls_elements)
# store program ending time
end_m = time.time()
run_time_m = end_m - start_m
print('################################################################ Merge sort #################################################################')
print('\nThe time needed to execute Merge sort with ' + str(len(unsorted_ls_elements)) + ' elements is :' + str(run_time_m) + ' seconds\n')
print('The sorted ls_elements for given elements by using merge sort technique is: ' + str(sorted_list))
print()