#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os

directory = "/work2/project/seqoccin/data/reads/Illumina/zea_mais"

x=1
for filename in os.listdir(directory):
    if filename.endswith("R1.fastq.gz"):
        output = open("runBwa"+str(x)+".sh","w")
        output.write("#!/bin/bash\n#SBATCH -p workq\n#SBATCH --mem 50GB\n\nmodule load bioinfo/bwa-0.7.17\nmodule load bioinfo/samtools-1.12\n")
        output.write("bwa mem Zea_mays.B73_RefGen_v4.dna.toplevel.fa -R '@RG\\tID:"+str(filename[0:34])+"\\tSM:"+str(filename[0:34])+"' "+str(filename)+" "+str(filename[0:36])+"2.fastq.gz | samtools sort -o output_"+str(filename[0:12])+".bam -")
        x+=1
