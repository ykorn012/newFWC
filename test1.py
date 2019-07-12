#https://stackoverflow.com/questions/48393080/plot-multicolored-time-series-plot-based-on-conditional-in-python

import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm
import numpy as np
import pandas as pd
import os

M = 10
S1 = 25
dM = 5
S2 = 30
RUNS_CNT = S1 + S2
N = M * S1 + dM * S2
dStart = 25  #25 * 10 + 30 * 5
Z_DoE = 12
Nz_RUN = 15
v_PLS = 0.8

os.chdir("D:/10. 대학원/04. Source/OnlyVM/10. DynamicSampling/")
ez_run_out = np.loadtxt('output/ez_run2.csv', delimiter=',')
df = pd.read_csv('output/ez_run2.csv', sep=',', header=None, names=['q1', 'q2'])

label = []
for i in np.arange(10, N + dM , 1):
    if i <= S1 * M:
        label.append(0)
    else:
        label.append(1)
df['label'] = pd.Series(label)
df.loc[261]['label']

xdata = []
y1data = []
y2data = []
ldata = []

plt.figure()

axes = plt.gca()
# axes.set_xlim(0, N)
# axes.set_ylim(-1.2, 1.2)
line1, = axes.plot(xdata, y1data, 'bx-', lw=2, ms=5, mew=2)
line2, = axes.plot(xdata, y2data, 'gx--', lw=2, ms=5, mew=2)

for i in np.arange(0, N + dM , 1):
    if i <= S1 * M and i % M == 0:
        xdata.append(i)
        y1data.append(df.loc[i]['q1'])
        y2data.append(df.loc[i]['q2'])
        ldata.append(0)
        # line1.set_xdata(xdata)
        # line1.set_ydata(y1data)
        # line2.set_xdata(xdata)
        # line2.set_ydata(y2data)
    if i > S1 * M and i % dM == 0:
        xdata.append(i)
        y1data.append(df.loc[i]['q1'])
        y2data.append(df.loc[i]['q2'])
        ldata.append(1)
        # line1.set_xdata(xdata)
        # line1.set_ydata(y1data)
        # line2.set_xdata(xdata)
        # line2.set_ydata(y2data)

#line1.set_xdata(xdata)
#line1.set_ydata(y1data)
# line2.set_xdata(xdata)
# line2.set_ydata(y2data)

#plt.show()

df2 = pd.DataFrame(np.array([xdata, y1data, y2data, ldata]))
df2 = df2.T
df2.columns = ['no', 'q1', 'q2', 'label']

num_classes = 2
#cmap = ListedColormap(['r', 'g', 'b', 'y'])
cmap = ListedColormap(['b', 'r'])
norm = BoundaryNorm(range(num_classes+1), cmap.N)
points = np.array([df2['no'], df2['q1']]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
lc = LineCollection(segments, cmap=cmap, norm=norm)
lc.set_array(df2['label'])

#fig1 = plt.figure()

plt.gca().add_collection(lc)
# plt.xlim(df.index.min(), df.index.max())
# plt.ylim(-1.1, 1.1)
plt.xlabel('Metrology Run No.(z)')
plt.ylabel('e(z)')
#plt.xticks(np.arange(0, 410, 50))
ticks = np.arange(0, 400, 50)
plt.xticks(ticks)
plt.yticks(np.arange(-1.2, 1.3, 0.2))

dic = {50 : "50 \n (5 runs)", 100: "100 \n (10 runs)", 150: "150 \n (15 runs)", 200: "200 \n (20 runs)",
       250: "250 \n (25 runs)", 300: "300 \n (35 runs)", 350: "350 \n (45 runs)", 400: "400 \n (55 runs)"}
labels = [ticks[i] if t not in dic.keys() else dic[t] for i,t in enumerate(ticks)]
axes.get_xticklabels()

i = 0
for text in axes.get_xticklabels():
    if i >= 5:
        text.set_color("red")
    i = i + 1

#ax = fig1.add_subplot(111)
axes.set_xticklabels(labels)
#axes.set_color_cycle(colors)
plt.tight_layout()

plt.show()

