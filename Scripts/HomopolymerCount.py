#!/bin/env python

import argparse
import math
from Bio import SeqIO
import matplotlib.pyplot as plt


Base="X"
LengthList=3000*[0]
LengthList[0]=1
Taille = 1
test=0
for record in SeqIO.parse("mother_raw.cgt.fa", "fasta"):
    for x in record.seq:
        test+=1
        if (test%100000000 == 0):
            print(LengthList)
        if x == Base:
            Taille +=1
        else:
            if Taille > 50:
                print (Taille)
                print(record.id)
            LengthList[Taille]+=1
            Taille = 1
            Base = x
    LengthList[Taille]+=1
    Taille = 1

for x in range (0, len(LengthList)):
    value=LengthList[x]
    if value != 0:
        LengthList[x] = float(math.log(value,10))
plt.plot(LengthList[0:50], "b")

Base="X"
LengthList=3000*[0]
LengthList[0]=1
Taille = 1
test=0
for record in SeqIO.parse("consensus.fasta", "fasta"):
    for x in record.seq:
        test+=1
        if (test%100000000 == 0):
            print(LengthList)
        if x == Base:
            Taille +=1
        else:
            if Taille > 50:
                print (Taille)
                print(record.id)
            LengthList[Taille]+=1
            Taille = 1
            Base = x
    LengthList[Taille]+=1
    Taille = 1

for x in range (0, len(LengthList)):
    value=LengthList[x]
    if value != 0:
        LengthList[x] = float(math.log(value,10))
plt.plot(LengthList[0:50], "r")

Base="X"
LengthList=3000*[0]
LengthList[0]=1
Taille = 1
test=0
for record in SeqIO.parse("assembly.racon1.fa", "fasta"):
    for x in record.seq:
        test+=1
        if (test%100000000 == 0):
            print(LengthList)
        if x == Base:
            Taille +=1
        else:
            if Taille > 50:
                print (Taille)
                print(record.id)
            LengthList[Taille]+=1
            Taille = 1
            Base = x
    LengthList[Taille]+=1
    Taille = 1

for x in range (0, len(LengthList)):
    value=LengthList[x]
    if value != 0:
        LengthList[x] = float(math.log(value,10))
plt.plot(LengthList[0:50], "g")
#
# Base="X"
# LengthList=3000*[0]
# LengthList[0]=1
# Taille = 1
# test=0
# for record in SeqIO.parse("ntEditTest_edited.fa", "fasta"):
#     for x in record.seq:
#         test+=1
#         if (test%1000000000 == 0):
#             print(LengthList)
#         if x == Base:
#             Taille +=1
#         else:
#             if Taille > 50:
#                 print (Taille)
#                 print(record.id)
#             LengthList[Taille]+=1
#             Taille = 1
#             Base = x
#     LengthList[Taille]+=1
#     Taille = 1
#
# for x in range (0, len(LengthList)):
#     value=LengthList[x]
#     if value != 0:
#         LengthList[x] = float(math.log(value,10))
# plt.plot(LengthList[0:50], "k")
plt.savefig("Homopolymer.png", format="png")
