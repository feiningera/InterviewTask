
def calculate_counter(m):
    
    temp = m-1
    n=0
    while m>=m_max or steps[m-1]==None:
        if m % 2 == 1:
            m = m * 3 + 1
        else:
            m = m // 2
        n = n + 1     
    steps[temp] = n + steps[m-1]
    return steps[temp]
    
if __name__ == '__main__':
    
    m_max = 10000
    steps = [None] * m_max
    steps[0] = 1
    
    for m in range(2,m_max+1):
        counter = calculate_counter(m)
        print("The sequence reaches 1 with the start value m={} after {} steps".format(m, counter))