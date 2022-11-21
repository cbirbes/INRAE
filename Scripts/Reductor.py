#!/bin/env python
#-*- coding: utf-8 -*-

from Bio import SeqIO
import os
import subprocess
import argparse

parser = argparse.ArgumentParser(description='Tools to delete area with low coverage in contigs and reduce homopolymer length')
parser.add_argument('--alignment', help = "bam file ", required=True)
parser.add_argument('--gff', help = "gffFile, output from KmerGffMaker.py", required=True)
parser.add_argument('--reference', help = "reference genome file", required=True)
parser.add_argument('--coverageThreshold', help = "area with coverage < coverageThreshold are deleted", required=False, default=4, type=int)
parser.add_argument('--sizeThreshold', help = "low coverage are longer than sizeThreshold are deleted", required=False, default=15, type=int)

args = vars(parser.parse_args())
BAM = args['alignment']
GFF = args['gff']
REFERENCE = args['reference']
COVERAGE = int(args['coverageThreshold'])
SIZE = int(args['sizeThreshold'])

output = open("assembly_corrected"+os.path.basename(REFERENCE)+".fasta", "w")
output_detail = open("correction_detail.txt", "w")

ctgFile= open("ctg.bed","w")
for record in SeqIO.parse(REFERENCE, "fasta"):
    ctgFile.write(str(record.id.strip(">")) + "\t0\t100000000000\n")
ctgFile.close()

process = subprocess.Popen(["samtools mpileup -a -Q 0 -l ctg.bed " + BAM], stdout = subprocess.PIPE, shell=True, universal_newlines=True)

mpileup_line = process.stdout.readline().strip("\n").split("\t")


gff = open(GFF, "r")
gff_line = gff.readline().strip("\n").split("\t")

fin=False
firstTime=True

#Pour chaque contigs
for record in SeqIO.parse(REFERENCE, "fasta"):
    numberOfDel = 0
    NumberReads = 0
    LastPosition = 0
    LowCoverageArea = 0
#On ecrit le nom du contig en en-tete
    output.write("\n>"+str(record.id)+"\n")
#Si le fichier Homopolymer ne contient aucune ligne, ou si on est arrivé au bout
    if gff_line[0] == "":
        gff_line=["ctg0","Fin","X","0","X","0","X","0"]

#Tant que le fichier mpileup est sur le meme contig que record
    while (str(mpileup_line[0]) == str(record.id)):
        if fin==True:
            break
#Si on arrive a une zonne d'homopolymere identifié dans gff.gff
        if (int(mpileup_line[1]) == int(gff_line[3])) and ((mpileup_line[0]) == (gff_line[0])):
#On va chercher la quantité de * (délétions)
            for i in range(int(gff_line[7])):
                NumberReads += (int(mpileup_line[3]))
                Event = mpileup_line[4]
                for x in Event:
                    if (x == "*"):
                        numberOfDel += 1
                mpileup_line = process.stdout.readline().strip("\n").split("\t")
                if mpileup_line[0]=="":
                    fin=True
                    break
            if (NumberReads != 0):
                MeanNumberOfDel= numberOfDel/(NumberReads/(int(gff_line[7])))
            else:
                MeanNumberOfDel = 0
#On arrondit pour supprimer le bon nombre de bases
            if gff_line[1]=="HomoDimer":
                while (round(MeanNumberOfDel)%2 != 0):
                    MeanNumberOfDel -= 1
            elif gff_line[1]=="HomoTrimer":
                while (round(MeanNumberOfDel)%3 != 0):
                    MeanNumberOfDel -= 1
            elif gff_line[1]=="HomoQuadmer":
                while (round(MeanNumberOfDel)%4 != 0):
                    MeanNumberOfDel -= 1
            AreaToRemove=MeanNumberOfDel
#On ecrit de la dernière position jusqu'a la position ciblé
            if (NumberReads/(int(gff_line[7]))) >= COVERAGE:
                output.write("X"+str(record.seq[LastPosition:(int(gff_line[5])-int(AreaToRemove))]))
                output_detail.write("Writed from "+ str(record.id) + " " + str(LastPosition) + " to " + str(int(gff_line[5])-int(AreaToRemove)-1) + "\t" + str(gff_line[1]) + " encountered\t" + str(AreaToRemove) + " base deleted\n" )
            LastPosition=int(gff_line[5])
#On remet les compteurs a 0
            numberOfDel = 0
            NumberReads = 0
#Puis on passe a l'homopolymere suivant
            gff_line = gff.readline().strip("\n").split("\t")
            if gff_line[0] == "":
                gff_line=["ctg0","Fin","X","0","X","0","X","0"]


#Si on est pas dans une zone d'Homopolymeres
        else:
            while ((mpileup_line[0]) == str(record.id)) and (((mpileup_line[1]) != (gff_line[3])) or (mpileup_line[0] != gff_line[0]) or gff_line[0] == "ctg0"):
                while ((int(mpileup_line[3])<COVERAGE) and ((mpileup_line[1]) != (gff_line[3])) and ((mpileup_line[0]) == (str(record.id)))):
                    # print("Low Coverage" + mpileup_line[1])
                    LowCoverageArea+=1
                    mpileup_line = process.stdout.readline().strip("\n").split("\t")
                    if mpileup_line[0]=="":
                        fin=True
                        break
                if fin:
                    break
                if (fin or (mpileup_line[0]) != str(record.id)) and (LowCoverageArea>SIZE) and (LastPosition<int(len(record.seq))-LowCoverageArea-2):
                    output.write("X"+str(record.seq[LastPosition:int(len(record.seq)-LowCoverageArea-1)]))
                    output_detail.write("Writed from "+ str(record.id) + " " + str(LastPosition+1) + " to " + str(int(len(record.seq))-LowCoverageArea-1) + "\tLow coverage area encountered\t" + str(LowCoverageArea) + " base deleted\n" )
                    LastPosition=int(len(record.seq))
                elif (LowCoverageArea>SIZE) and (int(mpileup_line[1])-LowCoverageArea-1 == 0):
                    LastPosition = int(mpileup_line[1])-1
                elif (LowCoverageArea>SIZE) and (LastPosition<int(len(record.seq))-LowCoverageArea-2):
                    output.write("X"+str(record.seq[LastPosition:int(mpileup_line[1])-LowCoverageArea-1]))
                    output_detail.write("Writed from "+ str(record.id) + " " + str(LastPosition+1) + " to " + str(int(mpileup_line[1])-LowCoverageArea-1) + "\tLow coverage area encountered\t" + str(LowCoverageArea) + " base deleted\n" )
                    LastPosition = int(mpileup_line[1])-1
                elif ((int(mpileup_line[1]) != int(gff_line[3]) or (mpileup_line[0] != gff_line[0])) and (mpileup_line[0]) == (str(record.id))):
                    mpileup_line = process.stdout.readline().strip("\n").split("\t")
                    if mpileup_line[0]=="":
                        fin=True
                        break
                LowCoverageArea = 0
    if(int(LastPosition)!=int(len(record.seq))):
        output.write("X"+str(record.seq[LastPosition:len(record.seq)]))
        output_detail.write("Writed from "+ str(record.id) + " " + str(LastPosition) + " to " + str(len(record.seq)) + "\n" )
