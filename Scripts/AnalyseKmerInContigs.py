import subprocess
import statistics
import os
import matplotlib as mpl
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using non-interactive Agg backend')
    mpl.use('Agg')
import matplotlib.pyplot as plt

inputList = open("List.txt","r")
output = open("ContigsHaplotypeAnalysis.txt","w")
compteur = 0

hap1_37161_percent = []
hap1_37162_percent = []
hap1_37161_flat = []
hap1_37162_flat = []

hap2_37161_percent = []
hap2_37162_percent = []
hap2_37161_flat = []
hap2_37162_flat = []

ListScatterx = []
ListScatterx2 = []
ListScatterxAll = []
ListScatterx2All = []
ListScattery = []
for lines in inputList:
    compteur += 1
    directory = lines.split('\n')[0]
    if "Hap1" in directory:
        size = int(subprocess.check_output("wc -c Analyse/"+directory+"/*.fa | awk '{print $1}'", shell=True))-13
        line37161 = int(subprocess.check_output("wc -l Analyse/"+directory+"/37161_Assembly.txt | awk '{print $1}'", shell=True))
        line37162 = int(subprocess.check_output("wc -l Analyse/"+directory+"/37162_Assembly.txt | awk '{print $1}'", shell=True))
        if line37162 != 0 or line37161 !=0:
            percent1 = float(float(line37161)*100/(float(line37162)+float(line37161)))
            percent2 = float(float(line37162)*100/(float(line37162)+float(line37161)))
            hap1_37161_percent.append(percent1)
            hap1_37162_percent.append(percent2)
            hap1_37161_flat.append(line37161)
            hap1_37162_flat.append(line37162)
            ListScattery.append(percent2)
            ListScatterx.append(size)
            ListScatterx2.append(line37161+line37162)
            ListScatterxAll.append(size)
            ListScatterx2All.append(line37161+line37162)
        else:
            percent1 = 0
            percent2 = 0
            ListScatterxAll.append(size)
            ListScatterx2All.append(line37161+line37162)


    if "Hap2" in directory:
        size = int(subprocess.check_output("wc -c Analyse/"+directory+"/*.fa | awk '{print $1}'", shell=True))-13
        line37161 = int(subprocess.check_output("wc -l Analyse/"+directory+"/37161_Assembly.txt | awk '{print $1}'", shell=True))
        line37162 = int(subprocess.check_output("wc -l Analyse/"+directory+"/37162_Assembly.txt | awk '{print $1}'", shell=True))
        if line37162 != 0 or line37161 !=0:
            percent1 = float(float(line37161)*100/(float(line37162)+float(line37161)))
            percent2 = float(float(line37162)*100/(float(line37162)+float(line37161)))
            hap2_37161_percent.append(percent1)
            hap2_37162_percent.append(percent2)
            hap2_37161_flat.append(line37161)
            hap2_37162_flat.append(line37162)
            ListScattery.append(percent1)
            ListScatterx.append(size)
            ListScatterx2.append(line37161+line37162)
            ListScatterxAll.append(size)
            ListScatterx2All.append(line37161+line37162)
        else:
            percent1 = 0
            percent2 = 0
            ListScatterxAll.append(size)
            ListScatterx2All.append(line37161+line37162)



output.write("hap1 37161 global %"+ str(sum(hap1_37161_flat)*100/(sum(hap1_37161_flat)+sum(hap1_37162_flat)))+"\n")
output.write("hap1 37162 global %"+ str(sum(hap1_37162_flat)*100/(sum(hap1_37161_flat)+sum(hap1_37162_flat)))+"\n")
output.write("hap2 37161 global %"+ str(sum(hap2_37161_flat)*100/(sum(hap2_37161_flat)+sum(hap2_37162_flat)))+"\n")
output.write("hap2 37162 global %"+ str(sum(hap2_37162_flat)*100/(sum(hap2_37161_flat)+sum(hap2_37162_flat)))+"\n")

