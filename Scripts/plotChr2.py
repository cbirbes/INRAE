from Bio import SeqIO
import matplotlib.pyplot as plt
import numpy as np

FastaIn = open("Offspring37160.asm.p_ctg.gfa.fa","r")
fastaOut = open("HifiOut.fa","w")
ListNMT=[]

for record in SeqIO.parse(FastaIn,"fasta"):
    CumulativeLength = 0
    pafIn = open("HiFi_VS_Offspring2.paf","r")
    for lines in pafIn:
        line = lines.strip("\n").split("\t")
        if line[5] == record.id:
            CumulativeLength += int(abs(int(line[3])-int(line[2])))
    pafIn.close()
    if CumulativeLength < int((len(record.seq))/2):
        ListNMT.append(str(record.id))
print(ListNMT)

hifiFasta = open("HifiOut.fa","r")

noMatchChr = []
matchChr = []
shortNoMatchChr = []
shortMatchChr = []
mediumNoMatchChr = []
mediumMatchChr = []

for record in SeqIO.parse(FastaIn,"fasta"):
    if record.id in ListNMT:
        output1.write(str(len(record.seq))+"\n")
        if len(record.seq)>500000:
            noMatchChr.append(len(record.seq))
        elif len(record.seq)>100000:
            mediumNoMatchChr.append(len(record.seq))
        else:
            shortNoMatchChr.append(len(record.seq))
    else:
        output2.write(str(len(record.seq))+"\n")
        if len(record.seq)>500000:
            matchChr.append(len(record.seq))
        elif len(record.seq)>100000:
            mediumMatchChr.append(len(record.seq))
        else:
            shortMatchChr.append(len(record.seq))

colors = ['b','g']
fig, ax1 = plt.subplots()
ax1.hist([shortNoMatchChr,shortMatchChr],color=colors)
ax1.set_ylabel("Count")
plt.tight_layout()
plt.show()

colors = ['b','g']
fig, ax1 = plt.subplots()
ax1.hist([mediumNoMatchChr,mediumMatchChr],color=colors)
ax1.set_ylabel("Count")
plt.tight_layout()
plt.show()

colors = ['b','g']
fig, ax1 = plt.subplots()
ax1.hist([noMatchChr,matchChr],color=colors)
ax1.set_ylabel("Count")
plt.tight_layout()
plt.show()
