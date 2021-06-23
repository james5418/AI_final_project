import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
filename = ["BFS","Manhattan","H2+Manhattan","H3+Manhattan","H4+Manhattan","H5+Manhattan"]
# text = np.loadtxt("0.txt",dtype = str)
data = []
# for i in text[:,0:4]:
#     data.append((int(i[2]),int(i[3])))
# data = sorted(data,key = lambda x:x[1], reverse = False)
# print(data)
for j in filename:
    addr = j + ".txt"
    temp = []
    text = np.loadtxt(addr,dtype = str)
    for i in text[:,0:3]:
        temp.append((int(i[1]),int(i[2])))
    temp = sorted(temp ,key = lambda x:x[1], reverse = False)
    data.append(temp)
totaly = []

for j in range(0,6):
    y = []
    for i in range(0,100):
        pos = data[j][i]
        y.append(pos[0])
    totaly.append(y)
# plt.plot(index,compare)
avg = []
for i in totaly:
    avg.append(np.average(i))
# plt.savefig('lineChart.png', bbox_inches='tight')
# plt.show()
# ax=plt.gca()
# y_major_locator=MultipleLocator(100)
# ax.yaxis.set_major_locator(y_major_locator)
plt.yscale('log')
plt.bar(filename,avg,1,color=['crimson','maroon','darkorange','burlywood','gold','tan'])
for a,b in zip(filename,avg):  
 plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=11)  
plt.axhline(avg[0],ls = "--")
plt.xlabel("Heurisitc Function")
plt.ylabel("Number Of Expanded Nodes")
plt.show()