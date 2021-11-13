import cmath
from cmath import *

complex_num = complex(input().strip())
print(abs(complex_num))
print(phase(complex_num))


#2
import cmath
print(*cmath.polar(complex(input())), sep='\n')