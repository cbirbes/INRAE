#!/bin/env python

import argparse
import math
from Bio import SeqIO
import matplotlib.pyplot as plt


Base1="X"
Base2="X"
CountList=3000*[0]
CountList[0]=1
Taille = 1
NbrBaseFait=0

for record in SeqIO.parse("assembly.racon1.fa", "fasta"):
    x=0
    while (x < len(record.seq)-3):
        NbrBaseFait+=1
        if (NbrBaseFait%1000000000 == 0):
            print(CountList)
        if (record.seq[x] == record.seq[x+2] and record.seq[x+1]==record.seq[x+3]):
            Taille +=1
            x+=2
        else:
            CountList[Taille]+=1
            Taille = 1
            x+=1
    CountList[Taille]+=1
    Taille = 1

for x in range (0, len(CountList)):
    value=CountList[x]
    if value != 0:
        CountList[x] = float(math.log(value,10))
plt.plot(CountList[0:50], "b")

Base1="X"
Base2="X"
CountList=3000*[0]
CountList[0]=1
Taille = 1
NbrBaseFait=0

for record in SeqIO.parse("assembly.pilon1.fa", "fasta"):
    x=0
    while (x < len(record.seq)-3):
        NbrBaseFait+=1
        if (NbrBaseFait%1000000000 == 0):
            print(CountList)
        if (record.seq[x] == record.seq[x+2] and record.seq[x+1]==record.seq[x+3]):
            Taille +=1
            x+=2
        else:
            CountList[Taille]+=1
            Taille = 1
            x+=1
    CountList[Taille]+=1
    Taille = 1

for x in range (0, len(CountList)):
    value=CountList[x]
    if value != 0:
        CountList[x] = float(math.log(value,10))
plt.plot(CountList[0:50], "g")



Base1="X"
Base2="X"
CountList=3000*[0]
CountList[0]=1
Taille = 1
NbrBaseFait=0

for record in SeqIO.parse("mother_raw.cgt.fa", "fasta"):
    x=0
    while (x < len(record.seq)-3):
        NbrBaseFait+=1
        if (NbrBaseFait%1000000000 == 0):
            print(CountList)
        if (record.seq[x] == record.seq[x+2] and record.seq[x+1]==record.seq[x+3]):
            Taille +=1
            x+=2
        else:
            CountList[Taille]+=1
            Taille = 1
            x+=1
    CountList[Taille]+=1
    Taille = 1

for x in range (0, len(CountList)):
    value=CountList[x]
    if value != 0:
        CountList[x] = float(math.log(value,10))
plt.plot(CountList[0:50], "k")

Base1="X"
Base2="X"
CountList=3000*[0]
CountList[0]=1
Taille = 1
NbrBaseFait=0

for record in SeqIO.parse("reference_concat.fasta", "fasta"):
    x=0
    while (x < len(record.seq)-3):
        NbrBaseFait+=1
        if (NbrBaseFait%1000000000 == 0):
            print(CountList)
        if (record.seq[x] == record.seq[x+2] and record.seq[x+1]==record.seq[x+3]):
            Taille +=1
            x+=2
        else:
            CountList[Taille]+=1
            Taille = 1
            x+=1
    CountList[Taille]+=1
    Taille = 1

for x in range (0, len(CountList)):
    value=CountList[x]
    if value != 0:
        CountList[x] = float(math.log(value,10))
plt.plot(CountList[0:50], "r")
plt.show()
