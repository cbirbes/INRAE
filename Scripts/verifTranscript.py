import argparse

parser = argparse.ArgumentParser(description='')
parser.add_argument('--flye', type=str, required=True, help='flye paf')
parser.add_argument('--wtdbg2', type=str, required=True, help='wtdbg2 paf')
parser.add_argument('--reference', type=str, required=True, help='reference')
parser.add_argument('--type', type=str, required=True, help='alignment type (cdna or cds)')

args = vars(parser.parse_args())
flyePaf = args['flye']
wtdbg2Paf = args['wtdbg2']
reference = args['reference']
name = args['type']

inputReference = open(reference,"r")
inputPafFlye = open(flyePaf,"r")
inputPafWtdbg2 = open(wtdbg2Paf,"r")

totalFlye = open(name+"FlyeListGenes.txt",'w')
totalWtdbg2 = open(name+"Wtdbg2ListGenes.txt","w")

missingFlye = open(name+"missingFlye.txt","w")
missingWtdbg2 = open(name+"missingWtdbg2.txt","w")

goodFlye = open(name+"FlyeGoodGenes.txt",'w')
goodWtdbg2 = open(name+"Wtdbg2GoodGenes.txt","w")

transcriptList = open(name+"Reference.txt","w")


listTranscript = []

for line in inputReference:
    if line.startswith(">"):
        listTranscript.append(line.strip(">").split(" ")[0])

for line in listTranscript:
    transcriptList.write(str(line)+"\n")

dejaVu = []
for line in inputPafFlye:
    lines = line.split("\t")
    if lines[0] not in dejaVu:
        totalFlye.write(lines[0]+"\n")
        dejaVu.append(lines[0])
        if abs(int(lines[3])-int(lines[2])) > (0.9*(int(lines[1]))):
            goodFlye.write(lines[0]+"\n")

for line in listTranscript:
    if line not in dejaVu:
        missingFlye.write(str(line)+"\n")


dejaVu = []
for line in inputPafWtdbg2:
    lines = line.split("\t")
    if lines[0] not in dejaVu:
        totalWtdbg2.write(lines[0]+"\n")
        dejaVu.append(lines[0])
        if abs(int(lines[3])-int(lines[2])) > (0.9*(int(lines[1]))):
            goodWtdbg2.write(lines[0]+"\n")

for line in listTranscript:
    if line not in dejaVu:
        missingWtdbg2.write(str(line)+"\n")
