#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os

directory ="/work2/project/seqoccin/assemblies/scaffolders/hic/coturnix_japonica/HiFi0151Assembly/3ddna/RepeatModeler/RepeatChrbyChr"

x=26
for filename in os.listdir(directory):
    if filename.endswith("fasta"):
        output = open("runRepeat"+str(x)+".sh","w")
        output.write("#!/bin/bash\n#SBATCH -p workq\n#SBATCH --mem 20GB\n#SBATCH -c 4\n\nmodule load bioinfo/RepeatModeler-2.0.1\nmodule load bioinfo/RepeatMasker-4-0-7\n")
        #output.write("BuildDatabase -name coturnix"+str(x)+" "+str(filename)+"\n")
        #output.write("RepeatModeler -pa 4 -database coturnix"+str(x)+"\n")
        output.write("RepeatMasker -pa 4 -gff -lib ../consensi.fa "+str(filename))
        x+=1
