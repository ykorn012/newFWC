import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm
import pandas as pd


num_classes = 4
ts = range(10)
df = pd.DataFrame(data={'TOTAL': np.random.rand(len(ts)), 'Label': np.random.randint(0, num_classes, len(ts))}, index=ts)
print(df)

cmap = ListedColormap(['r', 'g', 'b', 'y'])
norm = BoundaryNorm(range(num_classes+1), cmap.N)
points = np.array([df.index, df['TOTAL']]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)

lc = LineCollection(segments, cmap=cmap, norm=norm)
lc.set_array(df['Label'])

fig1 = plt.figure()
plt.gca().add_collection(lc)
plt.xlim(df.index.min(), df.index.max())
plt.ylim(-1.1, 1.1)
plt.show()
