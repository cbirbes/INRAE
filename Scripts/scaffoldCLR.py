from Bio.Seq import Seq


# Creation des dictionnaires avec info sur les paires de contigs a jointer.
def create_Dict():
    outputSam = open("filteredSam.sam","w")

    dictLink = {}
    dictLinkReads = {}
    test = 0

    for line in open("ListReadsTwiceAligned.sam","r"):
        if ("SA:Z:ptg" in line) and (line.split("\t")[2] != line.split("\t")[-2].split(",")[0][5:]) :
            outputSam.write(line)
            if (line.split("\t")[2]+"-"+line.split("\t")[-2].split(",")[0][5:]) in dictLink :
                dictLink[line.split("\t")[2]+"-"+line.split("\t")[-2].split(",")[0][5:]] += 1
                dictLinkReads[line.split("\t")[2]+"-"+line.split("\t")[-2].split(",")[0][5:]].append(line.split("\t")[1]+"/"+line.split("\t")[5]+"/"+line.split("\t")[9]+"/"+line.split("\t")[-2])
            elif (line.split("\t")[-2].split(",")[0][5:]+"-"+line.split("\t")[2]) in dictLink:
                dictLink[line.split("\t")[-2].split(",")[0][5:]+"-"+line.split("\t")[2]] += 1
                dictLinkReads[line.split("\t")[-2].split(",")[0][5:]+"-"+line.split("\t")[2]].append(line.split("\t")[1]+"/"+line.split("\t")[5]+"/"+line.split("\t")[9]+"/"+line.split("\t")[-2])
            else:
                dictLink[line.split("\t")[2]+"-"+line.split("\t")[-2].split(",")[0][5:]] = 1
                dictLinkReads[line.split("\t")[2]+"-"+line.split("\t")[-2].split(",")[0][5:]] = [line.split("\t")[1]+"/"+line.split("\t")[5]+"/"+line.split("\t")[9]+"/"+line.split("\t")[-2]]
    outputSam.close()

    dictionnaire = open("dictLink.dict",'w')
    dictionnaire.write(str(dictLink))
    dictionnaire.close()

    dictionnaireReads = open("dictLinkReads.dict",'w')
    dictionnaireReads.write(str(dictLinkReads))
    dictionnaireReads.close()

    return dictLink, dictLinkReads
# Fin creation des dictionnaires

dictLink, dictLinkReads = create_Dict()

dictionnaireNotUsed = open("notUsed.dict","w")
finalFasta = open("finalFasta.fasta","w")
listAlreadyUsed = []
search1 = True
search2 = True
for key, value in dictLink.items():
    if value > 5:
        print("value >5")
        listAlignement = []
        if (str(key[0:10]) in listAlreadyUsed) or (str(key[11:21]) in listAlreadyUsed):
            dictionnaireNotUsed.write(str(key) + " " + str(value)+"\n")
            print("Deja utilise un contig dici")
        else:
            print("on fait un scaffolding")
            print("on verifie les sens d'alignement des reads")
            for readsInfo in dictLinkReads[key]:
                if int(readsInfo[0]) & 16 == 0:
                    listAlignement.append("+"+readsInfo.split("/")[3].split(",")[2])
                else:
                    print(str(readsInfo))
                    listAlignement.append("-"+readsInfo.split("/")[3].split(",")[2])
            countok = 0
            countswap = 0
            for strand in listAlignement:
                if strand == "++" or strand == "--":
                    countok += 1
                if strand == "+-" or strand == "-+":
                    countswap += 1
            listAlreadyUsed.append(str(key[0:10]))
            listAlreadyUsed.append(str(key[11:21]))
            fasta = open("coturnix.bp.p_ctg.gfaOneLine.fa","r")
            compteur = 0
            while search1 == True or search2 == True:
                if compteur %2 == 0 :
                    nameCtg = fasta.readline().strip("\n")
                    compteur += 1
                    if nameCtg == str(">"+key[0:10]) and search1:
                        print("on a trouve 1")
                        search1 = False
                        seq1 = Seq(fasta.readline())
                        fasta.readline()
                    if nameCtg == str(">"+key[11:21]) and search2:
                        print("on a trouve 2")
                        search2 = False
                        seq2 = Seq(fasta.readline())
                        fasta.readline()
                else:
                    fasta.readline()
                    compteur += 1
            fasta.close()
            if countok > countswap:
                print("on les jointe")
                finalFasta.write(str(">"+key+"\n"))
                finalFasta.write(str(seq1+"NNNNNNNNNN"+seq2))
            else:
                print("on les jointe Swap")
                finalFasta.write(str(">"+key+"\n"))
                finalFasta.write(str(seq1+"NNNNNNNNNN"+seq2.reverse_complement()))
            search1 = True
            search2 = True
