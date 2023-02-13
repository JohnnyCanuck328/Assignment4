#Determines the largest number of subsequent equal integers i.e.
#Please input a list of integers separated by spaces: 1 2 2 3 3 3
#3
def longest_run(l):
    '''
    (list)->int
    list must be only of type float or type integer
    determines the greatest number of times  a number is repeated
    '''
    max_run=0
    current_run=0
    element=None
    for inc in l:
        if (inc == element) and (current_run>=max_run):
            current_run=current_run+1
            max_run=current_run
            element=inc

        elif (inc==element):
            current_run = current_run + 1
            element = inc

        else:
            current_run = 1
            element=inc
    return(max_run)

raw_input=input("Please input a list of integers separated by spaces: ")
raw_input=raw_input.strip()
usable_input1=raw_input.split()
for inc in range(len(usable_input1)):
    usable_input1[inc]=float(usable_input1[inc])

print(longest_run(usable_input1))