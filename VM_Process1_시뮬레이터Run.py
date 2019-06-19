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
# from pandas import DataFrame, Series
# import pandas as pd

A_p1 = np.array([[0.5, -0.2], [0.25, 0.15]])    #recipe gain matrix
d_p1 = np.array([[0.1, 0], [0.05, 0]])  #drift matrix
C_p1 = np.transpose(np.array([[0, 0.5, 0.05, 0, 0.15, 0], [0.085, 0, 0.025, 0.2, 0, 0]])) # FDC variable matrix
# Process 변수와 출력 관련 system gain matrix

def main():
    fwc_p1_vm = VM_Process1_시뮬레이터(A_p1, d_p1, C_p1, 300000)
    fwc_p1_vm.DoE_Run(Z=12, M=10)  #DoE Run
    VMResult = fwc_p1_vm.VM_Run(lamda_PLS=0.1, Z=40, M=10, showType="type-1")

if __name__ == "__main__":
    main()
