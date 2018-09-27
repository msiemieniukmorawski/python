a = [1,2,0,4,5,6,7,7,7,1,2,9]
b = [''] * 10

for ii in a:
    b[ii] += '#'

i=0
for ii in b:

    print(i,' ', ii)
    i += 1