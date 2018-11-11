a = [1,2,0,4,5,6,7,7,7,7,1,2,]
b = [''] * 10
print(b)

for ii in a:
    b[ii] += 'x'

print(f'b: {b}')


cc = [0] * 10
for ii in a:
    cc[ii] += 1

c = [0] * 10
for ii, elem in enumerate(cc):
    c[ii] = 'x'*elem

print(f'c: {c}')

d = ['x'*ii for ii in cc]
print(f'd: {d}')
dd = []
for ii in cc:
    dd.append('x'*ii)

e = [None] * 10
for ii in cc:
    e[ii] = 'x'*ii

print(f'e: {e}')
"""
0: x
1: xx
2 xx
3: 
"""