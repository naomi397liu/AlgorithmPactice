# input: list of ints
# monotonic - sequence that is always inc or always dec
# return T or F 

def is_monotonic(llist):
    """
    iterate thru
    if the second int is greater/less than the first
    then I will check the following to see if they continue
    to inc otherwise break and return false
    
    """
    # sol in interview:
    # if llist == llist.sort() or llist == llist.sort(reverse=True):
    #     return True
    # else:
    #     return False

    #one-liner
    # return llist == llist.sort() or llist == llist.sort(reverse=True)

    #fastest sol
    increasing, decreasing = True, True
    for i in range(len(llist)-1):
        if llist[i] < llist[i+1]:
            decreasing = False
        if llist[i] > llist[i+1]:
            increasing = False
    return (increasing or decreasing)



print(is_monotonic([6,4,3]))

