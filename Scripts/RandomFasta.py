import random
import argparse

parser = argparse.ArgumentParser(description='Create random fasta file and apply mutations')
parser.add_argument('--DeletionRate', help = "Probabilite de deletion [0:1], Del+Inv+Ins = 1", required=False, default=0.33)
parser.add_argument('--InversionRate', help = "Probabilite d'inversion' [0:1], Del+Inv+Ins = 1", required=False, default=0.33)
parser.add_argument('--InsertionRate', help = "Probabilite d'insertion' [0:1], Del+Inv+Ins = 1", required=False, default=0.33)
parser.add_argument('--DuplicationRate', help = "Probabilite de dupliquer la sequence au lieu de simplement la deplacer", required=False, default=0.5)
parser.add_argument('--FastaSize', help = "Taille de la sequence", required=False, default=100000)
parser.add_argument('--MinSize', help = "Taille minimale des modifications", required=False, default=10)
parser.add_argument('--MaxSize', help = "Taille maximale des modifications", required=False, default=200)
parser.add_argument('--Event', help = "Nombre maximum de modifications", required=False, default=2000)

args = vars(parser.parse_args())

# Création des valeurs de bases : liste de nucleotides, liste d'evenements et taille du fichier fasta (nombre de caractères), Compteur de modifications pour connaitre la différence de taille entre sesquence initiale et finale
# Taukke minimale et maximale des évènements
Nucleotides = ["A","T","C","G"]
Evenements = ["Insertion","Deletion","Inversion"]
PDeletion = float(args['DeletionRate'])
PInversion = float(args['InversionRate'])
PInsertion = float(args['InsertionRate'])
PDuplication = float(args['DuplicationRate'])
Probabilites = [PInsertion, PDeletion, PInversion]
FastaSize  = int(args['FastaSize'])
TailleMax = int(args['MaxSize'])
TailleMin = int(args['MinSize'])
Event = int(args['Event'])
PosEvenement = []
TailleEvenement = []
CompteurModif = 0
InsertionValue = 0

# Preparation des fichiers Output
Changements = open("changes.gff", "w")
FastaModifiedFile = open("fastaModified.fasta", "w")
FastaOriginalFile = open("fastaOriginal.fasta", "w")


# Création de la séquence de manière aléatoire
# Un exemplaire est modifié aléatoirement, l'autre est conservé tel quel
## test=random.choices(Nucleotides, k=20000000)
FastaSeq = random.choices(Nucleotides, k=FastaSize)
OriginalSeq = list(FastaSeq)
for cpt, x in enumerate(OriginalSeq):
    if (cpt%80==0 and cpt!=0):
        OriginalSeq.insert(cpt-1,'\n')
FastaOriginalFile.write(">Sequence1\n")
FastaOriginalFile.write("".join(OriginalSeq).lower())


# Création des évènements de manière aléatoire. Nombre d'evenement aléatoire puis une liste aléatoire indiquant la position et la taille de l'évènement
# Si deux évènements sont trop proches, on supprime l'évènement+1
NombreEvenement = random.randint(1, Event)
for i in range(NombreEvenement):
    PosEvenement.append(random.randint(0, FastaSize))
    TailleEvenement.append(random.randint(TailleMin, TailleMax))
PosEvenement.sort()
x=0
while (x < len(PosEvenement)):
    if (x+1 < len(PosEvenement)):
        if (PosEvenement[x]+1000 > PosEvenement[x+1]):
            del PosEvenement[x+1]
        else:
            x+=1
    else:
        x+=1
print ("Position des évènements déterminée")




