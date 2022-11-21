from Bio.SeqUtils import GC
from Bio import SeqIO

SeqOccin = open("SeqoccinCailleGCBloc.tsv","w")
CailleRef = open("CailleRef.tsv","w")
PouleRef = open("PouleRef.tsv","w")

for record in SeqIO.parse("assembly.pilon1.FINAL.fasta", "fasta"):
    x=0
    while x < len(record.seq):
        if x+100000 < len(record.seq):
            SeqOccin.write(str(record.id)+"\t"+str(x)+"\t"+str(x+100000)+"\t"+(str(GC(record.seq[x:x+100000])))+"\n")
        else:
            SeqOccin.write(str(record.id)+"\t"+str(x)+"\t"+str(len(record.seq))+"\t"+(str(GC(record.seq[x:-1])))+"\n")
        x+=100000
