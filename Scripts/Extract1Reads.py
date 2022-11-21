import gzip
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


ListIn = open("40755ListReads.txt","r")
ListIn2 = open("40494ListReads.txt","r")

# sizeList = []
# countHeight=["< 4000","< 8000","< 12000","< 16000","< 20000","< 24000","< 28000","< 32000","< 36000","< 40000","< 44000","< 48000","< 52000","< 56000","< 60000"]
# for line in ListIn:
#     sizeList.append(int(line.split("/")[2].split("_")[1])-int(line.split("/")[2].split("_")[0]))
# countList = [0]*100
# for val in sizeList:
#     barre = int(int(val)/4000)
#     countList[barre] += 1
#
#
# sizeList2 = []
# countHeight2=[]
# for line in ListIn2:
#     sizeList2.append(int(line.split("/")[2].split("_")[1])-int(line.split("/")[2].split("_")[0]))
# countList2 = [0]*100
# for val in sizeList2:
#     barre = int(int(val)/4000)
#     countList2[barre] += 1
#
# orange_patch = mpatches.Patch(color='orange', label='CLR Bovin 40755')
# blue_patch = mpatches.Patch(color='blue', label='CLR Bovin 40494')
# plt.legend(handles=[orange_patch,blue_patch],fontsize=24)
# X_axis = np.arange(len(countHeight))
# plt.bar(X_axis-0.2,countList2[0:15],0.4, color=["blue"])
# plt.bar(X_axis+0.2,countList[0:15],0.4, color=["orange"])
# plt.xticks(X_axis, countHeight,fontsize=15)
# plt.yticks(fontsize=16)
# plt.xlabel("Insert size",fontsize=24)
# plt.ylabel("Occurence (x10^6)",fontsize=24)
# axes = plt.gca()
# axes.yaxis.grid()
#
# plt.show()



List = []
puits = -1
countSubReads = 0
nbpuits=0
for line in ListIn:
    oldPuits = puits
    puits = line.split("/")[1]
    if puits == oldPuits:
        countSubReads += 1
    else:
        List.append(countSubReads)
        countSubReads = 1
        nbpuits+=1
List.sort()
plotList = {}
for item in List:
    if item in plotList:
        plotList[item]+=1
    else:
        plotList[item]=1

finalList = []
for key, value in plotList.items():
    finalList.append([key,value])
finalList.sort()

listToPlot = []
listHeight = []
mean = 0
for val in finalList:
    if val[1] != 1 and val[0] != 1:
        listToPlot.append(val[0])
        listHeight.append(val[1])
        mean += val[0]*val[1]




List2 = []
puits = -1
countSubReads = 0
nbpuits=0
for line in ListIn2:
    oldPuits = puits
    puits = line.split("/")[1]
    if puits == oldPuits:
        countSubReads += 1
    else:
        List2.append(countSubReads)
        countSubReads = 1
        nbpuits+=1
List2.sort()
plotList2 = {}
for item in List2:
    if item in plotList2:
        plotList2[item]+=1
    else:
        plotList2[item]=1

finalList2 = []
for key, value in plotList2.items():
    finalList2.append([key,value])
finalList2.sort()

listToPlot2 = []
listHeight2 = []
mean = 0
for val in finalList2:
    if val[1] != 1 and val[0] != 1:
        listToPlot2.append(val[0])
        listHeight2.append(val[1])
        mean += val[0]*val[1]

orange_patch = mpatches.Patch(color='orange', label='40755')
blue_patch = mpatches.Patch(color='blue', label='40494')
countHeight = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14"]

X_axis = np.arange(len(listToPlot))
print(X_axis)
plt.bar(X_axis[0:14]-0.2,listHeight2[0:14],0.4, color=["blue"])
plt.bar(X_axis[0:14]+0.2,listHeight[0:14],0.4, color=["orange"])
plt.legend(handles=[orange_patch,blue_patch])
plt.xlabel("Nombre de reads dans le puits", fontsize =24)
plt.ylabel("Occurence", fontsize=24)
plt.xticks(X_axis[0:14], countHeight,fontsize=15)
plt.yticks(fontsize=16)
axes = plt.gca()
axes.yaxis.grid()
plt.show()
plt.bar(X_axis[14:50]-0.2,listHeight2[14:50],0.4, color=["blue"])
plt.bar(X_axis[14:50]+0.2,listHeight[14:50],0.4, color=["orange"])
plt.legend(handles=[orange_patch,blue_patch])
plt.xlabel("Nombre de reads dans le puits")
plt.ylabel("Occurence")
plt.xlim(13,50)
plt.show()
