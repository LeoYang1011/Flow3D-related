import re
import numpy as np
import matplotlib.pyplot as pl

f_read = open('123.txt','r')

m_t = re.compile(r't=\d+\.\d+E?\+?(\d+)?')
m_data = re.compile(r'(\d+\.\d{7}E(\+|\-)\d+)')
data = list()
scl = list()
time = list()

for eachLine in f_read:
    list_t = re.search(m_t, eachLine)
    if list_t:
        if data:
            scl.append(np.mean(data))
            data = []
        time.append(float(list_t.group(0)[2:]))

    list_line = re.findall(m_data, eachLine)
    if len(list_line) == 4 and abs(float(list_line[3][0])-0.0) > 1e-4:
        data.append(float(list_line[3][0]))
scl.append(np.mean(data))

time = time[0:len(time):2]
scl = scl[0:len(scl):2]

pl.figure(facecolor='w')
pl.plot(time,scl)
pl.xlabel('Time(s)')
pl.ylabel('DO concentration($mg/m^3$)')
pl.show()
