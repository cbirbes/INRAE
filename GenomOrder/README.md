## GenomOrder pipeline
GenomOrder is a Nextflow pipeline reordering and renaming scaffolds from up to 5 assemblies using a reference. It is also able to produce D-Genies back-up files allowing rapid visual comparison of chromosomes of the assemblies versus the reference. These files can be uploaded and visualized with the online tool D-Genies : http://dgenies.toulouse.inra.fr/
The assembly mapping versus the reference is performed with minimap2. These assemblies can be scaffolded or not. If they are not, an option enables to scaffold them according to the reference.
The pipeline produces D-Genies back-up file for a user defined list of reference chromosomes. The chromosome file contains one reference chromosome name per line.

The pipeline has been tested on several data sets including the one hereunder.
## Data used for the test run

Reference: https://www.ncbi.nlm.nih.gov/assembly/GCA_003401745.1

Assembly: https://www.ncbi.nlm.nih.gov/assembly/GCA_003402055.1

## D-Genies backup files examples

<div align="center">
  <img src="Image/HowTo_4.svg">
</div>


## Installation
```
git clone --recursive git@forgemia.inra.fr:seqoccin/GenomOrder.git
cd GenomOrder
```

## Running the test pipeline
To test the pipeline, first make sure that <a href="https://www.nextflow.io/docs/latest/getstarted.html"> Nextflow is installed with >v20.01.0 </a> <a href="https://docs.conda.io/projects/conda/en/latest/user-guide/install/"> and Conda is installed </a>

Then you can run it using conda:
locally :
```
nextflow run main.nf -profile conda,local --reference data/GCA_003401745.fasta --assembly data/GCA_003402055.fasta --compare data/Example_compare.txt --outdir ./TestPipeline/
```
Or on clusters (change, slurm to your cluster settings in conf/small.config):
```
nextflow run main.nf -profile conda,small --reference data/GCA_003401745.fasta --assembly data/GCA_003402055.fasta --compare data/Example_compare.txt --outdir ./TestPipeline/
```

if you already have python3 (biopython package, os and argparse), minimap2 and samtools installed, you can just run :
```
nextflow run main.nf -profile small --reference data/GCA_003401745.fasta --assembly data/GCA_003402055.fasta --compare data/Example_compare.txt --outdir ./TestPipeline/
```





## Parameters
```
The typical command for running the pipeline is as follows:
nextflow run main.nf --reference [referenceFile] --assembly [assemblyFile] [options]

Mandatory arguments:
  --assembly          Path to assembly file (fa, fasta)
  --reference         Path to reference file (fa, fasta)

Optionnal arguments:
  --assembly2       Path to second assembly file (fa, fasta)
  --assembly3       Path to third assembly file (fa, fasta)
  --assembly4       Path to fourth assembly file (fa, fasta)
  --assembly5       Path to fifth assembly file (fa, fasta)

  --arrange         If true, in addition to create DGenies backup, arrange assembly according to reference (default, False).

  --compare         Run DGenie to compare target chromosome vs equivalent in others assembly. Input file with one chromosome name per row (see data/Example_compare.txt).

```

## How to visualize your file.tar ouput
<div align="center">
  <img src="Image/HowTo_1.svg">
  <br />
  <br />
  <br />
  <img width="1800" height="600" src="Image/HowTo_2.svg">
  <img width="1800" height="600" src="Image/HowTo_3.svg">
</div>
