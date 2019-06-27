#======================================================================================================
# !/usr/bin/env python
# title          : LocalW2W_FWC_Run.py
# description    : Semiconductor Fab Wide Control using FDC, VM, R2R, L2L
# author         : Youngil Jung
# date           : 2019-06-17
# version        : v0.8
# usage          : python LocalW2W_FWC_Run.py
# notes          : Reference Paper "Virtual metrology and feedback control for semiconductor manufacturing"
# python_version : v3.5.3
#======================================================================================================
import numpy as np
from simulator.VM_Process1_시뮬레이터 import VM_Process1_시뮬레이터
from simulator.VM_Process2_시뮬레이터 import VM_Process2_시뮬레이터
from simulator.FDC_Graph import FDC_Graph
# from pandas import DataFrame, Series
# import pandas as pd
import os

os.chdir("D:/10. 대학원/04. Source/OnlyVM/01. Local VM/")

A_p1 = np.array([[0.5, -0.2], [0.25, 0.15]])    #recipe gain matrix
d_p1 = np.array([[0.1, 0], [0.05, 0]])  #drift matrix
C_p1 = np.transpose(np.array([[0, 0.5, 0.05, 0, 0.15, 0], [0.085, 0, 0.025, 0.2, 0, 0]])) # FDC variable matrix
# Process 변수와 출력 관련 system gain matrix

A_p2 = np.array([[1, 0.1], [-0.5, 0.2]])
d_p2 = np.array([[0, 0.05], [0, 0.05]])
C_p2 = np.transpose(np.array([[0.1, 0, 0, -0.2, 0.1], [0, -0.2, 0, 0.3, 0]]))
F_p2 = np.array([[2.5, 0], [0, 2.5]])
SEED = 1000000000
# Process 변수와 출력 관련 system gain matrix

def main():
    fdh_graph = FDC_Graph()
    fwc_p1_vm = VM_Process1_시뮬레이터(A_p1, d_p1, C_p1, SEED)
    fwc_p1_vm.DoE_Run(lamda_PLS=0.5, Z=12, M=10)  # DoE Run
    p1_VM_Output, p1_ACT_Output, p1_ez_run, p1_y_act, p1_y_prd = fwc_p1_vm.VM_Run(lamda_PLS=0.5, Z=40, M=10)

    p1_mape_Queue = []
    M = 10
    for z in np.arange(0, 40, 1):
        mape = fdh_graph.mean_absolute_percentage_error(z + 1, p1_y_act[((z + 1) * M) - 1][0],
                                                        p1_y_prd[((z + 1) * M) - 1][0])
        p1_mape_Queue.append(mape)
    print('Process-1 MAPE (%) : ', np.mean(p1_mape_Queue))

    fdh_graph.plt_show1(400, p1_y_act[:, 0:1], p1_y_prd[:, 0:1])
    fdh_graph.plt_show2(40 + 1, p1_ez_run[:, 0:1], p1_ez_run[:, 1:2])

    np.savetxt("output/VM_Output1.csv", p1_VM_Output, delimiter=",", fmt="%.4f")

    fwc_p2_act = VM_Process2_시뮬레이터(A_p2, d_p2, C_p2, F_p2, p1_VM_Output, p1_ACT_Output, SEED)
    fwc_p2_act.DoE_Run(lamda_PLS=0.5, Z=12, M=20, f=p1_ACT_Output)  #DoE Run ACT값으로 가능
    p2_VM_Output, p2_ACT_Output, p2_ez_run, p2_y_act, p2_y_prd = fwc_p2_act.VM_Run(lamda_PLS=0.5, Z=40, M=10)

    p2_mape_Queue = []
    M = 10
    for z in np.arange(0, 40, 1):
        mape = fdh_graph.mean_absolute_percentage_error(z + 1, p2_y_act[((z + 1) * M) - 1][0], p2_y_prd[((z + 1) * M) - 1][0])
        p2_mape_Queue.append(mape)
    print('Process-2 MAPE (%) : ', np.mean(p2_mape_Queue))

    # for i in np.arange(22 * M, 34 * M, 1):
    #     mape = fdh_graph.mean_absolute_percentage_error(i + 1, p2_y_act[i][1], p2_y_prd[i][1])
    #     p2_mape_Queue.append(mape)

    fdh_graph.plt_show1(400, p2_y_act[:, 1:2], p2_y_prd[:, 1:2])
    fdh_graph.plt_show2(40 + 1, p2_ez_run[:, 0:1], p2_ez_run[:, 1:2])

if __name__ == "__main__":
    main()
