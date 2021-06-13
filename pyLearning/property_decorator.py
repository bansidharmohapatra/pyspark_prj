class Alfabate:
    def __init__(self,value):
        self._value =value
    @property
    def value(self):
        print("value getting")
        return self._value
    @value.setter
    def value(self,value):
        print("value setting")
        self._value=value
    @value.deleter
    def value(self):
        print("value deleting")
        del self._value

letter= Alfabate("GodShiva")
print(letter.value)
letter.value="Paramdham"
print(letter.value)

