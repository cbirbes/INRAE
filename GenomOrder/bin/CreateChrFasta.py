#!/usr/bin/env python3

import os
from Bio import SeqIO
import argparse

parser = argparse.ArgumentParser(description='Create fasta')
parser.add_argument('--Chr', help = "input Chr name", required=True)
parser.add_argument('--Ref', help = "input Ref name", required=True)
parser.add_argument('--assembly1', help = "input Assembly name", required=True)
parser.add_argument('--assembly2', help = "input Assembly name", required=True)
parser.add_argument('--assembly3', help = "input Assembly name", required=True)
parser.add_argument('--assembly4', help = "input Assembly name", required=True)
parser.add_argument('--assembly5', help = "input Assembly name", required=True)

args = vars(parser.parse_args())
InputChr = args['Chr']
InputRef = args['Ref']
path1=args['assembly1']
path2=args['assembly2']
path3=args['assembly3']
path4=args['assembly4']
path5=args['assembly5']

output = open(str(InputChr)+"File.fasta","w")

find = False

for record in SeqIO.parse(InputRef, "fasta"):
    if (str(record.id) == str(InputChr)):
        output.write(">Reference_"+str(InputChr)+"\n"+str(record.seq)+"\n")

if (str(path1) != "NO_FILE1") and (os.path.exists(path1)):
    for record in SeqIO.parse(path1, "fasta"):
        if (str(record.id) == str(InputChr)):
            output.write(">1_"+str(path1)+"_"+str(InputChr)+"\n"+str(record.seq)+"\n")
            find = True
            break
    if find == False:
        output.write(">1_"+str(path1)+"_"+str(InputChr)+"\n"+str("NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN")+"\n")


if (str(path2) != "NO_FILE2") and (os.path.exists(path2)):
    for record in SeqIO.parse(path2, "fasta"):
        if (str(record.id) == str(InputChr)):
            output.write(">2_"+str(path2)+"_"+str(InputChr)+"\n"+str(record.seq)+"\n")
            find = True
            break
    if find == False:
        output.write(">2_"+str(path2)+"_"+str(InputChr)+"\n"+str("NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN")+"\n")

if (str(path3) != "NO_FILE3") and (os.path.exists(path3)):
    for record in SeqIO.parse(path3, "fasta"):
        if (str(record.id) == str(InputChr)):
            output.write(">3_"+str(path3)+"_"+str(InputChr)+"\n"+str(record.seq)+"\n")
            find = True
            break
    if find == False:
        output.write(">3_"+str(path3)+"_"+str(InputChr)+"\n"+str("NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN")+"\n")


if (str(path4) != "NO_FILE4") and (os.path.exists(path4)):
    for record in SeqIO.parse(path4, "fasta"):
        if (str(record.id) == str(InputChr)):
            output.write(">4_"+str(path4)+"_"+str(InputChr)+"\n"+str(record.seq)+"\n")
            find = True
            break
    if find == False:
        output.write(">4_"+str(path4)+"_"+str(InputChr)+"\n"+str("NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN")+"\n")


if (str(path5) != "NO_FILE5") and (os.path.exists(path5)):
    for record in SeqIO.parse(path5, "fasta"):
        if (str(record.id) == str(InputChr)):
            output.write(">5_"+str(path5)+"_"+str(InputChr)+"\n"+str(record.seq)+"\n")
            find = True
            break
    if find == False:
        output.write(">5_"+str(path5)+"_"+str(InputChr)+"\n"+str("NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN")+"\n")
