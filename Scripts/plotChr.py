from Bio import SeqIO
import matplotlib.pyplot as plt
import numpy as np

noMatchTarget = open("no_target_matches_Offspring2_Final_to_Offspring37160.asm.p_ctg.gfa.txt","r")
hifiFasta = open("Offspring37160.asm.p_ctg.gfa.fa","r")
output1 = open("noMatch_len.txt","w")
output2 = open("match_len.txt","w")
ListNMT=[]
for line in noMatchTarget:
    ListNMT.append(line.strip("\n"))


noMatchChr = []
matchChr = []
shortNoMatchChr = []
shortMatchChr = []
mediumNoMatchChr = []
mediumMatchChr = []
for record in SeqIO.parse(hifiFasta,"fasta"):
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
