# Iterative function 
def lucas(n) : 
  
    # declaring base values 
    # for positions 0 and 1 
    a = 2
    b = 1
      
    if (n == 0) : 
        return a 
   
    # generating number 
    for i in range(2, n + 1) : 
        c = a + b 
        a = b 
        b = c 
      
    return b 

with open(sys.argv[1], 'r') as input:
    n = input.read()

f = open('team15_ttwins/challenge29/result.txt', 'w', encoding='utf8')
f.write(lucas(n))
f.close()