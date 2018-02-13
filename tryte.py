from trigit import *

class tryte:
    def __init__(self,s):
        if type(s) == list and len(s) == 3 and all(isinstance(item,trigit) for item in s):
            self.list = s
        elif type(s) == int and s >= -9841 and s <= 9841:
            s = s + 9841
            self.list = [trigit(s//729-13),trigit(s//27%27-13),trigit(s%27-13)]
        elif type(s) == str and len(s) == 3:
            self.list = [trigit(c) for c in s]
        else:
            raise TypeError('Invalid constructor input')

    def __str__(self,prefix=trinary_prefix):
        return prefix + ''.join([tg.__str__('') for tg in self.list])

    def __repr__(self):
        return "tryte('%s')" % self.__str__('')

    def __eq__(self, other):
        try:
            assert(not isinstance(other,tryte))
            raise TypeError('Invalid arguments for __eq__: tryte and %s' % str(type(other).__name__))
        except AssertionError:
            return all(self.list[i] == other.list[i] for i in range(3))

    def __int__(self):
        return (int(self.list[0]) * 729) + (int(self.list[1]) * 27) + int(self.list[2])

    def __add__(self, other):
        try:
            assert(not isinstance(other,tryte))
            raise TypeError('Invalid arguments for __add__: tryte and %s' % str(type(other).__name__))
        except AssertionError:
            out = []
            carry = trigit(0)
            for i in range(2,-1,-1):
                add = self.list[i] + other.list[i]
                overflow = self.list[i].overflow(other.list[i])
                out.insert(0,carry + add)
                carry = overflow + carry.overflow(add)
            return tryte(out)

    def overflow(self, other):
        try:
            assert(not isinstance(other,tryte))
            raise TypeError('Invalid arguments for __add__: tryte and %s' % str(type(other).__name__))
        except AssertionError:
            out = []
            carry = trigit(0)
            for i in range(2,-1,-1):
                add = self.list[i] + other.list[i]
                overflow = self.list[i].overflow(other.list[i])
                out.insert(0,carry + add)
                carry = overflow + carry.overflow(add)
            return tryte([trigit(0),trigit(0),carry])

    def trits(self):
        return ''.join(trigit.trits() for trigit in self.list)
