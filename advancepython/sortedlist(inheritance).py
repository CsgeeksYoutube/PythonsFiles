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

    
sl= SortedList([4,5,2,3,6,9])
print(sl._items)
print(len(sl))
sl.add(-56)
print(sl._items)
sl.add(89)
print(sl._items)


