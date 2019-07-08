import numpy as np
from matplotlib import pyplot as plt

class FDC_Graph:

    def plt_show1(self, n, y_act, y_prd):
        plt.figure()
        plt.plot(np.arange(n), y_act, 'rx--', y_prd, 'bx--', lw=2, ms=5, mew=2)
        plt.xticks(np.arange(0, n + 1, 50))
        plt.xlabel('Run No.')
        plt.ylabel('Actual and Predicted Response (y1)')

    def plt_show2(self, n, y1, y2):
        plt.figure()
        plt.plot(np.arange(0, n + 1, 1), y1, 'bx-', y2, 'gx--', lw=2, ms=5, mew=2)
        plt.xticks(np.arange(0, n + 1, 5))
        plt.yticks(np.arange(-1.2, 1.3, 0.2))
        plt.xlabel('Metrology Run No.(z)')
        plt.ylabel('e(z)')

    def plt_show3(self, n, y1, y2):
        plt.figure()
        plt.plot(np.arange(n), y1, 'bx-', y2, 'gx--', lw=2, ms=5, mew=2)
        plt.xticks(np.arange(0, n + 1, 5))
        plt.yticks(np.arange(-12, 3, 2))
        plt.xlabel('Metrology Run No.(z)')
        plt.ylabel('e(z)')

    def plt_show4(self, n, y1):
        plt.figure()
        plt.plot(np.arange(n), y1, 'rx-', lw=2, ms=5, mew=2)
        plt.xticks(np.arange(0, n + 1, 5))
        plt.yticks(np.arange(-1.2, 1.3, 0.2))
        plt.xlabel('Metrology Run No.(z)')
        plt.ylabel('e(z)')

    def mean_absolute_percentage_error(self, z, y_act, y_prd):
        #print('z: ', z, 'y_act : ', y_act, 'y_prd : ', y_prd)
        mape = np.mean(np.abs((y_act - y_prd) / y_act)) * 100
        #print('mape : ', mape)
        return mape
