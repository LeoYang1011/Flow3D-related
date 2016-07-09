import re
import matplotlib.pyplot as pl

porbe_file = open('1234.txt')

m_porbe = re.compile(r'(\d+\.\d{7}E(\+|\-)\d+)')

time = list()
porbe_ave = list()
porbe1 = list()
porbe2 = list()
porbe3 = list()

for eachline in porbe_file:

    temp = re.findall(m_porbe,eachline)

    if len(temp) == 4:
        time.append(float(temp[0][0]))
        porbe1.append(float(temp[1][0]))
        porbe2.append(float(temp[2][0]))
        porbe3.append(float(temp[3][0]))
        porbe_ave.append((float(temp[1][0])+float(temp[2][0])+float(temp[3][0]))/3.0)

pl.figure(facecolor='w')
pl.plot(time,porbe1,label = '$x = 22.5m$')
pl.plot(time,porbe2,label = '$x = 25m$')
pl.plot(time,porbe3,label = '$x = 27.5m$')
pl.plot(time,porbe_ave,label = '$ mean $')
pl.xlabel('Time(s)')
pl.ylabel('DO concentration($mg/m^3$)')
pl.legend(loc='upper left')
pl.show()
