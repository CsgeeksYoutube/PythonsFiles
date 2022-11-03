class SimpleList:
    def __init__(self,items):
        self._items = list(items)
    
    def add(self,item):
        self._items.append(item)
    
    def __getitem__(self,index):
        return self._items[index]
    def sort(self):
        self._items.sort()
    
    def __len__(self):
        return len(self._items)
      
class SortedList(SimpleList):
    def __init__(self,items=()):
        super().__init__(items)
        self.sort()
    
    def add(self, item):
        super().add(item)
        self.sort()

class IntList(SimpleList):
    def __init__(self,items=()):
        for x in items: self._validate(x)
        super().__init__(items)
    
    @staticmethod
    def _validate(x):
        if not isinstance(x,int):
            raise TypeError('intlist only support interger value')
    
    def add(self,item):
        self._validate(item)
        super().add(item)

class SortedIntList(IntList, SortedList):
    pass

print(SortedIntList.mro())
sil=SortedIntList([5,15,10])
sil.add(6)
print(sil._items)




# super(SortedList, SortedIntList).add(4)

# super(SortedIntList, SortedIntList)._validate(5)
# sil=SortedIntList([5,15,10])
# super(SortedList, sil).add('6')
# print(sil._items)





# print(SortredIntList.__mro__)
# print(SortredIntList.mro())

# il= IntList([1,2,3,4])
# il.add(19)
# print(il._items)
# il.add('5')

# print(issubclass(IntList, SimpleList))
# print(issubclass(SortedList, IntList))

# sil= SortredIntList([42,23,2])
# print(sil._items)
# sil.add(-1234)
# print(sil._items)
# sil.add('hello frnds')

# print(SortredIntList.__bases__)
# print(IntList.__bases__)