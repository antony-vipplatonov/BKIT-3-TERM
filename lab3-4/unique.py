from gen_random import gen_random


class Unique(object):
    def __init__(self, items, **kwargs):
        self.ignore = kwargs.get("ignore_case", False)
        self.items = list(items)
        self.were = []
        self.n = 0

    def __next__(self):
        while (self.n < len(self.items)):
            one = self.items[self.n]
            if (self.ignore):
                if str(one).lower() not in self.were:
                    self.were.append(str(one).lower())
                    self.n += 1
                    return one
                else:
                    self.n += 1
            else:
                if one not in self.were:
                    self.were.append(one)
                    self.n += 1
                    return one
                else:
                    self.n += 1
        raise StopIteration

    def __iter__(self):
        return self


'''
data = list(gen_random(10, 1, 3))
print(data)
i = iter(Unique(list(data)))
for elem in i:
    print(elem)
data1 = ['a', 'A', 'B', 'b', 'a', 'A', 'B', 'b']
print(data1)
j = iter(Unique(data1))
for elem in j:
    print(elem)
print(data1)
k = iter(Unique(data1, ignore_case=True))
for elem in k:
    print(elem)
'''
