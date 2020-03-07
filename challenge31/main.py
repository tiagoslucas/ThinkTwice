import sys

def zeros_matrix(rows, cols):
    A = []
    for i in range(rows):
        A.append([])
        for j in range(cols):
            A[-1].append(0.0)

    return A

def copy_matrix(M):
    rows = len(M)
    cols = len(M[0])

    MC = zeros_matrix(rows, cols)

    for i in range(rows):
        for j in range(cols):
            MC[i][j] = M[i][j]

    return MC

def matrix_multiply(A,B):
    rowsA = len(A)
    colsA = len(A[0])

    rowsB = len(B)
    colsB = len(B[0])

    if colsA != rowsB:
        sys.exit()

    C = zeros_matrix(rowsA, colsB)

    for i in range(rowsA):
        for j in range(colsB):
            total = 0
            for ii in range(colsA):
                total += A[i][ii] * B[ii][j]
            C[i][j] = total

    return C

with open(sys.argv[1], 'r', encoding='utf8') as f:
    line = f.readline()
    A = []
    B = []
    while line:
        dic = {'x':0, 'y':0, 'ind': 0}
        line = line.split()
        sinal = 1
        for arg in line:
            if '=' in arg:
                sinal = -1
            elif 'x' in arg:
                if len(arg) == 1:
                    dic['x'] += (1*sinal)
                else:
                    dic['x'] += (int(arg.split('x')[0])*sinal)
            elif 'y' in arg:
                if len(arg) == 1:
                    dic['y'] += (1*sinal)
                else:
                    dic['y'] += (int(arg.split('y')[0])*sinal)
            elif arg.isnumeric():
                dic['ind'] += (int(arg)*sinal)
            if(dic['ind'] != 0):
                dic['ind'] = -dic['ind']
        A.append([dic['x'], dic['y']])
        B.append([dic['ind']])
        line = f.readline()
    
    AM = copy_matrix(A)
    n = len(A)
    BM = copy_matrix(B)

    indices = list(range(n)) # allow flexible row referencing ***
    for fd in range(n): # fd stands for focus diagonal
        if AM[fd][fd] == 0:
            break
        fdScaler = 1.0 / AM[fd][fd]
        # FIRST: scale fd row with fd inverse. 
        for j in range(n): # Use j to indicate column looping.
            AM[fd][j] *= fdScaler
        BM[fd][0] *= fdScaler
        
        # Section to print out current actions:
        string1  = '\nUsing the matrices above, '
        string1 += 'Scale row-{} of AM and BM by '
        string2  = 'diagonal element {} of AM, '
        string2 += 'which is 1/{:+.3f}.\n'
        stringsum = string1 + string2
        val1 = fd+1; val2 = fd+1
        Action = stringsum.format(val1,val2,round(1./fdScaler,3))
        
        # SECOND: operate on all rows except fd row.
        for i in indices[0:fd] + indices[fd+1:]: # *** skip fd row.
            crScaler = AM[i][fd] # cr stands for "current row".
            for j in range(n): # cr - crScaler*fdRow.
                AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
            BM[i][0] = BM[i][0] - crScaler * BM[fd][0]
            
            # Section to print out current actions:
            string1  = 'Using matrices above, subtract {:+.3f} *'
            string1 += 'row-{} of AM from row-{} of AM, and '
            string2 = 'subtract {:+.3f} * row-{} of BM '
            string2 += 'from row-{} of BM\n'
            val1 = i+1; val2 = fd+1
            stringsum = string1 + string2
            Action = stringsum.format(crScaler, val2, val1, 
                                    crScaler, val2, val1)

f = open('team15_ttwins/challenge31/result.txt', 'w')
if int(BM[0][0]) == 0 or int(BM[1][0]) == 0:
    f.write(str("don't know")+'\n')
    f.write(str("don't know"))
else:
    f.write(str(int(BM[0][0]))+'\n')
    f.write(str(int(BM[1][0])))
f.close()
