from Bio.SeqUtils import GC
from Bio import SeqIO

SeqOccin = open("SeqoccinCaille.tsv","w")
CailleRef = open("CailleRef.tsv","w")
PouleRef = open("PouleRef.tsv","w")

for record in SeqIO.parse("assembly.pilon1.FINAL.fasta", "fasta"):
    SeqOccin.write(str(record.id)+"\t"+(str(GC(record.seq)))+"\n")

for record in SeqIO.parse("Gallus_gallus.GRCg6a.dna.toplevel.fa", "fasta"):
    CailleRef.write(str(record.id)+"\t"+(str(GC(record.seq)))+"\n")

for record in SeqIO.parse("../Dgenies/GCA_001577835.1_Coturnix_japonica_2.0_genomic.fa", "fasta"):
    PouleRef.write(str(record.id)+"\t"+(str(GC(record.seq)))+"\n")
