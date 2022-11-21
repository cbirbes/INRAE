#!/bin/env python
import argparse
from Bio import SeqIO
import gzip

output = open("readsFiltered50kb.fasta", "w")
with gzip.open("trio1.mother.run123.fastq.gz", "rt") as fileIn:
    for record in SeqIO.parse(fileIn, "fastq"):
        if (len(record.seq)>50000):
            output.write(str(record.id)+"\n"+str(record.seq)+"\n")
