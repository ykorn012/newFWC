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
from simulator.VM_Process1_DynamicSampling_시뮬레이터 import VM_Process1_DynamicSampling_시뮬레이터
from simulator.FDC_Graph import FDC_Graph
# from pandas import DataFrame, Series
# import pandas as pd
import os
from matplotlib import pyplot as plt

os.chdir("D:/10. 대학원/04. Source/OnlyVM/10. DynamicSampling/")

A_p1 = np.array([[0.5, -0.2], [0.25, 0.15]])    #recipe gain matrix
d_p1 = np.array([[0.1, 0], [0.05, 0]])  #drift matrix
C_p1 = np.transpose(np.array([[0, 0.5, 0.05, 0, 0.15, 0], [0.085, 0, 0.025, 0.2, 0, 0]])) # FDC variable matrix
SEED = 1  #3

M = 10
Z_DoE = 12
Z_VM = 55
Nz_RUN = 15
v_PLS = 1
dM = 5
dStart = 26  #25 * 10 + 30 * 5

# Process 변수와 출력 관련 system gain matrix

def main():
    fdh_graph = FDC_Graph()
    fwc_p1_vm = VM_Process1_DynamicSampling_시뮬레이터(A_p1, d_p1, C_p1, dM, dStart, SEED)
    fwc_p1_vm.DoE_Run(lamda_PLS=v_PLS, Z=Z_DoE, M=M)  #DoE Run
    VM_Output, ACT_Output, ez_run, y_act, y_prd = fwc_p1_vm.VM_Run(lamda_PLS=v_PLS, Z=Z_VM, M=M)

    np.savetxt("output/VM_Output.csv", VM_Output, delimiter=",", fmt="%.4f")
    np.savetxt("output/ACT_Output.csv", ACT_Output, delimiter=",", fmt="%.4f")
    np.savetxt("output/ez_run.csv", ez_run, delimiter=",", fmt="%.4f")
    np.savetxt("output/y_act.csv", y_act, delimiter=",", fmt="%.4f")
    np.savetxt("output/y_prd.csv", y_prd, delimiter=",", fmt="%.4f")

    fdh_graph.plt_show1(40 * M, y_act[:, 0:1], y_prd[:, 0:1])
    fdh_graph.plt_show2(55, ez_run[:, 0:1], ez_run[:, 1:2])

    ez_run_out = []

    for z in range(Z_VM):
        if z == dM:
            M = dM
        for k in np.arange(z * M, (z + 1) * M):
            ez_run_out[k] = ez_run[z]

if __name__ == "__main__":
    main()
