
def calculate_counter(m):
          
    n=1 #the first value is also the first step
    while m!=1:
        if m % 2 == 1:
            m = m * 3 + 1
        else:
            m = m / 2
        n = n + 1
    return n
    
if __name__ == '__main__':
    
    for m in range(1,10001):
        counter = calculate_counter(m)
        print("The sequence reaches 1 with the start value m={} after {} steps".format(m, counter))