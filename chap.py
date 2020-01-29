#! usr/local/bin/python3

import numpy as np
########################
myar = np.zeros(1000000)
index = 0
inte = 1
while myar[999999] == 0:
    mystr = str(inte)
    for i in range(len(mystr)):
        myar[index] = mystr[i]
        if index > 999998:
            break
        else:
            index +=1
    inte +=1
print(myar[0]*myar[9]*myar[99]*myar[999]*myar[9999]*myar[99999]*myar[999999])
