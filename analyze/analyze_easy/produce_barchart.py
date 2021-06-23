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
colors = {"BFS":'crimson',"Manhattan":'maroon',"H2+Manhattan":'darkorange',"H3+Manhattan":'burlywood',"H4+Manhattan":'gold',"H5+Manhattan":'tan'}
plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False)
labels = list(colors.keys())
handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]
plt.legend(handles, labels,loc='right',fontsize = 20)
plt.xlabel("Heurisitc Function",fontsize=25)
plt.ylabel("Number Of Expanded Nodes",fontsize=25)
plt.show()