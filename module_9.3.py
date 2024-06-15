class EvenNumber:
    def __init__(self, start=0, end=1):
        self.start = start
        self.end = end
        print("После перебора и  вывода:")
        if start % 2 == 0:
            print(start)

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end - 1:
            count = self.start
            self.start += 1
            if count % 2 != 0:
                count += 1
                self.start += 1
                return count
            else:
                self.start += 1
                return self.start
        else:
            raise StopIteration


en = EvenNumber(10, 25)

for i in en:
    print(i)
