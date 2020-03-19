
def calculate_counter(m):
    
    if(m<1):
        #raise ValueError('The value number should be a natural number without zero')
        return None # In this case None means the number is out of range
         
    n=1 #the first value is also the first step
    while m!=1:
        if m % 2 == 1:
            m = m * 3 + 1
        else:
            m = m / 2
        n = n + 1
    return n
    
if __name__ == '__main__':
    
    #Please enter a number for m:
    m = 947
    counter = calculate_counter(m)
    print("The sequence reaches 1 with the start value m={} after {} steps".format(m, counter))