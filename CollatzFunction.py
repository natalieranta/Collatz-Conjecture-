'''
Program for collatz without optimization to show plot
The formula for the Collatz conjecture is executed until 1 is reached.
User inputs a number n. The numbers from 1 to n and their corresponding stopping time are outputted and plotted
'''
import matplotlib.pyplot as plt

nums = []  #stores numbers from 1 to n, where n is chosen 
Map = {}   #dictionary to store already checked values (could also be an array but faster access time in dictionary) 
run = True #boolean to run iterations 

def collatz(n):
    i = 0
    while n != 1:
        
        if n % 2 == 0:
            n /= 2
        else:
            n = 3*n + 1
        i = i+1

    nums.append(i)

while run:
    n = int(input('Enter number: '))
    temp = range(1, n+1)
    
    if n == -1:
        break
    
    for j in temp: 
        collatz(j)
    #incrementing through the array
        
    k = 0    
    while k < len(nums):
        print ('iterations for n =',k+1,':', nums[k])
        k +=1
    print('--------------------------------')
    print ('total iterations: ', sum(nums))

    plt.plot(range(1,n+1), nums, 'go', markersize=1, linewidth =1)
    plt.xlabel('Number Entered, incrementing') 
    plt.ylabel('Iterations to each 1')
    plt.show()
    break
    #this plot is without the optimized algorithm 



