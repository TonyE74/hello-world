import numpy as np
import math

msg = "Roll a dice!!"
print(msg)

msg = msg.upper()
print(msg)

print(np.random.randint(1,25))

#Determine root 2
rt2 = (10/7)*( 1 - 10**-2 - (1/2)*10**-4 - (1/2)*10**-6 )
print(rt2)
print(rt2 - math.sqrt(2))

#Determine root 3
rt3 = 2*(1+0.5*-0.25+0.5*-0.5*0.25/2)
print(rt3)
print(rt3 - math.sqrt(3))

#Determine pi
mypi = 4*(1 - 1/6 - 1/40 - 1/112 - 5/1152)
print('Pi')
print(mypi)
print(mypi - math.pi)

print('pi2 when intergrating to a half')
mypi2 = 12*(0.5 - 0.5*(1/3)*(1/2)**3 - (1/8)*(1/5)*(1/2)**5 - (1/16)*(1/7)*(1/2)**7 - (5/128)*(1/9)*(1/2)**9 - math.sqrt(3)/8 )
print(mypi2)
print(mypi2 - math.pi)
# end
