import random
import argparse

parser = argparse.ArgumentParser(description='Create random fasta file and apply mutations')
parser.add_argument('--FastaSize', help = "Taille de la sequence", required=False, default=30000000)

args = vars(parser.parse_args())

# Création des valeurs de bases : liste de nucleotides, liste d'evenements et taille du fichier fasta (nombre de caractères), Compteur de modifications pour connaitre la différence de taille entre sesquence initiale et finale
# Taukke minimale et maximale des évènements
Nucleotides = ["A","T","C","G"]
GC = ["G","C"]

FastaSize  = int(args['FastaSize'])
Size=0


# Preparation des fichiers Output
ReferenceFile = open("Reference.fasta", "w")
FastaSeq=[]

# Création de la séquence de manière aléatoire

while (Size < FastaSize):
    if random.randint(1,100000)==100000:
        if random.randint(1,100)<70:
            #Insert HomoPolymer
            test = random.randint(1,100)
            if test<65:
                Base=random.choice(Nucleotides)
                Taille=random.randint(10,40)
                for x in range (0,Taille):
                    FastaSeq.append(Base)
                    Size +=1
            elif test<85:
                Base=random.choices(Nucleotides, k=2)
                Taille=random.randint(6,20)
                for x in range (0,Taille):
                    FastaSeq.append(Base)
                    Size +=1

            elif test<95:
                Base=random.choices(Nucleotides, k=3)
                Taille=random.randint(5,15)
                for x in range (0,Taille):
                    FastaSeq.append(Base)
                    Size +=1

            elif test<=100:
                Base=random.choices(Nucleotides, k=4)
                Taille=random.randint(4,12)
                for x in range (0,Taille):
                    FastaSeq.append(Base)
                    Size +=1

        else:
            #Insert GC rich
            for x in range (0,random.randint(100,700)):
                FastaSeq.append(random.choice(GC))
                Size +=1

    else:
        FastaSeq.append(random.choice(Nucleotides))
        Size +=1

ReferenceFile.write(">Sequence1\n")
ReferenceFile.write(str(FastaSeq).upper())
ReferenceFile.close()
print(len(FastaSeq))
