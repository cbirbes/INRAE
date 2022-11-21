input = open("ragtag_output/ragtag.scaffold.fasta","r")
output = open("ZmWGA05a-04.fasta","w")

x=0

for lines in input:
    x+=1
    if lines.startswith(">"):
        output.write(lines.strip("_RagTag"))
    elif x==2:
        output.write(lines[0:90800000])
        output.write(lines[226900000:-2]+"\n")
        sequence = lines[90800000:226900000]
    elif x == 4:
        output.write("\n"+sequence+lines)
    else:
        output.write(lines)
