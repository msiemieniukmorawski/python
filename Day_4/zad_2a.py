a = [1,2,0,4,5,6,7,7,7,1,2,9]
b = [''] * 10

for ii in a:
    b[ii] += 'x'
    print(b[ii])