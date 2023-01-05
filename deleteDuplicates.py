#deleting duplicates from a sorted array and returning the count of unique values in Constant space O(1) and linear time O(n)

def delete_duplicates(l):
    writing_ptr = 1
    for i in range(1, len(l)):
        if l[writing_ptr - 1] != l[i]:
            l[writing_ptr] = l[i]
            writing_ptr +=1
    return writing_ptr

    # if you want to return the unique values return the below list instead of above pointer index

    # return l[:writing_ptr]

#driver code
# l = [1,1,2,2,3,4,4,5,5,5,6]
# print(delete_duplicates(l))

l = list(map(int,(input('Enter space seperated values: ').split(' '))))
print('The number of unique values is: ', delete_duplicates(l))