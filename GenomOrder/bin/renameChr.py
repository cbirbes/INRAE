#!/usr/bin/env python3

import os
from Bio import SeqIO
import argparse

parser = argparse.ArgumentParser(description='Create fasta')
parser.add_argument('--Chr', help = "input Chr name", required=True)
parser.add_argument('--Ref', help = "input Ref name", required=True)
parser.add_argument('--Assembly1', help = "assembly fasta file", required=True)
parser.add_argument('--Assembly2', help = "assembly fasta file", required=True)
parser.add_argument('--Assembly3', help = "assembly fasta file", required=True)
parser.add_argument('--Assembly4', help = "assembly fasta file", required=True)
parser.add_argument('--Assembly5', help = "assembly fasta file", required=True)

args = vars(parser.parse_args())
InputChr = args['Chr']
InputRef = args['Ref']
path1 = args['Assembly1']
path2 = args['Assembly2']
path3 = args['Assembly3']
path4 = args['Assembly4']
path5 = args['Assembly5']

output = open(str(InputChr)+"File.fasta","w")
Match = 0
for record in SeqIO.parse(InputRef, "fasta"):
    if (str(record.id) == str(InputChr)):
        output.write(">Reference_"+str(InputChr)+"\n"+str(record.seq)+"\n")

if str(path1) != 'NO_FILE1':
    input = open("map1.paf")
    searching = True
    reverse = False
    for line in input:
        lines = line.strip("\n").split("\t")
        if (str(InputChr) in lines[5] and searching):
            Match = lines[0]
            searching = False
            if (int(lines[8])-int(line[7]) < 0):
                reverse=True
            break
        else:
            Match = 0
    for record in SeqIO.parse(path1, "fasta"):
        if ((str(record.id) == str(Match)) and reverse):
            output.write(">1_"+str(path1)+"_"+str(InputChr)+"\n"+str(record.seq.reverse_complement())+"\n")
        elif ((str(record.id) == str(Match)) and not reverse):
            output.write(">1_"+str(path1)+"_"+str(InputChr)+"\n"+str(record.seq)+"\n")
    if Match == 0:
        output.write(">1_"+str(path1)+"_"+str(InputChr)+"\n"+str("NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN")+"\n")

if str(path2) != 'NO_FILE2':
    input = open("map2.paf")
    searching = True
    reverse = False
    for line in input:
        lines = line.strip("\n").split("\t")
        if (str(InputChr) in lines[5] and searching):
            Match = lines[0]
            searching = False
            if (int(lines[8])-int(line[7]) < 0):
                reverse=True
            break
        else:
            Match = 0
    for record in SeqIO.parse(path2, "fasta"):
        if ((str(record.id) == str(Match)) and reverse):
            output.write(">2_"+str(path2)+"_"+str(InputChr)+"\n"+str(record.seq.reverse_complement())+"\n")
        elif ((str(record.id) == str(Match)) and not reverse):
            output.write(">2_"+str(path2)+"_"+str(InputChr)+"\n"+str(record.seq)+"\n")
    if Match == 0:
        output.write(">2_"+str(path2)+"_"+str(InputChr)+"\n"+str("NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN")+"\n")

if str(path3) != 'NO_FILE3':
    input = open("map3.paf")
    searching = True
    reverse = False
    for line in input:
        lines = line.strip("\n").split("\t")
        if (str(InputChr) in lines[5] and searching):
            Match = lines[0]
            searching = False
            if (int(lines[8])-int(line[7]) < 0):
                reverse=True
            break
        else:
            Match = 0
    for record in SeqIO.parse(path3, "fasta"):
        if ((str(record.id) == str(Match)) and reverse):
            output.write(">3_"+str(path3)+"_"+str(InputChr)+"\n"+str(record.seq.reverse_complement())+"\n")
        elif ((str(record.id) == str(Match)) and not reverse):
            output.write(">3_"+str(path3)+"_"+str(InputChr)+"\n"+str(record.seq)+"\n")
    if Match == 0:
        output.write(">3_"+str(path3)+"_"+str(InputChr)+"\n"+str("NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN")+"\n")

if str(path4) != 'NO_FILE4':
    input = open("map4.paf")
    searching = True
    reverse = False
    for line in input:
        lines = line.strip("\n").split("\t")
        if (str(InputChr) in lines[5] and searching):
            Match = lines[0]
            searching = False
            if (int(lines[8])-int(line[7]) < 0):
                reverse=True
            break
        else:
            Match = 0
    for record in SeqIO.parse(path4, "fasta"):
        if ((str(record.id) == str(Match)) and reverse):
            output.write(">4_"+str(path4)+"_"+str(InputChr)+"\n"+str(record.seq.reverse_complement())+"\n")
        elif ((str(record.id) == str(Match)) and not reverse):
            output.write(">4_"+str(path4)+"_"+str(InputChr)+"\n"+str(record.seq)+"\n")
    if Match == 0:
        output.write(">4_"+str(path4)+"_"+str(InputChr)+"\n"+str("NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN")+"\n")

if str(path5) != 'NO_FILE5':
    input = open("map5.paf")
    searching = True
    reverse = False
    for line in input:
        lines = line.strip("\n").split("\t")
        if (str(InputChr) in lines[5] and searching):
            Match = lines[0]
            searching = False
            if (int(lines[8])-int(line[7]) < 0):
                reverse=True
            break
        else:
            Match = 0
    for record in SeqIO.parse(path5, "fasta"):
        if ((str(record.id) == str(Match)) and reverse):
            output.write(">5_"+str(path5)+"_"+str(InputChr)+"\n"+str(record.seq.reverse_complement())+"\n")
        elif ((str(record.id) == str(Match)) and not reverse):
            output.write(">5_"+str(path5)+"_"+str(InputChr)+"\n"+str(record.seq)+"\n")
    if Match == 0:
        output.write(">5_"+str(path5)+"_"+str(InputChr)+"\n"+str("NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN")+"\n")

input.close()
output.close()
