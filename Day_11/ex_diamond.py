class A:
    def __init__(self):
        super().__init__()
        print('Class A')

class B(A):
    def __init__(self):
        super().__init__()
        print('Class B')

class C:#(A):
    def __init__(self):
        super().__init__()
        print('Class C')

class D(B,C):
# class D(C,B):
    def __init__(self):
        super().__init__()
        print('Class D')

a = A()
print(15 * '-')
b = B()
print(15 * '-')
c = C()
print(15 * '-')
d = D()
