from Bio import SeqIO

noMatchTarget = open("no_target_matches_Offspring2_Final_to_Offspring37160.asm.p_ctg.gfa.txt","r")
noMatchQuery = open("no_query_matches_Offspring2_Final_to_Offspring37160.asm.p_ctg.gfa.txt","r")
ontFasta =open("Offspring2_Final.fa","r")
hifiFasta = open("Offspring37160.asm.p_ctg.gfa.fa","r")

outputONT = open("Ont.fa","w")
outputHIFI = open("Hifi.fa","w")

ListNMT=[]
ListNMQ=[]
for line in noMatchTarget:
    ListNMT.append(line.strip("\n"))
for line in noMatchQuery:
    ListNMQ.append(line.strip("\n"))

for record in SeqIO.parse(ontFasta,"fasta"):
    print(record.id)
    if record.id in ListNMQ:
        outputONT.write(">"+str(record.id)+"\n"+str(record.seq)+"\n")
for record in SeqIO.parse(hifiFasta,"fasta"):
    print(record.id)
    if record.id in ListNMT:
        outputHIFI.write(">"+str(record.id)+"\n"+str(record.seq)+"\n")
