inputGFA_1 = open("Alpine.dip.hap1.p_ctg.gfa","r")
inputGFA_2 = open("Alpine.dip.hap2.p_ctg.gfa","r")
outputFa_1 = open("Alpine.rephased_hap1.fa","w")
outputFa_2 = open("Alpine.rephased_hap2.fa","w")
outputFa_3 = open("Alpine.rephased_hap3.fa","w")

# inputGFA_1 = open("HN_Yak.asm.dip.hap1.p_ctg.gfa","r")
# inputGFA_2 = open("HN_Yak.asm.dip.hap2.p_ctg.gfa","r")
# outputFa_1 = open("HN_Yak.rephased_hap1.fa","w")
# outputFa_2 = open("HN_Yak.rephased_hap2.fa","w")
# outputFa_3 = open("HN_Yak.rephased_hap3.fa","w")

information = open("Information.txt","w")

countReads = 0
common = 0
paternal = 0
maternal = 0
first = True
switch = []
switchA = []
totSize = 0
totSizeA = 0
totSizeL = []
totSizeAL = []
information.write("Total number of reads in fastq: 10 282 406 \n")

for lines in inputGFA_1:
    line = lines.split('\t')
    if line[0]=="S":
        if first == True:
            name = line[1]+"_hap1"
            sequence = line[2]
            size = int(line[3].strip('LN:i:'))
            coverage = line[4].strip('rd:i:').strip("\n")
            first = False
        else:
            if paternal > maternal:
                outputFa_1.write(">"+str(name)+"\t"+str(size)+"\t"+str(coverage)+"\tp"+str(paternal)+"\tm"+str(maternal)+"\ta"+str(common)+"\n"+str(sequence)+"\n")
            if maternal > paternal:
                switch.append(str(name))
                totSize += int(size)
                totSizeL.append(size)
                outputFa_2.write(">"+str(name)+"\t"+str(size)+"\t"+str(coverage)+"\tp"+str(paternal)+"\tm"+str(maternal)+"\ta"+str(common)+"\n"+str(sequence)+"\n")
            if paternal == maternal:
                switchA.append(str(name))
                totSizeA += int(size)
                totSizeAL.append(size)
                outputFa_3.write(">"+str(name)+"\t"+str(size)+"\t"+str(coverage)+"\tp"+str(paternal)+"\tm"+str(maternal)+"\ta"+str(common)+"\n"+str(sequence)+"\n")
            name = line[1]+"_hap1"
            sequence = line[2]
            size = line[3].strip('LN:i:')
            coverage = line[4].strip('rd:i:')
            common = 0
            paternal = 0
            maternal = 0


    if line[0]=="A":
        countReads += 1
        if str(line[8].strip("\n"))=="HG:A:a":
            common += 1
        if str(line[8].strip("\n"))=="HG:A:p":
            paternal += 1
        if str(line[8].strip("\n"))=="HG:A:m":
            maternal += 1

information.write("Number of reads in hap1 (before correction): "+str(countReads)+"\n")
information.write("Number of ctg in hap1(paternal) switched to hap2(maternal): "+str(len(switch))+str("\n"))
information.write("Switched size global: " + str(totSize) +str("\n"))
information.write("Switched size list: " + str(totSizeL) +str("\n"))
information.write("name of the switched contigs: \n")
information.write(str(switch)+"\n\n")

information.write("Number of ctg in hap1(paternal) switched to hap3(common): "+str(len(switchA))+str("\n"))
information.write("Switched size global: " + str(totSizeA) +str("\n"))
information.write("Switched size list: " + str(totSizeAL) +str("\n"))
information.write("name of the switched contigs: \n")
information.write(str(switchA)+"\n\n")

countReads = 0
common = 0
paternal = 0
maternal = 0
switch = []
switchA = []
totSize = 0
totSizeA = 0
totSizeL = []
totSizeAL = []


first = True
for lines in inputGFA_2:
    line = lines.split('\t')
    if line[0]=="S":
        if first == True:
            name = line[1]+"_hap2"
            sequence = line[2]
            size = int(line[3].strip('LN:i:'))
            coverage = line[4].strip('rd:i:').strip("\n")
            first = False
        else:
            if paternal > maternal:
                switch.append(str(name))
                totSize += int(size)
                totSizeL.append(size)
                outputFa_1.write(">"+str(name)+"\t"+str(size)+"\t"+str(coverage)+"\tp"+str(paternal)+"\tm"+str(maternal)+"\ta"+str(common)+"\n"+str(sequence)+"\n")
            if maternal > paternal:
                outputFa_2.write(">"+str(name)+"\t"+str(size)+"\t"+str(coverage)+"\tp"+str(paternal)+"\tm"+str(maternal)+"\ta"+str(common)+"\n"+str(sequence)+"\n")
            if paternal == maternal:
                switchA.append(str(name))
                totSizeA += int(size)
                totSizeAL.append(size)
                outputFa_3.write(">"+str(name)+"\t"+str(size)+"\t"+str(coverage)+"\tp"+str(paternal)+"\tm"+str(maternal)+"\ta"+str(common)+"\n"+str(sequence)+"\n")
            name = line[1]+"_hap2"
            sequence = line[2]
            size = line[3].strip('LN:i:')
            coverage = line[4].strip('rd:i:')
            common = 0
            paternal = 0
            maternal = 0


    if line[0]=="A":
        countReads += 1
        if str(line[8].strip("\n"))=="HG:A:a":
            common += 1
        if str(line[8].strip("\n"))=="HG:A:p":
            paternal += 1
        if str(line[8].strip("\n"))=="HG:A:m":
            maternal += 1

information.write("Number of reads in hap2 (before correction): "+str(countReads)+"\n")
information.write("Number of ctg in hap2(maternal) switched to hap1(paternal): "+str(len(switch))+str("\n"))
information.write("Switched size global: " + str(totSize) +str("\n"))
information.write("Switched size list: " + str(totSizeL) +str("\n"))
information.write("name of the switched contigs: \n")
information.write(str(switch)+"\n\n")

information.write("Number of ctg in hap2(maternal) switched to hap3(common): "+str(len(switchA))+str("\n"))
information.write("Switched size global: " + str(totSizeA) +str("\n"))
information.write("Switched size list: " + str(totSizeAL) +str("\n"))
information.write("name of the switched contigs: \n")
information.write(str(switchA)+"\n\n")
