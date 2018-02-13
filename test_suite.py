from tryte import *

#trit str init
w = trit('-')
x = trit('+')
#trit int init
y = trit(0)
z = trit(1)

#trit str
assert(str(y) == '0')
#trit int
assert(int(w) == -1)
#trit eq
assert(x == z)
assert(y != w)
#trit add
assert(x + y == z)
assert(w + x == trit('0'))

#trigit list init
tg = trigit([w,y,z])
#trigit str init
tg2 = trigit('s')
#trigit int init
tg3 = trigit(5)

#trigit str
assert(str(tg3) == 'T#e')
#trigit int
assert(int(tg2) == -8)
#trigit eq
assert(tg == tg2)
assert(tg != tg3)
#trigit add
assert(tg + tg2 == trigit('k'))

#tryte list init
te = tryte([tg,tg2,tg3])
#tryte str init
te2 = tryte('sse')
#tryte int init
te3 = tryte(362)

#tryte str
assert(str(te3) == 'T#_mk')
#tryte int
assert(int(te) == -6043)
#tryte eq
assert(te == te2)
assert(te != te3)
#tryte add
assert(te + te3 == tryte(-5681))
