from trit import *

class trigit:
    alphabet = ['n','o','p','q','r','s','t','u','v','w','x','y','z','_',
                'a','b','c','d','e','f','g','h','i','j','k','l','m']

    def __init__(self,s):
        if type(s) == list and len(s) == 3 and all(isinstance(item,trit) for item in s):
            self.list = s
        elif type(s) == int and s >= -13 and s <= 13:
            self.fromInt(s)
        elif type(s) == str:
            if s in trigit.alphabet:
                self.fromChar(s)
            elif len(s) == 3:
                self.list = [trit(c) for c in s]
            else:
                raise TypeError('Invalid constructor input')
        else:
            raise TypeError('Invalid constructor input')

    def fromInt(self,n):
        n = n + 13
        self.list = [trit(n//9-1),trit(n//3%3-1),trit(n%3-1)]

    def fromChar(self,c):
        n = trigit.alphabet.index(c) - 13
        self.fromInt(n)

    def __str__(self,prefix=trinary_prefix):
        return prefix + trigit.alphabet[((self.list[0].d+1) * 9) + ((self.list[1].d+1) * 3) + (self.list[2].d+1)]

    def __repr__(self):
        return "trigit('%s')" % self.__str__('')

    def __eq__(self,other):
        try:
            assert(not isinstance(other,trigit))
            raise TypeError('Invalid arguments for __eq__: trigit and %s' % str(type(other).__name__))
        except AssertionError:
            return all(self.list[i] == other.list[i] for i in range(3))

    def __int__(self):
        return ((self.list[0].d) * 9) + ((self.list[1].d) * 3) + (self.list[2].d)

    def __add__(self, other):
        try:
            assert(not isinstance(other,trigit))
            raise TypeError('Invalid arguments for __add__: trigit and %s' % str(type(other).__name__))
        except AssertionError:
            out = []
            carry = trit(0)
            for i in range(2,-1,-1):
                add = self.list[i] + other.list[i]
                overflow = self.list[i].overflow(other.list[i])
                out.insert(0,carry + add)
                carry = overflow + carry.overflow(add)
            return trigit(out)

    def overflow(self, other):
        out = []
        carry = trit(0)
        for i in range(2,-1,-1):
            add = self.list[i] + other.list[i]
            overflow = self.list[i].overflow(other.list[i])
            out.insert(0,carry + add)
            carry = overflow + carry.overflow(add)
        return trigit([trit(0),trit(0),carry])

    def trits(self):
        return ''.join(str(trit) for trit in self.list)
