#Determines if any two subsequent ints are the same i.e.
#Please input a list of integers separated by spaces: 2 3 3 1
#True
def two_length_run(l):
    '''
    (list)->boolean
    list must be only of type float or type integer
    determines if a number is repeated at least once
    '''
    counter=0
    while counter<len(l)-1:
        temp=l[counter]
        temp2=l[counter+1]
        if (temp==temp2):
            return_value=True
            counter=len(l)
        else:
            return_value=False
            counter=counter+1

    return(return_value)


raw_input=input("Please input a list of integers separated by spaces: ")
raw_input=raw_input.strip()
usable_input1=raw_input.split()
for inc in range(len(usable_input1)):
    usable_input1[inc]=float(usable_input1[inc])

print(two_length_run(usable_input1))