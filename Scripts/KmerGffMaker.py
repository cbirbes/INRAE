#!/bin/env python

from Bio import SeqIO
import argparse

parser = argparse.ArgumentParser(description='Description of your program')
parser.add_argument('--fasta', help = "input fasta file", required=True)
args = vars(parser.parse_args())

FILENAME = args['fasta']

compteurHomoPolymer = 0
compteurHomoDimer = 0
compteurHomoTrimer = 0
compteurHomoQuadmer = 0
with open("HomoPolymer.gff","w") as gff:
    for record in SeqIO.parse(FILENAME, "fasta"):
        x=0
        while x <= (len(record.seq)-9):
            if (record.seq[x] == record.seq[x+1]):
                PosStart=x
                PosEnd=x+1
                while ((x <= (len(record.seq)-3)) and (record.seq[x] == record.seq[x+1])):
                    PosEnd=x+1
                    x+=1
                if (PosEnd-PosStart >= 15):
                    gff.write(str(record.id) + "\tHomoPolymer\tStart:\t" + str(PosStart+1) + "\tEnd:\t" + str(PosEnd+1) + "\tSize:\t" + str(PosEnd-PosStart+1) + "\n")
                    x+=1

            elif ((record.seq[x] == record.seq[x+2]) and (record.seq[x+1] == record.seq[x+3])):
                PosStart=x
                PosEnd=x+3
                while ((x <= (len(record.seq)-5)) and ((record.seq[x] == record.seq[x+2]) and (record.seq[x+1] == record.seq[x+3]))):
                    PosEnd=x+3
                    x+=2
                if (PosEnd-PosStart >= 20):
                    gff.write(str(record.id) + "\tHomoDimer\tStart:\t" + str(PosStart+1) + "\tEnd:\t" + str(PosEnd+1) + "\tSize:\t" + str(PosEnd-PosStart+1) + "\n")
                    x+=1

            elif ((record.seq[x] == record.seq[x+3]) and (record.seq[x+1] == record.seq[x+4]) and (record.seq[x+2] == record.seq[x+5])):
                PosStart=x
                PosEnd=x+5
                while ((x <= (len(record.seq)-7)) and ((record.seq[x] == record.seq[x+3]) and (record.seq[x+1] == record.seq[x+4]) and (record.seq[x+2] == record.seq[x+5]))):
                    PosEnd=x+5
                    x+=3
                if (PosEnd-PosStart >= 25):
                    gff.write(str(record.id) + "\tHomoTrimer\tStart:\t" + str(PosStart+1) + "\tEnd:\t" + str(PosEnd+1) + "\tSize:\t" + str(PosEnd-PosStart+1) + "\n")
                    x+=1

            elif ((record.seq[x] == record.seq[x+4]) and (record.seq[x+1] == record.seq[x+5]) and (record.seq[x+2] == record.seq[x+6]) and (record.seq[x+3] == record.seq[x+7])):
                PosStart=x
                PosEnd=x+7
                while ((x <= (len(record.seq)-8)) and ((record.seq[x] == record.seq[x+4]) and (record.seq[x+1] == record.seq[x+5]) and (record.seq[x+2] == record.seq[x+6]) and (record.seq[x+3] == record.seq[x+7]))):
                        PosEnd=x+7
                        x+=4
                if (PosEnd-PosStart >= 30):
                    gff.write(str(record.id) + "\tHomoQuadmer\tStart:\t" + str(PosStart+1) + "\tEnd:\t" + str(PosEnd+1) + "\tSize:\t" + str(PosEnd-PosStart+1) + "\n")
                    x+=1

            else:
                x+=1
