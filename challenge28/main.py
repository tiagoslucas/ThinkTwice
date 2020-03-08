import sys

def collatzLenUtil(n, collLenMap): 
      
    # If value already  
    # computed, return it 
    if n in collLenMap: 
        return collLenMap[n] 
      
    # Base case 
    if(n == 1): 
        collLenMap[n] = 1
  
    # Even case 
    elif(n % 2 == 0): 
        collLenMap[n] = 1 + collatzLenUtil(n//2, collLenMap) 
  
    # Odd case 
    else: 
        collLenMap[n] = 1 + collatzLenUtil(3 * n + 1, collLenMap) 
      
    return collLenMap[n] 
  
def collatzLen(n): 
      
    # Declare empty Map / Dict 
    # to store collatz lengths 
    collLenMap = {} 
      
    collatzLenUtil(n, collLenMap) 
  
    # Initalise ans and  
    # its collatz length 
    num, l =-1, 0
      
    for i in range(1, n): 
          
        # If value not already computed, 
        # pass Dict to Helper function 
        # and calculate and store value 
        if i not in collLenMap: 
            collatzLenUtil(i, collLenMap) 
          
        cLen = collLenMap[i] 
        if l < cLen: 
            l = cLen 
            num = i 
      
    # Return ans and  
    # its collatz length 
    return (num, l-1) 

with open(sys.argv[1], 'r') as input:
    n = input.read()

f = open('team15_ttwins/challenge28/result.txt', 'w')
f.write(str(collatzLen(int(n)))[1:-1].replace(',',''))
f.close()
