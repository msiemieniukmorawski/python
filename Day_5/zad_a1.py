a = list(range(100)) # utworzenie listy poprzez zrzutowanie generatora

print(a)
print(a[50])
print(a[50::2])
print(a[50:60:2]) # []

print(a[60:50:-2]) # efektem działania indeksowania jest nowa lista

print((a[40:50])[1:2])

a = list(range(100))
d = a[40:50][1:2]
b= a[40:50]
c = b[1:2]
e = b[1]


#####
a = [1,2,3]
b = ['inna_wartosc']
a[2] = b

b.append(5)
a[2].append(5)
print(a)
print(b)

a[2] = 8
print(a)
print(b)

del b