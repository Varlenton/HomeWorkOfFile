class MyException1(Exception):
    def __init__(self, unp1, p2):
        self.unp1 = unp1
        self.p2 = p2

    def __str__(self):
        return f'not correct data {self.unp1} - first number'


class MyException2(Exception):
    def __init__(self, p1, unp2):
        self.p1 = p1
        self.unp2 = unp2

    def __str__(self):
        return f'not correct data {self.unp2} - second number'


class Summ:
    def __init__(self, p1, p2):
        unp1, unp2 = 10, 10
        if p1 != unp1:
            self.p1 = p1
        else:
            raise MyException1(unp1, p2)
        if p2 != unp2:
            self.p2 = p2
        else:
            raise MyException2(p1, unp2)

    def __str__(self):
        return f'This is result {self.p1 + self.p2}'


try:
    answer = Summ(10, 10)
except MyException1 as e:
    print(f'not correct number,', e)
except MyException2 as e:
    print(f' not correct number,', e)