output1 = open("hap1_37161","w")
output2 = open("hap1_37162","w")
output3 = open("hap2_37161","w")
output4 = open("hap2_37162","w")
output1.write(str(hap1_37161_percent))
output2.write(str(hap1_37162_percent))
output3.write(str(hap2_37161_percent))
output4.write(str(hap2_37162_percent))

plt.figure()
bpl = plt.boxplot(hap1_37161_percent, positions = [2], widths = 1.4)
bpl = plt.boxplot(hap1_37162_percent, positions = [4], widths = 1.4)
bpl = plt.boxplot(hap2_37161_percent, positions = [6], widths = 1.4)
bpl = plt.boxplot(hap2_37162_percent, positions = [8], widths = 1.4)
plt.xlim(0,10)
plt.ylim(0,105)
plt.ylabel("Quality of haplotyping")
plt.xticks([2, 4, 6, 8],['hap1_37161', 'hap1_37162', 'hap2_37161', 'hap2_37162'])
plt.savefig('boxcompare.png')

plt.clf()
plt.scatter(ListScatterx, ListScattery, s=0.1)
plt.ylabel("Quality of haplotyping")
plt.xlabel("Contig size (10⁸ base)")
plt.savefig('scatterPlot_%vsSize.png')

Z = [x for _,x in sorted(zip(ListScattery,ListScatterx))]

plt.clf()
plt.hist2d(Z, ListScattery, bins=(150,150), cmap=plt.cm.jet)
plt.ylabel("Quality of haplotyping")
plt.xlabel("Contig size (10^8 base)")
plt.savefig('TESTscatterPlot_%vsSize.png')

plt.clf()
plt.scatter(ListScatterx, ListScattery, s=0.1)
plt.xlim(0,20000000)
plt.ylabel("Quality of haplotyping")
plt.xlabel("Contig size (10^7 base)")
plt.savefig('scatterPlot2_%vsSize.png')

plt.clf()
plt.scatter(ListScatterx, ListScattery, s=0.1)
plt.xlim(0,200000)
plt.ylabel("Quality of haplotyping")
plt.xlabel("Contig size (10^5 base)")
plt.savefig('scatterPlot3_%vsSize.png')

plt.clf()
plt.scatter(ListScatterx2, ListScattery, s=0.1)
plt.ylabel("Quality of haplotyping")
plt.xlabel("Number of unique Shared Kmer")
plt.savefig('scatterPlot_%vsKmer.png')

plt.clf()
plt.scatter(ListScatterx2, ListScattery, s=0.1)
plt.xlim(0,max(ListScatterx2)/2)
plt.ylabel("Quality of haplotyping")
plt.xlabel("Number of unique Shared Kmer")
plt.savefig('scatterPlot_%vsKmer.png')

inputYak_trioeval = open("../Yak/slurm-28777589.out","r")
switchList = []
for lines in inputYak_trioeval:
    if lines[0] == "S":
        line = lines.split("\t")
        if (int(line[5])+int(line[6])+int(line[4])+int(line[7])) != 0:
            switch = (int(line[5])+int(line[6]))/(int(line[4])+int(line[7])+int(line[5])+int(line[6]))
            switchList.append(switch)
        else:
            switchList.append(int(-0.5))
    elif lines[0] == "W":
        line = lines.split("\t")
        output.write("Hap global switch rate: "+str(line[3].strip("\n"))+"\n")

plt.clf()
plt.scatter(ListScatterxAll, switchList, s=0.1)
plt.ylabel("Switch rate")
plt.xlabel("Contig size (10⁸ base)")
plt.savefig('scatterPlot_SwitchvsSize.png')

plt.clf()
plt.scatter(ListScatterx2All, switchList, s=0.1)
plt.ylabel("Switch rate")
plt.xlabel("Number of unique Shared Kmer")
plt.savefig('scatterPlot_SwitchvsKmer.png')