# Debut des modifications. On choisit d'abord une modification au hasard dans la liste. On fait ensuite un traitement différent en fonction de la modification.
for x in range(len(PosEvenement)):
    if (PosEvenement[x]>len(FastaSeq)-InsertionValue):
        break
    if (x%10 == 0):
        print(str(x)+" Modifications effectuées")

    TypeEvenement = random.choices(Evenements, Probabilites)
    print(TypeEvenement)

    # Si la modification est une insertion: On définit deux cas: la duplication ou l'insertion.
    if (TypeEvenement == ["Insertion"]):
        # Si c'est une duplication: On Enregistre la sequence [Position:Position+taille] et on l'insere a un endroit aléatoire de FastaSeq

        if random.uniform(0,1) < PDuplication:
            InsertionSeq = [z for z in FastaSeq[len(FastaSeq)-TailleEvenement[x]-InsertionValue:len(FastaSeq)-InsertionValue]]
            for cpt, y in enumerate(InsertionSeq):
                FastaSeq.insert(PosEvenement[x]+cpt-1, y)
            Changements.write("Sequence1\tRandomFasta.py\tDuplication\t" + str(PosEvenement[x]+CompteurModif) + "\t" + str(PosEvenement[x]+CompteurModif+TailleEvenement[x]) + "\t.\t.\t.\tPosition_Origine: "+ str(len(FastaSeq)-1-TailleEvenement[x]-InsertionValue) + "FastaSize_impact: +" + str(TailleEvenement[x]) + "\n")
            CompteurModif += TailleEvenement[x]
            InsertionValue += TailleEvenement[x]

        # Si c'est une insertion: On Enregistre la sequence [Position:Position+taille], on la supprime et on l'insere a un endroit aléatoire de FastaSeq
        else:
            InsertionSeq = [z for z in FastaSeq[len(FastaSeq)-TailleEvenement[x]-InsertionValue:len(FastaSeq)-InsertionValue]]
            del FastaSeq[len(FastaSeq)-TailleEvenement[x]-InsertionValue:len(FastaSeq)-InsertionValue]
            for cpt, y in enumerate(InsertionSeq):
                FastaSeq.insert(PosEvenement[x]+cpt-1, y)
            Changements.write("Sequence1\tRandomFasta.py\tInsertion\t" + str(PosEvenement[x]+CompteurModif) + "\t" + str(PosEvenement[x]+CompteurModif+TailleEvenement[x]) + "\t.\t.\t.\tPosition_Origine: "+ str(len(FastaSeq)-1-TailleEvenement[x]-InsertionValue) + "FastaSize_impact: 0\n")


    # Si la modification est une délétion: On supprime tous les éléments dans l'intervalle [Position:Position+taille], si on est en bout de sequence : [Position:-1]
    elif (TypeEvenement == ["Deletion"]):
        if (len(FastaSeq)>(PosEvenement[x])+CompteurModif+TailleEvenement[x]):
            del FastaSeq[PosEvenement[x]+CompteurModif:PosEvenement[x]+CompteurModif+TailleEvenement[x]]
        else:
            TailleEvenement[x]=(len(FastaSeq)-(PosEvenement[x]+CompteurModif)-1)
            print(len(FastaSeq)-TailleEvenement[x])
            del FastaSeq[PosEvenement[x]+CompteurModif:-1]
            print(len(FastaSeq))

        Changements.write("Sequence1\tRandomFasta.py\tDeletion\t" + str(PosEvenement[x]+CompteurModif) + "\t" + str(PosEvenement[x]+CompteurModif+TailleEvenement[x]) + "\t.\t.\t.\tFastaSize_impact: -" + str(TailleEvenement[x]) + "\n")
        CompteurModif -= TailleEvenement[x]



    # Si la modification est une inversion: On remplace la séquence de [Position:Position+taille] par son reverse complément inversé.
    elif (TypeEvenement == ["Inversion"]):
        InversionSeq = [z for z in FastaSeq[PosEvenement[x]+CompteurModif-1:PosEvenement[x]+CompteurModif+TailleEvenement[x]-1]]
        if (TailleEvenement[x]>len(InversionSeq)):
            TailleEvenement[x]=len(InversionSeq)
        ReverseSeq = InversionSeq[::-1]
        for compteur, nuc in enumerate(ReverseSeq):
            if nuc == "A":
                ReverseSeq[compteur] = "T"
            if nuc == "T":
                ReverseSeq[compteur] = "A"
            if nuc == "C":
                ReverseSeq[compteur] = "G"
            if nuc == "G":
                ReverseSeq[compteur] = "C"
        FastaSeq[PosEvenement[x]+CompteurModif-1:PosEvenement[x]+CompteurModif+TailleEvenement[x]-1]=ReverseSeq
        Changements.write("Sequence1\tRandomFasta.py\tInversion\t" + str(PosEvenement[x]+CompteurModif) + "\t" + str(PosEvenement[x]+CompteurModif+TailleEvenement[x]) + "\t.\t.\t.\tFastaSize_impact: 0\n")

for cpt, x in enumerate(FastaSeq):
    if (cpt%80==0 and cpt!=0):
        FastaSeq.insert(cpt-1,'\n')
FastaModifiedFile.write(">Sequence1\n")
FastaModifiedFile.write("".join(FastaSeq).lower())
