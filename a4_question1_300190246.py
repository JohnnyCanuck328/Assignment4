#finds the number of ints divisible by n i.e.
#Please input a list of integers separated by spaces: 2 2 1 4 3
# Please input an integer: 2
#The number of elements divisible by 2 is 3
def number_divisible(int_list,n):
    '''
    (list, int)->int
    list must contain only integers and n must be non zero
    returns the number of numbers in the list divisible by the integer give
    '''
    if (n!=0):
        counter=0
        for inc in int_list:
            if (inc%n==0):
                counter=counter+1

        return(counter)
    else:
        print("Division by zero is not possible")



raw_input=input("Please input a list of integers separated by spaces: ")
raw_input=raw_input.strip()
usable_input1=raw_input.split()
for inc in range(len(usable_input1)):
    usable_input1[inc]=int(usable_input1[inc])

usable_input2=int(input("Please input an integer: "))

print("The number of elements divisible by", usable_input2,"is", number_divisible(usable_input1,usable_input2))