'''
REVERSED OUTER LOOP

This program tests numbers from 1 to n in decreasing order to see if they reach 1
by the collatz conjecture. If a number is reached during the collatz function that
has already been proved to reach 1 it is skipped. total iterations are plotted for each n
from 1 to n. (Utilizes recursive nature of conjecture)
'''
import matplotlib.pyplot as plt

nums = []  #stores numbers from 1 to n, where n is chosen 
Map = {}   #dictionary to store already checked values (could also be an array but faster access time in dictionary) 
run = True #boolean to run iterations 

def isInList(n):
    
    try:
        Map[n]
        return True 
    except:
        return False
    #to see if the number has already been checked in the collatz function 
   
def collatz(n):
    i = 0
    while n != 1 and not isInList(n):
        
        Map[n] = n
        
        if n % 2 == 0:
            n /= 2
        else:
            n = 3*n + 1
        i = i + 1

    nums.append(i)

while run:
    n = int(input('Enter number: '))
    
    if n == -1:
        break
    
    for j in range(n,1,-1): 
        collatz(j)
    #decrementing through the array
        
    k = 0 
    while k < len(nums):
        print ('iterations for n =',n-k,':', nums[k])
        k +=1
    print('--------------------------------')
    print ('total iterations: ', sum(nums))

    plt.plot(range(n,1,-1), nums, 'bo', markersize=1, linewidth =1)
    markerline, stemlines, baseline = plt.stem(range(n,1,-1), nums,'b', linefmt = 'b-.', markerfmt = ' ', basefmt = '-b' )
    plt.setp(stemlines, 'linewidth', .5 )
    plt.xlabel('Number Entered, Incrementing') 
    plt.ylabel('Iterations to Reach 1')
    plt.show()
    #plot the result from 1 to n 

