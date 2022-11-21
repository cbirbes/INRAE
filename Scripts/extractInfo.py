paf3 = open("Filtered3.paf","r")
paf8 = open("Filtered8.paf","r")
paf3Out = open("FilteredFinal3.paf","w")
paf8Out = open("FilteredFinal8.paf","w")


for lines in paf3:
    line = lines.split("\t")
    if (int(line[7]) > 63955495) or (int(line[7]) < 79936367) or (int(line[8]) > 63955495) or (int(line[8]) < 79936367):
        paf3Out.write(lines)


for lines in paf8:
    line = lines.split("\t")
    if (int(line[7]) > 21108458) or (int(line[7]) < 24878922) or (int(line[8]) > 21108458) or (int(line[8]) < 24878922):
        paf8Out.write(lines)
