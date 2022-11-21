#!/usr/bin/env python
#-*- coding: utf-8 -*-

from Bio import SeqIO
import matplotlib.pyplot as plt

inputHiFi = open("CoverageHiFi.tsv","r")
inputLR = open("CoverageLR.tsv","r")
input10X = open("Coverage10X.tsv","r")
ID=0
coverage=0
ListCover=[]
ListPos=[]

for lines in inputHiFi:
    line=lines.split("\t")
    if (ID == 0) or (ID == line[0]):
        coverage+=int(line[2])
        base = int(line[1])
        ID = line[0]
        if int(line[1])%100000==0:
            ListCover.append(int(coverage/(100000)))
            ListPos.append(base)
            coverage=0

    else:
        ListCover.append(int(coverage/(base%100000)))
        ListPos.append(base)
        coverage = 0
        oldID=ID
        ID = line[0]

        print(str(ListCover))
        print("/////////////////////////////////////////////////////////////////////////////////")
        print(str(ListPos))

        plt.plot(ListCover,ListPos)
        plt.savefig("Plot_"+oldID,format="png")
