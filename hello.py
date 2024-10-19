import numpy as np
import math

msg = "Roll a dice!!"
print(msg)

msg = msg.upper()
print(msg)

print(np.random.randint(1,25))

#Determine root 2
rt2 = (10/7)*( 1 - 10**-2 - (1/2)*10**-4 - (1/2)*10**-6 )
print(rt2 - math.sqrt(2))
