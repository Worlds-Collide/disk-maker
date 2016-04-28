from __future__ import division, print_function
from diskmaker.create import calcSemis, createBigin

totalmass = 5.0
smallmass = 0.01
largemass = 0.1
nsmallbodies = 260
inner = 0.2
outer = 4.0
alpha = 3./2.

with open('tmp','w') as obj:
    print(createBigin(totalmass, smallmass,largemass, 
        nsmallbodies, inner, outer, alpha), file=obj)
