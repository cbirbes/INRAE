#!/usr/bin/env python3

pafIn = open("mapIn.paf", "r")
pafOut = open("map.paf", "w")

for lines in pafIn:
    line = lines.split("\t")
    query = line[0]
    target = line[5]
    if (query == target) or (query[0]=="R"):
        pafOut.write(lines)
    elif (target[0] == "R"):
        pafOut.write(line[5]+"\t"+line[6]+"\t"+line[7]+"\t"+line[8]+"\t"+line[4]+"\t"+line[0]+"\t"+line[1]+"\t"+line[2]+"\t"+line[3]+"\t"+line[9]+"\t"+line[10]+"\t"+line[11]+"\t"+line[12]+"\t"+line[13]+"\t"+line[14]+"\t"+line[15])
    elif (int(target[0]) < int(query[0])):
        pafOut.write(line[5]+"\t"+line[6]+"\t"+line[7]+"\t"+line[8]+"\t"+line[4]+"\t"+line[0]+"\t"+line[1]+"\t"+line[2]+"\t"+line[3]+"\t"+line[9]+"\t"+line[10]+"\t"+line[11]+"\t"+line[12]+"\t"+line[13]+"\t"+line[14]+"\t"+line[15])
    else:
        pafOut.write(lines)

pafIn.close()
pafOut.close()
