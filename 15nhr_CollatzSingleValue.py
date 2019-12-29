'''This program is the un-optimized collatz code that shows the pattern of
convergence to 1 for any n'''

import matplotlib.pyplot as plt
run = True
vals = []


def collatz(n):
    i = 0    
    while n != 1:
        
        if n % 2 == 0:
            n /= 2
        else:
            n = 3*n + 1
            
        vals.append(n)  
        i = i + 1
    print(vals)   
#runs the collatz function and stores the values it reaches in vals[]
    
while run:
    n = int(input('Enter number: '))
    collatz(n)
    if n == -1:
        break
    
    plt.plot(range(0,len(vals)), vals,'r--o', markersize = 1,linewidth = .5)
    plt.xlabel('iteration') 
    plt.ylabel('values')
    plt.show()
#plots the values the number reaches as it undergoes the collatz function 
