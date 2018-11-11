class A:
    counter = 1
    def __init__(self):
        print('Class A')
        self.increase()

    def increase(self, val=1):
        self.counter *= val
        print(self.counter)


class B(A):
    def __init__(self):
        super().__init__()
        print('Class B')
        self.increase(-2)


class C1(A):
    def __init__(self):
        super().__init__()
        print('Class C1')
        self.counter = 0


class C(C1):
    def __init__(self):
        super().__init__()
        print('Class C')
        self.increase(4)


class D(B,C):
    def __init__(self):
        super().__init__()
        print('Class D')
        self.increase(-1)

a = A()
print(15 * '-')
b = B()
print(15 * '-')
c = C()
print(15 * '-')
d = D()
