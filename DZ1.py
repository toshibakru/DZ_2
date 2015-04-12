
"""
Scheme Checking
"""
import time
START = time.time()
import sys
import DZ2
INPUT_FILE = sys.argv[1]
import xml.dom.minidom
DOM = xml.dom.minidom.parse(INPUT_FILE)
import copy

NET = DOM.getElementsByTagName('net')
N = len(NET)
RESISTOR = DOM.getElementsByTagName('resistor')
CAPACTOR = DOM.getElementsByTagName('capactor')
DIODE = DOM.getElementsByTagName('diode')
D = []
for i in range(N):
    D.append([0]*N)
MAS = []
K = len(RESISTOR) + len(CAPACTOR) + len(DIODE)
for i in range(K):
    MAS.append([0] * 4)
IND = 0
for i in range(0, len(RESISTOR)):
    MAS[IND][0] = int(RESISTOR[i].attributes["net_from"].value)
    IND = IND + 1
for i in range(0, len(CAPACTOR)):
    MAS[IND][0] = int(CAPACTOR[i].attributes["net_from"].value)
    IND = IND + 1
for i in range(0, len(DIODE)):
    MAS[IND][0] = int(DIODE[i].attributes["net_from"].value)
    IND = IND + 1
IND = 0
for i in range(0, len(RESISTOR)):
    MAS[IND][1] = int(RESISTOR[i].attributes["net_to"].value)
    IND = IND + 1
for i in range(0, len(CAPACTOR)):
    MAS[IND][1] = int(CAPACTOR[i].attributes["net_to"].value)
    IND = IND + 1
for i in range(0, len(DIODE)):
    MAS[IND][1] = int(DIODE[i].attributes["net_to"].value)
    IND = IND + 1
IND = 0
for i in range(0, len(RESISTOR)):
    MAS[IND][2] = float(RESISTOR[i].attributes["resistance"].value)
    IND = IND + 1
for i in range(0, len(CAPACTOR)):
    MAS[IND][2] = float(CAPACTOR[i].attributes["resistance"].value)
    IND = IND + 1
for i in range(0, len(DIODE)):
    MAS[IND][2] = float(DIODE[i].attributes["resistance"].value)
    IND = IND + 1
IND = 0
for i in range(0, len(RESISTOR)):
    MAS[IND][3] = float(RESISTOR[i].attributes["resistance"].value)
    IND = IND + 1
for i in range(0, len(CAPACTOR)):
    MAS[IND][3] = float(CAPACTOR[i].attributes["resistance"].value)
    IND = IND + 1
for i in range(0, len(DIODE)):
    MAS[IND][3] = float(DIODE[i].attributes["reverse_resistance"].value)
    IND = IND + 1
for i in range(N):
    for j in range(N):
        D[i][j] = float('inf')
        if i == j:
            D[i][j] = 0
for i in range(IND):
    try:
        A = 1 / D[MAS[i][0] - 1][MAS[i][1] - 1]
    except ZeroDivisionError:
        A = float('inf')
    try:
        B = 1 / MAS[i][2]
    except ZeroDivisionError:
        B = float('inf')
    try:
        D[MAS[i][0] - 1][MAS[i][1] - 1] = 1 / (A + B)
    except ZeroDivisionError:
        D[MAS[i][0] - 1][MAS[i][1] - 1] = float('inf')
    try:
        A = 1 / D[MAS[i][1] - 1][MAS[i][0] - 1]
    except ZeroDivisionError:
        A = float('inf')
    try:
        B = 1 / MAS[i][3]
    except ZeroDivisionError:
        B = float('inf')
    try:
        D[MAS[i][1] - 1][MAS[i][0] - 1] = 1 / (A + B)
    except ZeroDivisionError:
        D[MAS[i][1] - 1][MAS[i][0] - 1] = float('inf')
DD = copy.deepcopy(D)
for k in range(N):
    for i in range(N):
        for j in range(N):
            try:
                A = 1 / D[i][j]
            except ZeroDivisionError:
                A = float('inf')
            try:
                B = 1 / (D[i][k] + D[k][j])
            except ZeroDivisionError:
                B = float('inf')
            try:
                D[i][j] = 1 / (A + B)
            except ZeroDivisionError:
                A = float('inf')
OUTPUT = sys.argv[2]
OUTFILE = open(OUTPUT, 'w')
for row in D:
    for i in row:
        OUTFILE.write("{:.6f},".format(i))
    OUTFILE.write("\n")
OUTFILE.close()
FINISH = time.time()

START_F = time.time();
ANS = DZ2.DZ2(DD)
FINISH_F = time.time()

try:
    ANS_TIME = (FINISH - START) / (FINISH_F - START_F)
    print(ANS_TIME)
except ZeroDivisionError:
    ANS_TIME = float('inf')
    print('Ваш компьютер очень быстрый')

