arr = [4,5,3,1,45,34,1045,-1000,41]
wanted_sum = 45



def brute_force(array,wanted_sum):
    solutions = []
    for i,x in enumerate(array):
        for y in array[i+1:]:
            if x + y == wanted_sum:
                solutions.append((x,y))
    return(solutions)

def two_pointers(array,wanted_sum):
    array.sort()
    left = 0
    right = len(array)-1
    solutions = []
    while (left < right):
        if array[left] + array[right] == wanted_sum:
            solutions.append((array[left],array[right]))
            left += 1
            right -= 1
        elif array[left] + array[right] < wanted_sum:
            left += 1
        else:
            right -= 1
    return solutions

def set_hash(array, wanted_sum):
    solutions = []
    mn = set(array)
    for i in array:
        if (wanted_sum-i in mn) and (wanted_sum-i != i):
            solutions.append((wanted_sum-i,i))
        mn.remove(i)
    return solutions


print(set_hash(arr,wanted_sum))


#print(two_pointers(arr,wanted_sum))
#print(brute_force(arr,wanted_sum))

