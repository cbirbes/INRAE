#!/bin/env python

from Bio import SeqIO
import matplotlib.pyplot as plt


inputList = open("KmerList.txt","r")
kmerList = []
for line in inputList:
    kmerList.append(line.strip("\n").upper())

print(kmerList)
inputFasta = open("GCA_003401745.fasta","r")
for record in SeqIO.parse(inputFasta, "fasta"):
    for x in range(0,len(record.seq)):
        print(record.seq[x:x+21])
        if (record.seq[x:x+21] in kmerList):
            print(record.seq[x:x+21])
