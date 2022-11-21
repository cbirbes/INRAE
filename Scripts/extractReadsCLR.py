paf = open("Caille.sam","r")
listContigs = {}
outpoutInf1000 = open("outpoutInf1000.sam","w")
outpoutSup1000 = open("outpoutSup1000.sam","w")


for lines in paf:
    line = lines.strip("\n").split("\t")
    if lines.startswith("@SQ"):
        listContigs[line[1].strip("SN:")]=line[2].strip("LN:")

    elif lines.startswith("R") and line[2] != "*":
        activeSize = listContigs[line[2]]
        mappingPos = line[3]
        mappingLength = len(line[9])
        if int(line[4]) >= 5 and int(line[4])!=255:
            if int(line[3]) < 2000:
                outpoutInf1000.write(lines+"\n")

            elif (int(mappingPos)+int(mappingLength)) >= (int(activeSize)-2000):
                outpoutSup1000.write(lines+"\n")
