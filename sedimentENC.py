import re
import numpy as np
import matplotlib.pyplot as pl

dataFile = open('packed sediment elevation net change.txt','r')

timeTarget = re.compile(r't=\d+\.\d+E?\+?(\d+)?')
dataTarget = re.compile(r'(\-?\d+\.\d{7}E(\+|\-)\d+)')
data = list()
totalData = list()
time = list()
xDis = list()

index = 0

for eachLine in dataFile:
    t = re.search(timeTarget, eachLine)
    if t:
        if data:
            totalData.append(tuple(data))
            data = []
            index = index + 1
        time.append(float(t.group(0)[2:]))


    dataLine = re.findall(dataTarget, eachLine)
    print(dataLine)
    if len(dataLine) == 4:
        data.append(float(dataLine[3][0]))
        if index == 0:
            xDis.append(float(dataLine[0][0]))


totalData.insert(0,tuple(xDis))

totalData = np.array(totalData)

totalData = np.transpose(totalData)

time = np.array(time)

np.savetxt("result.txt", totalData)

np.savetxt("time.txt", time)

dataFile.close()


#pl.figure(facecolor='w')
#pl.plot(time,scl)
#pl.xlabel('Time(s)')
#pl.ylabel('DO concentration($mg/m^3$)')
#pl.show()
