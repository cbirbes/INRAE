from Bio import SeqIO
with open("noChr12345678Ref.fa","w") as output:
    for record in SeqIO.parse("GCA_001577835.1_Coturnix_japonica_2.0_genomic.fa", "fasta"):
        if (not "CM003781.1" in record.id) and (not "CM003782.1" in record.id) and (not "CM003783.1" in record.id) and (not "CM003784.1" in record.id) and (not "CM003785.1" in record.id) and (not "CM003786.1" in record.id) and (not "CM003787.1" in record.id) and (not "CM003812.1" in record.id) and (not "CM003788.1" in record.id) and (not "CM003789.1" in record.id) and (not "CM003790.1" in record.id) and (not "CM003791.1" in record.id) and (not "CM003792.1" in record.id) and (not "CM003793.1" in record.id) and (not "CM003794.1" in record.id) and (not "CM003795.1" in record.id) and (not "CM003796.1" in record.id) and (not "CM003797.1" in record.id) and (not "CM003798.1" in record.id) and (not "CM003799.1" in record.id):
            output.write(">"+str(record.id)+"\n"+str(record.seq)+"\n")
