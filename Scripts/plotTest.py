#!/usr/bin/env python
import argparse
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import set_matplotlib_formats
set_matplotlib_formats('retina',quality=100)
plt.rcdefaults()
plt.rcParams['figure.figsize'] = (16,10)
plt.rcParams['axes.linewidth'] = 3

fig,ax = plt.subplots()

parser = argparse.ArgumentParser(description='')
parser.add_argument('--file', type=str, required=True, help='list of input asmgene output')
args = vars(parser.parse_args())
file = args['file']
input = open(file, "r")
compteur = -1

for files in input:
    asmIn = open(files.strip('\n'),"r")
    compteur += 1
    line = asmIn.readline()
    lines = line.split("\t")

    if compteur == 0:
        xticks = [str(lines[2]),str(lines[3])]
        x = [0,1]
    else:
        xticks = np.append(xticks,str(lines[3]))
        x.append(compteur+1)

    line = asmIn.readline()
    lines = line.split("\t")
    if compteur == 0:
        lines = line.split("\t")
        y1 = np.array([int(lines[2]),int(lines[3])])
    else:
        y1 = np.append(y1,int(lines[3]))

    line = asmIn.readline()
    lines = line.split("\t")
    if compteur == 0:
        y2 = np.array([int(lines[2]),int(lines[3])])
    else:
        y2 = np.append(y2,int(lines[3]))

    line = asmIn.readline()
    lines = line.split("\t")
    if compteur == 0:
        y3 = np.array([int(lines[2]),int(lines[3])])
    else:
        y3 = np.append(y3,int(lines[3]))

    # line = asmIn.readline()
    # lines = line.split("\t")
    # if compteur == 0:
    #     z1 = np.array([int(lines[2]),int(lines[3])])
    # else:
    #     z1 = np.append(z1,int(lines[3]))
    #
    # line = asmIn.readline()
    # lines = line.split("\t")
    # if compteur == 0:
    #     z2 = np.array([int(lines[2]),int(lines[3])])
    # else:
    #     z2 = np.append(z2,int(lines[3]))
    #
    # line = asmIn.readline()
    # lines = line.split("\t")
    # if compteur == 0:
    #     z3 = np.array([int(lines[2]),int(lines[3])])
    # else:
    #     z3 = np.append(z3,int(lines[3]))

# print(x)
# print(y1)
# print(y2)
# print(y3)
# print(z1)
# print(z2)
# print(z3)

bars = ax.bar(x,y1,color='dodgerblue',align='center')
bars += ax.bar(x,y2, bottom=y1, color='royalblue',align='center')
bars += ax.bar(x,y3, bottom=y1+y2, color='gold',align='center')
# bars += ax.bar(x,z1,color='orange',align='center',bottom=y1+y2+y3)
# bars += ax.bar(x,z2,color='red',align='center',bottom=z1+y1+y2+y3)
# bars += ax.bar(x,z3,color='darkred',align='center',bottom=z1+z2+y1+y2+y3)
ax.set_xlabel('Assemblies', labelpad=15, color='#333333',weight='bold',size='17')
ax.set_ylabel('Number of Genes', labelpad=15, color='#333333',weight='bold',size='17')
plt.xticks(x,xticks)
plt.tick_params(axis='both', labelsize=14)
plt.legend(["Good","Present","Missing"],loc='upper center',ncol=1,labelspacing=0.10,fontsize='18',frameon=False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(True)
ax.spines['bottom'].set_visible(True)
ax.tick_params(bottom=False, left=True)
ax.set_axisbelow(True)
ax.yaxis.grid(False)
ax.xaxis.grid(False)
plt.ylim(0, max(y1)+int(round((max(y1)/5),0)))

bar_color = bars[0].get_facecolor()
numBar = compteur+2
compteurbar = -1
posYadd = [0]*numBar

for bar in bars:
    compteurbar +=1
    posX = bar.get_x() + bar.get_width() / 2
    posY = bar.get_height()
    if(posY > max(y1)/70):
        ax.text(
          posX,
          posYadd[compteurbar%numBar] + posY/2-200,
          " "+str(bar.get_height())+" - "+str(round((bar.get_height()*100)/max(y1),1))+"%",
          horizontalalignment='center',
          color='black',
          #weight='bold',
          size=bar.get_width()*20
          )
    posYadd[compteurbar%numBar]+=posY

plt.tight_layout()
plt.show()
