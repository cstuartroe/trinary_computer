trinary_prefix = "T#"

class trit:
    def __init__(self,d):
        if d=='+' or d==1:
            self.d = 1
        elif d=='0' or d==0:
            self.d = 0
        elif d=='-' or d==-1:
            self.d = -1
        else:
            raise TypeError('Inappropriate digit')

    def __str__(self):
        return ['0','+','-'][self.d]

    def __repr__(self):
        return "trit('%s')" % str(self)

    def __eq__(self, other):
        try:
            assert(not isinstance(other,trit))
            raise TypeError('Invalid arguments for __eq__: trit and %s' % str(type(other).__name__))
        except AssertionError:
            return self.d == other.d

    def __int__(self):
        return self.d

    def __add__(self,other):
        try:
            assert(not isinstance(other,trit))
            raise TypeError('Invalid arguments for __add__: trit and %s' % str(type(other).__name__))
        except AssertionError:
            n = (self.d + other.d)%3
            return trit(-1 if n==2 else n)

    def overflow(self,other):
        if self == other:
            return trit(self.d)
        else:
            return trit(0)
