'''Selection sort
1. set the first element as your minimun
2. loop through the unsorted list:
    if element < minimum:
       Minimun = element
3. change positions of minimum and start of the unsorted list
4. repeat 1-3 for number o times equal to length of list

Input: unsorted list (make it up)
Output: return sorted list '''

import time
import random
def sort(x):
    f = 0
    #first value to compare it to

    for i in range (len(x)):
        #when i is the value of the element in the list that its working with dudes
        f = x[i]
        for y in range (len(x)):
            if (y>i):
                if (x[y]<f):
                    f = x[y]
                    l = y

        if (f != x[i]):
            # != is not equal because when f isn't equal to x[i] do stuff later
            x[l]=x[i]
            x[i]=f

    return x
        

def main():
    diffList = []
    for i in range(10):



        
        Ahh = []
        n = 500

        for i in range(n):
            Ahh.append(random.randint(1,n))
              
        start = time.time()
        results = sort(Ahh)
        stop = time.time()
        diff = stop - start
        diffList.append(diff)
    print(diffList)
    total = 0
    for dif in diffList:
        total = total + dif
    avgTime = total/10
    print("\n The average time to Selection Sort this list was " + str(avgTime) + " seconds!")
    
    print(results)
        
 
if __name__ == "__main__":
    main()

    
