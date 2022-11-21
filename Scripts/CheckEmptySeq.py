from Bio import SeqIO

for record in SeqIO.parse("50X_aligned_reads.fastq", "fastq"):
    if int(len(record.seq))==0:
        print(str(record.id))
