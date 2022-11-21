#!/bin/bash
#SBATCH -p workq
#SBATCH --mem 20GB

#Load binaries
module load bioinfo/Nextflow-v20.01.0
module load system/Miniconda3-4.7.10

nextflow run main.nf -profile conda,small --reference data/GCA_003401745.fasta --assembly data/GCA_003402055.fasta --compare data/Example_compare.txt --outdir ./TestPipeline/
