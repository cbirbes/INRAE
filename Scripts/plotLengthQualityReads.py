import matplotlib.pyplot as plt
import numpy as np
import random
from statistics import mean

inputHifi = open("Hifistats.tsv","r")
inputONT = open("ONTstats.tsv","r")
inputCLR = open("CLRstats.tsv","r")
input10X = open("10Xstats.tsv","r")
inputIll = open("Illuminastats.tsv","r")
inputHiC = open("Hicstats.tsv","r")

listSizeIll = 100000*[250]
listSizeIll.append(int(0))
listSizeIll.append(int(500))

listSizeHic10x = 100000*[150]
listSizeHic10x.append(int(0))
listSizeHic10x.append(int(500))


listSizeHifi = []
listQualHifi = []
for lines in inputHifi:
    line = lines.strip("\n").split(" ")
    listSizeHifi.append(int(line[0]))
    listQualHifi.append(float(line[1]))
meanSizeHifi = mean(listSizeHifi)

listSizeONT = []
listQualONT = []
for lines in inputONT:
    line = lines.strip("\n").split(" ")
    listSizeONT.append(int(line[0]))
    listQualONT.append(float(line[1]))


listSizeCLR = []
for lines in inputCLR:
    line = lines.strip("\n").split(" ")
    listSizeCLR.append(int(line[0]))

listQual10X = []
for lines in input10X:
    line = lines.strip("\n").split(" ")
    listQual10X.append(float(line[1]))

listQualIll = []
for lines in inputIll:
    line = lines.strip("\n").split(" ")
    listQualIll.append(float(line[1]))

listQualHic = []
for lines in inputHiC:
    line = lines.strip("\n").split(" ")
    listQualHic.append(float(line[1]))


# fig = plt.figure(figsize =(10, 7))
# ax = fig.add_subplot(111)
# listQual = [random.sample(listQualHifi,100000),random.sample(listQualONT,100000), random.sample(listQual10X,100000), random.sample(listQualHic,100000), random.sample(listQualIll,100000)]
# plt.yticks(np.arange(0,60,5))
# plt.boxplot(listQual)
# ax.set_xticklabels(['Hifi', 'Nanopore', '10X', 'Hi-C', 'Illumina'])
# plt.ylim(0, 60)
# ax.set_ylabel('Reads quality', size= 12)
# ax.spines['right'].set_visible(False)
# ax.spines['top'].set_visible(False)
# plt.show()
# plt.clf()

fig = plt.figure(figsize =(10, 7))
ax = fig.add_subplot(231)
listQual = [random.sample(listQualONT,100000)]
plt.boxplot(listQual)
ax.set_xticklabels(['Nanopore'])
plt.ylim(0, 60)
ax.set_ylabel('Reads quality', size= 12)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.yticks(np.arange(0,60,5))

bx = fig.add_subplot(232)
listQual = [random.sample(listQualHifi,100000)]
plt.boxplot(listQual)
bx.set_xticklabels(['Hifi'])
plt.ylim(0, 60)
bx.set_ylabel('Reads quality', size= 12)
bx.spines['right'].set_visible(False)
bx.spines['top'].set_visible(False)
plt.yticks(np.arange(0,60,5))

cx = fig.add_subplot(234)
listQual = [random.sample(listQual10X,100000)]
plt.boxplot(listQual)
cx.set_xticklabels(['10X'])
plt.ylim(0, 60)
cx.set_ylabel('Reads quality', size= 12)
cx.spines['right'].set_visible(False)
cx.spines['top'].set_visible(False)
plt.yticks(np.arange(0,60,5))

dx = fig.add_subplot(235)
listQual = [random.sample(listQualHic,100000)]
plt.boxplot(listQual)
plt.ylim(0, 60)
dx.set_xticklabels(['Hi-C'])
dx.set_ylabel('Reads quality', size= 12)
dx.spines['right'].set_visible(False)
dx.spines['top'].set_visible(False)
plt.yticks(np.arange(0,60,5))

ex = fig.add_subplot(236)
listQual = [random.sample(listQualIll,100000)]
plt.boxplot(listQual)
plt.ylim(0, 60)
ex.set_xticklabels(['Illumina'])
ex.set_ylabel('Reads quality', size= 12)
ex.spines['right'].set_visible(False)
ex.spines['top'].set_visible(False)
plt.yticks(np.arange(0,60,5))

plt.tight_layout()
plt.savefig('Quality.svg')

plt.clf()





fig = plt.figure(figsize =(10, 7))
ax = fig.add_subplot(231)
plt.hist(random.sample(listSizeCLR,100000),bins=5000)
plt.xlim(0, 60000)
ax.set_xlabel('Reads length', size = 12)
ax.set_ylabel('Number of occurences', size= 12)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.set_title('CLR', size = 20)

bx = fig.add_subplot(232)
plt.hist(random.sample(listSizeONT,100000),bins=5000)
plt.xlim(0, 60000)
bx.set_xlabel('Reads length', size = 12)
bx.set_ylabel('Number of occurences', size= 12)
bx.spines['right'].set_visible(False)
bx.spines['top'].set_visible(False)
bx.set_title('ONT', size = 20)

cx = fig.add_subplot(233)
plt.hist(random.sample(listSizeHifi,100000),bins=5000)
plt.xlim(0, 60000)
cx.set_xlabel('Reads length', size = 12)
cx.set_ylabel('Number of occurences', size= 12)
cx.spines['right'].set_visible(False)
cx.spines['top'].set_visible(False)
cx.set_title('Hifi', size = 20)

dx = fig.add_subplot(234)
plt.hist(listSizeHic10x, bins=100)
plt.xlim(0, 500)
dx.set_xlabel('Reads length', size = 12)
dx.set_ylabel('Number of occurences', size= 12)
dx.spines['right'].set_visible(False)
dx.spines['top'].set_visible(False)
dx.set_title('10X', size = 20)

ex = fig.add_subplot(235)
plt.hist(listSizeIll,bins=100)
plt.xlim(0, 500)
ex.set_xlabel('Reads length', size = 12)
ex.set_ylabel('Number of occurences', size= 12)
ex.spines['right'].set_visible(False)
ex.spines['top'].set_visible(False)
ex.set_title('Illumina', size = 20)

fx = fig.add_subplot(236)
plt.hist(listSizeHic10x,bins=100)
plt.xlim(0, 500)
fx.set_xlabel('Reads length', size = 12)
fx.set_ylabel('Number of occurences', size= 12)
fx.spines['right'].set_visible(False)
fx.spines['top'].set_visible(False)
fx.set_title('Hi-C', size = 20)

plt.tight_layout()
plt.savefig('Length.svg')
