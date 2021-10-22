'''Selection sort
1. set the first element as your minimun
2. loop through the unsorted list:
    if element < minimum:
       Minimun = element
3. change positions of minimum and start of the unsorted list
4. repeat 1-3 for number o times equal to length of list

Input: unsorted list (make it up)
Output: return sorted list '''
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

    Ahh = [17, 3, 23, 14, 11, 18, 12, 7, 123]
    print(Ahh)
    print(sort(Ahh))
 
if __name__ == "__main__":
    main()

    
