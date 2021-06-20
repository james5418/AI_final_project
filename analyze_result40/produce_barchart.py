import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
filename = ["BFS","H2","H3","H4","Manhattan","H2+Manhattan","H3+Manhattan","H4+Manhattan","H5+Manhattan"]
# text = np.loadtxt("0.txt",dtype = str)
data = []
# for i in text[:,0:4]:
#     data.append((int(i[2]),int(i[3])))
# data = sorted(data,key = lambda x:x[1], reverse = False)
# print(data)
index = []
for i in range(1,101):
    index.append(i)
for j in filename:
    addr = j + ".txt"
    temp = []
    text = np.loadtxt(addr,dtype = str)
    for i in text[:,0:4]:
        temp.append((int(i[2]),int(i[3])))
    temp = sorted(temp ,key = lambda x:x[1], reverse = False)
    if j==0:
        print(temp)
    data.append(temp)

for i in range(1,101):
    index.append(i)

totaly = []
for j in range(0,9):
    y = []
    for i in range(0,100):
        pos = data[j][i]
        if j==0:
            y.append(pos[1])
        else :
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
plt.bar(filename,avg,1,color=['maroon','darkorange','burlywood','gold','tan','navajowhite','peru','orange','chocolate'])
plt.axhline(avg[0],ls = "--")
plt.savefig('BarChart.png', bbox_inches='tight')
plt.show()